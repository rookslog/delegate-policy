import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CHECK_STATE = REPO / "check_state.py"
CHECK_WIDS = REPO / "check_wids.py"
INSTALL = importlib.import_module("install")
CHECK_WIDS_MODULE = importlib.import_module("check_wids")


def run_python(script, *args):
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )


class CheckerCliTests(unittest.TestCase):
    def test_check_state_today_value_is_not_misparsed_as_state_path(self):
        completed = run_python(CHECK_STATE, "--today", "2026-07-12")

        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("as of 2026-07-12: OK", completed.stdout)

    def test_check_wids_source_scope_is_explicitly_accepted(self):
        completed = run_python(CHECK_WIDS, "--scope", "source")

        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("cited: OK", completed.stdout)

    def test_check_wids_deployment_requires_manifest(self):
        with tempfile.TemporaryDirectory() as installation_root:
            completed = run_python(
                CHECK_WIDS,
                "--scope",
                "deployment",
                installation_root,
            )

        self.assertNotEqual(0, completed.returncode)
        self.assertIn("--manifest", completed.stderr)


class PackagePlanTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(
            hasattr(INSTALL, "PackageSpecError"),
            "install.PackageSpecError must define fail-closed package errors",
        )
        self.assertTrue(
            hasattr(INSTALL, "load_package_spec"),
            "install.load_package_spec must load schema-versioned policy",
        )
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name) / "source"
        self.repo.mkdir()
        self.destination = Path(self.temp.name) / "claude-root"
        self._git("init", "-q")
        self._git("config", "user.name", "Package Test")
        self._git("config", "user.email", "package-test@example.invalid")

    def tearDown(self):
        self.temp.cleanup()

    def _git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.repo), *args],
            capture_output=True,
            text=True,
            check=True,
        )

    def _write(self, relative, text="fixture\n"):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def _base_spec(self):
        return {
            "schema_version": 1,
            "exact_files": [
                {
                    "source": "SKILL.md",
                    "destination": "skills/delegate-triage/SKILL.md",
                },
                {
                    "source": "probes/README.md",
                    "destination": "skills/delegate-triage/probes/README.md",
                },
                {
                    "source": "adapters/claude-code/delegation.md",
                    "destination": "delegation.md",
                },
            ],
            "tracked_globs": [
                {
                    "pattern": "agents/*.md",
                    "destination_prefix": "agents",
                    "exclude": ["agents/MANIFEST.md"],
                },
                {
                    "pattern": "probes/records/*.md",
                    "destination_prefix": "skills/delegate-triage/probes/records",
                    "exclude": [],
                },
            ],
            "forbidden_parts": [".git", "fixtures", "runtime"],
            "forbidden_names": [".DS_Store", "prompt.md"],
            "source_only_links": [],
            "required_integrity_commands": [
                "python3 check_state.py ROOT/skills/delegate-triage/STATE.md",
                "python3 check_wids.py --scope deployment --manifest ROOT/delegate-triage-package-manifest.json ROOT",
                "python3 install.py claude-code --root ROOT --check",
            ],
        }

    def _commit_fixture(self, spec=None):
        self._write("SKILL.md")
        self._write("probes/README.md")
        self._write("probes/records/tracked.md")
        self._write("agents/reviewer.md")
        self._write("agents/MANIFEST.md")
        self._write("adapters/claude-code/delegation.md")
        spec_path = self._write(
            "adapters/claude-code/package-spec.json",
            json.dumps(spec or self._base_spec()),
        )
        self._git("add", ".")
        self._git("commit", "-qm", "fixture")
        return spec_path

    def _plan(self, spec_path):
        old_pkg = INSTALL.PKG
        try:
            INSTALL.PKG = self.repo
            spec = INSTALL.load_package_spec(spec_path)
            return INSTALL.claude_code_plan(self.destination, spec)
        finally:
            INSTALL.PKG = old_pkg

    def test_plan_selects_only_declared_tracked_regular_files(self):
        spec_path = self._commit_fixture()
        self._write("probes/records/untracked.md")
        self._write("probes/fixtures/private.md")
        self._write("probes/runtime/run-1/prompt.md")
        self._write("probes/fixtures/nested/.git/config")

        pairs = self._plan(spec_path)

        actual = [str(destination.relative_to(self.destination)) for _, destination in pairs]
        self.assertEqual(
            [
                "agents/reviewer.md",
                "delegation.md",
                "skills/delegate-triage/SKILL.md",
                "skills/delegate-triage/probes/README.md",
                "skills/delegate-triage/probes/records/tracked.md",
            ],
            actual,
        )

    def test_plan_rejects_invalid_spec_and_source_shapes(self):
        cases = {
            "unsupported schema": {"schema_version": 2},
            "absolute destination": {
                "exact_files": [{"source": "SKILL.md", "destination": "/tmp/escape"}]
            },
            "traversal destination": {
                "exact_files": [{"source": "SKILL.md", "destination": "../escape"}]
            },
            "duplicate destination": {
                "exact_files": [
                    {"source": "SKILL.md", "destination": "same.md"},
                    {"source": "probes/README.md", "destination": "same.md"},
                ]
            },
            "missing source": {
                "exact_files": [{"source": "missing.md", "destination": "missing.md"}]
            },
        }
        for name, updates in cases.items():
            with self.subTest(name=name):
                spec = self._base_spec()
                spec.update(updates)
                spec_path = self._commit_fixture(spec)
                with self.assertRaises(INSTALL.PackageSpecError):
                    self._plan(spec_path)

    def test_plan_rejects_symlink_source(self):
        spec = self._base_spec()
        spec["exact_files"].append(
            {"source": "linked.md", "destination": "skills/delegate-triage/linked.md"}
        )
        spec_path = self._commit_fixture(spec)
        os.symlink("SKILL.md", self.repo / "linked.md")
        self._git("add", "linked.md")
        self._git("commit", "-qm", "track symlink")

        with self.assertRaises(INSTALL.PackageSpecError):
            self._plan(spec_path)


class RepositoryPackageSpecTests(unittest.TestCase):
    def test_operator_xhigh_review_override_is_documented_and_deliverable(self):
        contract = (REPO / "CONTRACT.md").read_text(encoding="utf-8")
        routes = (REPO / "ROUTES.md").read_text(encoding="utf-8")
        reviewer_xhigh = (REPO / "agents" / "reviewer-xhigh.md").read_text(encoding="utf-8")

        self.assertIn("### §2a Operator declaration overrides the route", contract)
        self.assertIn("An explicitly declared model, effort, or pin", contract)
        self.assertIn("Record the override in the fit line", contract)
        self.assertIn(
            "explicit operator declaration > project overlay > profile delta > this table",
            routes,
        )
        self.assertRegex(reviewer_xhigh, r"(?m)^name: reviewer-xhigh$")
        self.assertRegex(reviewer_xhigh, r"(?m)^model: opus$")
        self.assertRegex(reviewer_xhigh, r"(?m)^effort: xhigh$")

        spec_path = REPO / "adapters" / "claude-code" / "package-spec.json"
        spec = INSTALL.load_package_spec(spec_path)
        pairs = INSTALL.claude_code_plan(Path("/tmp/declared-claude-root"), spec)
        destinations_by_source = {
            str(source.relative_to(REPO)): str(destination)
            for source, destination in pairs
        }
        self.assertEqual(
            "/tmp/declared-claude-root/agents/reviewer-xhigh.md",
            destinations_by_source["agents/reviewer-xhigh.md"],
        )

    def test_repository_spec_resolves_the_bounded_sixty_seven_file_package(self):
        spec_path = REPO / "adapters" / "claude-code" / "package-spec.json"
        self.assertTrue(spec_path.is_file(), "the reviewed package specification must exist")
        spec = INSTALL.load_package_spec(spec_path)

        pairs = INSTALL.claude_code_plan(Path("/tmp/declared-claude-root"), spec)
        sources = [str(source.relative_to(REPO)) for source, _ in pairs]

        # 67 = the 65-file xhigh-override package + the two 2026-08-14 probe records
        # (family-rename flash legs, S4 crosswalk mapping) swept in by the records glob.
        self.assertEqual(67, len(pairs))
        self.assertIn("SKILL.md", sources)
        self.assertIn("probes/INDEX.md", sources)
        self.assertIn("probes/records/P-20260731-pst-paired-trial.md", sources)
        self.assertIn("probes/records/P-20260805-effort-surface-and-pin-registration.md", sources)
        self.assertIn("probes/records/P-20260807-pin-registration-turn-boundary.md", sources)
        self.assertIn("probes/records/P-20260814-family-rename-flash-legs.md", sources)
        self.assertIn("probes/records/P-20260814-s4-crosswalk-mapping.md", sources)
        self.assertIn("agents/implementer-high.md", sources)
        self.assertIn("agents/reviewer.md", sources)
        self.assertIn("agents/reviewer-max.md", sources)
        self.assertIn("agents/reviewer-xhigh.md", sources)
        self.assertIn("adapters/claude-code/delegation.md", sources)
        self.assertNotIn("agents/MANIFEST.md", sources)
        self.assertFalse(any("fixtures" in Path(source).parts for source in sources))
        self.assertFalse(any("runtime" in Path(source).parts for source in sources))
        self.assertFalse(any(".git" in Path(source).parts for source in sources))
        self.assertFalse(any(Path(source).name == "prompt.md" for source in sources))
        self.assertEqual(
            [
                "python3 check_state.py ROOT/skills/delegate-triage/STATE.md",
                "python3 check_wids.py --scope deployment --manifest ROOT/delegate-triage-package-manifest.json ROOT",
                "python3 install.py claude-code --root ROOT --check",
            ],
            spec["required_integrity_commands"],
        )


class ManifestTests(unittest.TestCase):
    def setUp(self):
        for name in (
            "DirtySourceError",
            "build_manifest",
            "manifest_bytes",
            "require_clean_source",
        ):
            self.assertTrue(hasattr(INSTALL, name), f"install.{name} must exist")

    def test_manifest_is_deterministic_and_spans_all_declared_destinations(self):
        spec_path = REPO / "adapters" / "claude-code" / "package-spec.json"
        spec = INSTALL.load_package_spec(spec_path)
        root = Path("/tmp/manifest-claude-root")
        pairs = INSTALL.claude_code_plan(root, spec)
        source_commit = subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()

        first = INSTALL.build_manifest(pairs, spec, source_commit, spec_path)
        second = INSTALL.build_manifest(pairs, spec, source_commit, spec_path)
        first_bytes = INSTALL.manifest_bytes(first)
        second_bytes = INSTALL.manifest_bytes(second)

        self.assertEqual(first_bytes, second_bytes)
        self.assertTrue(first_bytes.endswith(b"\n"))
        self.assertEqual(1, first["schema_version"])
        self.assertEqual(source_commit, first["source_commit"])
        self.assertFalse(first["dirty_source"])
        self.assertEqual(67, len(first["entries"]))
        self.assertEqual(
            sorted(entry["destination"] for entry in first["entries"]),
            [entry["destination"] for entry in first["entries"]],
        )
        self.assertEqual(13, len(first["source_only_links"]))
        self.assertEqual(
            {"destination", "source", "size", "mode", "sha256"},
            set(first["entries"][0]),
        )
        self.assertTrue(all(entry["mode"] in ("0644", "0755") for entry in first["entries"]))
        self.assertEqual(
            __import__("hashlib").sha256(spec_path.read_bytes()).hexdigest(),
            first["package_spec_sha256"],
        )

    def test_clean_source_gate_rejects_tracked_untracked_and_staged_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            subprocess.run(["git", "-C", directory, "init", "-q"], check=True)
            subprocess.run(["git", "-C", directory, "config", "user.name", "Clean Test"], check=True)
            subprocess.run(
                ["git", "-C", directory, "config", "user.email", "clean@example.invalid"],
                check=True,
            )
            tracked = repo / "tracked.txt"
            tracked.write_text("clean\n", encoding="utf-8")
            subprocess.run(["git", "-C", directory, "add", "tracked.txt"], check=True)
            subprocess.run(["git", "-C", directory, "commit", "-qm", "clean"], check=True)

            INSTALL.require_clean_source(repo)

            tracked.write_text("dirty\n", encoding="utf-8")
            with self.assertRaises(INSTALL.DirtySourceError):
                INSTALL.require_clean_source(repo)
            tracked.write_text("clean\n", encoding="utf-8")

            untracked = repo / "untracked.txt"
            untracked.write_text("new\n", encoding="utf-8")
            with self.assertRaises(INSTALL.DirtySourceError):
                INSTALL.require_clean_source(repo)
            untracked.unlink()

            tracked.write_text("staged\n", encoding="utf-8")
            subprocess.run(["git", "-C", directory, "add", "tracked.txt"], check=True)
            with self.assertRaises(INSTALL.DirtySourceError):
                INSTALL.require_clean_source(repo)


class DeploymentManifestTests(unittest.TestCase):
    def setUp(self):
        for name in ("ValidationResult", "validate_deployment"):
            self.assertTrue(hasattr(CHECK_WIDS_MODULE, name), f"check_wids.{name} must exist")
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.root = self.base / "claude-root"
        self.root.mkdir()
        self.manifest_path = self.root / "delegate-triage-package-manifest.json"
        self.stamp_path = self.base / "canonical-MANIFEST.md"
        self.entries = []
        self._add_file(
            "skills/delegate-triage/WARRANTS.md",
            "# Warrants\n\n### W-001 Fixture\n\nClaim.\n",
            "WARRANTS.md",
        )
        self._add_file(
            "skills/delegate-triage/probes/record.md",
            "# Record\n\nUses W-001.\n",
            "probes/record.md",
        )
        self._add_file("agents/reviewer.md", "# Reviewer\n", "agents/reviewer.md")
        self._add_file("delegation.md", "# Delegation\n", "adapters/claude-code/delegation.md")
        self.manifest = {
            "schema_version": 1,
            "source_commit": "a" * 40,
            "dirty_source": False,
            "package_spec_sha256": "b" * 64,
            "entries": self.entries,
            "source_only_links": [],
        }
        self._write_manifest()

    def tearDown(self):
        self.temp.cleanup()

    def _add_file(self, destination, content, source, mode="0644"):
        path = self.root / destination
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        path.chmod(int(mode, 8))
        data = content.encode("utf-8")
        self.entries.append(
            {
                "destination": destination,
                "source": source,
                "size": len(data),
                "mode": mode,
                "sha256": __import__("hashlib").sha256(data).hexdigest(),
            }
        )
        return path

    def _write_manifest(self, stamp=True):
        data = (
            json.dumps(self.manifest, sort_keys=True, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        self.manifest_path.write_bytes(data)
        if stamp:
            digest = __import__("hashlib").sha256(data).hexdigest()
            self.stamp_path.write_text(
                "# Deployment stamps\n\n"
                f"<!-- claude-package-manifest:v1 sha256={digest} "
                f"source_commit={'a' * 40} -->\n",
                encoding="utf-8",
            )

    def _replace_file(self, destination, content):
        path = self.root / destination
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        path.chmod(0o644)
        data = content.encode("utf-8")
        for entry in self.manifest["entries"]:
            if entry["destination"] == destination:
                entry.update(
                    size=len(data),
                    mode="0644",
                    sha256=__import__("hashlib").sha256(data).hexdigest(),
                )
                break
        else:
            self.manifest["entries"].append(
                {
                    "destination": destination,
                    "source": destination.removeprefix("skills/delegate-triage/"),
                    "size": len(data),
                    "mode": "0644",
                    "sha256": __import__("hashlib").sha256(data).hexdigest(),
                }
            )
        self._write_manifest()

    def _validate(self):
        return CHECK_WIDS_MODULE.validate_deployment(
            self.root,
            self.manifest_path,
            self.stamp_path,
        )

    def test_valid_manifest_covers_skill_agents_and_root_delegation(self):
        result = self._validate()

        self.assertTrue(result.ok, result.failures)
        self.assertEqual(4, result.checked_files)
        self.assertEqual([], result.extras)

    def test_manifest_shape_and_path_failures_are_fail_closed(self):
        mutations = {
            "unsupported schema": lambda: self.manifest.update(schema_version=2),
            "duplicate destination": lambda: self.manifest["entries"].append(
                dict(self.manifest["entries"][0])
            ),
            "absolute destination": lambda: self.manifest["entries"][0].update(
                destination="/tmp/escape"
            ),
            "traversal destination": lambda: self.manifest["entries"][0].update(
                destination="../escape"
            ),
            "dirty manifest": lambda: self.manifest.update(dirty_source=True),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                original = json.loads(json.dumps(self.manifest))
                mutate()
                self._write_manifest()
                self.assertFalse(self._validate().ok)
                self.manifest = original

    def test_installed_file_mismatches_fail(self):
        target = self.root / "skills/delegate-triage/probes/record.md"
        cases = {
            "missing": lambda: target.unlink(),
            "digest and size": lambda: target.write_text("changed\n", encoding="utf-8"),
            "mode": lambda: target.chmod(0o755),
        }
        for name, mutate in cases.items():
            with self.subTest(name=name):
                original = target.read_bytes()
                original_mode = target.stat().st_mode & 0o777
                try:
                    mutate()
                    self.assertFalse(self._validate().ok)
                finally:
                    if not target.exists():
                        target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(original)
                    target.chmod(original_mode)

    def test_full_root_agent_and_delegation_mismatches_fail(self):
        for destination in ("agents/reviewer.md", "delegation.md"):
            with self.subTest(destination=destination):
                target = self.root / destination
                original = target.read_bytes()
                try:
                    target.write_bytes(original + b"mutation\n")
                    self.assertFalse(self._validate().ok)
                finally:
                    target.write_bytes(original)

    def test_symlink_manifest_entry_fails(self):
        target = self.root / "agents/reviewer.md"
        content = target.read_bytes()
        target.unlink()
        backing = self.base / "reviewer-backing.md"
        backing.write_bytes(content)
        target.symlink_to(backing)

        self.assertFalse(self._validate().ok)

    def test_unlisted_skill_file_fails_but_extra_agent_is_reported(self):
        extra_skill = self.root / "skills/delegate-triage/unlisted.md"
        extra_skill.write_text("unlisted\n", encoding="utf-8")

        self.assertFalse(self._validate().ok)

        extra_skill.unlink()
        extra_agent = self.root / "agents/external-overlay.md"
        extra_agent.write_text("external\n", encoding="utf-8")
        result = self._validate()
        self.assertTrue(result.ok, result.failures)
        self.assertEqual(["agents/external-overlay.md"], result.extras)

    def test_missing_or_mismatched_external_stamp_fails(self):
        self.stamp_path.unlink()
        self.assertFalse(self._validate().ok)

        self.stamp_path.write_text(
            "<!-- claude-package-manifest:v1 "
            f"sha256={'0' * 64} source_commit={'a' * 40} -->\n",
            encoding="utf-8",
        )
        self.assertFalse(self._validate().ok)

    def test_exact_declared_missing_edge_is_reported_source_only(self):
        source = "skills/delegate-triage/probes/record.md"
        target = "../../docs/review.md"
        self._replace_file(source, f"# Record\n\nUses W-001 and [review]({target}).\n")
        self.manifest["source_only_links"] = [
            {"source": source, "target": target, "reason": "maintainer review"}
        ]
        self._write_manifest()

        result = self._validate()

        self.assertTrue(result.ok, result.failures)
        self.assertEqual([f"{source} -> {target}"], result.source_only)

    def test_undeclared_or_wrong_missing_edge_fails(self):
        source = "skills/delegate-triage/probes/record.md"
        target = "../../docs/review.md"
        self._replace_file(source, f"# Record\n\nUses W-001 and [review]({target}).\n")

        self.assertFalse(self._validate().ok)

        self.manifest["source_only_links"] = [
            {"source": source, "target": "../../docs/other.md", "reason": "wrong edge"}
        ]
        self._write_manifest()
        self.assertFalse(self._validate().ok)

    def test_declared_edge_fails_when_target_becomes_packaged(self):
        source = "skills/delegate-triage/probes/record.md"
        target = "../present.md"
        self._replace_file(source, f"# Record\n\nUses W-001 and [present]({target}).\n")
        self._replace_file("skills/delegate-triage/present.md", "# Present\n")
        self.manifest["source_only_links"] = [
            {"source": source, "target": target, "reason": "stale declaration"}
        ]
        self._write_manifest()

        self.assertFalse(self._validate().ok)

    def test_present_target_outside_root_or_absent_from_manifest_fails(self):
        source = "skills/delegate-triage/probes/record.md"
        outside_target = "../../../../outside.md"
        (self.base / "outside.md").write_text("outside\n", encoding="utf-8")
        self._replace_file(
            source,
            f"# Record\n\nUses W-001 and [outside]({outside_target}).\n",
        )
        outside_result = self._validate()
        self.assertFalse(outside_result.ok)
        self.assertIn(
            f"link target escapes installation root: {source} -> {outside_target}",
            outside_result.failures,
        )

        inside_unlisted = self.root / "unlisted.md"
        inside_unlisted.write_text("inside\n", encoding="utf-8")
        inside_target = "../../../unlisted.md"
        self._replace_file(
            source,
            f"# Record\n\nUses W-001 and [inside]({inside_target}).\n",
        )
        self.assertFalse(self._validate().ok)


class SourceDeclarationTests(unittest.TestCase):
    def test_source_scope_rejects_declaration_after_link_is_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / "adapters/claude-code").mkdir(parents=True)
            (package / "WARRANTS.md").write_text(
                "# Warrants\n\n### W-001 Fixture\n\nClaim.\n",
                encoding="utf-8",
            )
            (package / "source.md").write_text("Uses W-001 without a link.\n", encoding="utf-8")
            (package / "target.md").write_text("# Target\n", encoding="utf-8")
            spec = {
                "schema_version": 1,
                "exact_files": [],
                "tracked_globs": [],
                "forbidden_parts": [".git", "fixtures", "runtime"],
                "forbidden_names": [".DS_Store", "prompt.md"],
                "source_only_links": [
                    {"source": "source.md", "target": "target.md", "reason": "stale"}
                ],
            }
            (package / "adapters/claude-code/package-spec.json").write_text(
                json.dumps(spec),
                encoding="utf-8",
            )

            completed = run_python(CHECK_WIDS, package)

        self.assertNotEqual(0, completed.returncode)
        self.assertIn("declared source-only edge is not present", completed.stdout)


class IsolatedInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.source = self.base / "source"
        self.root = self.base / "claude-root"
        self.source.mkdir()

        spec_path = REPO / "adapters/claude-code/package-spec.json"
        spec = INSTALL.load_package_spec(spec_path)
        pairs = INSTALL.claude_code_plan(self.base / "unused-root", spec)
        copy_paths = {source.relative_to(REPO) for source, _ in pairs}
        copy_paths.update(
            {
                Path("install.py"),
                Path("adapters/claude-code/package-spec.json"),
                Path("agents/MANIFEST.md"),
            }
        )
        for relative in sorted(copy_paths):
            destination = self.source / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, destination)

        self._git("init", "-q")
        self._git("config", "user.name", "Isolated Install")
        self._git("config", "user.email", "isolated@example.invalid")
        self._git("add", ".")
        self._git("commit", "-qm", "clean package source")

    def tearDown(self):
        self.temp.cleanup()

    def _git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.source), *args],
            capture_output=True,
            text=True,
            check=True,
        )

    def _run(self, script, *args):
        return subprocess.run(
            [sys.executable, str(self.source / script), *map(str, args)],
            cwd=self.source,
            capture_output=True,
            text=True,
            check=False,
        )

    def _install_and_stamp(self):
        completed = self._run("install.py", "claude-code", "--root", self.root)
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        manifest = self.root / "delegate-triage-package-manifest.json"
        self.assertTrue(manifest.is_file(), "install must emit the package manifest")
        digest = __import__("hashlib").sha256(manifest.read_bytes()).hexdigest()
        source_commit = json.loads(manifest.read_text(encoding="utf-8"))["source_commit"]
        with (self.source / "agents/MANIFEST.md").open("a", encoding="utf-8") as handle:
            handle.write(
                "\n<!-- claude-package-manifest:v1 "
                f"sha256={digest} source_commit={source_commit} -->\n"
            )
        return manifest

    def test_clean_install_and_all_documented_integrity_commands_pass(self):
        manifest = self._install_and_stamp()

        state = self._run(
            "check_state.py",
            self.root / "skills/delegate-triage/STATE.md",
        )
        deployment = self._run(
            "check_wids.py",
            "--scope",
            "deployment",
            "--manifest",
            manifest,
            self.root,
        )
        installer_check = self._run(
            "install.py",
            "claude-code",
            "--root",
            self.root,
            "--check",
        )

        self.assertEqual(0, state.returncode, state.stdout + state.stderr)
        self.assertEqual(0, deployment.returncode, deployment.stdout + deployment.stderr)
        self.assertIn("13 SOURCE_ONLY", deployment.stdout)
        self.assertEqual(0, installer_check.returncode, installer_check.stdout + installer_check.stderr)

    def test_check_refuses_mutated_agent_delegation_skill_or_manifest(self):
        manifest = self._install_and_stamp()
        targets = [
            self.root / "agents/reviewer.md",
            self.root / "delegation.md",
            self.root / "skills/delegate-triage/SKILL.md",
            manifest,
        ]
        for target in targets:
            with self.subTest(target=target.relative_to(self.root)):
                original = target.read_bytes()
                try:
                    target.write_bytes(original + b"mutation\n")
                    completed = self._run(
                        "install.py",
                        "claude-code",
                        "--root",
                        self.root,
                        "--check",
                    )
                    self.assertNotEqual(0, completed.returncode)
                finally:
                    target.write_bytes(original)

    def test_behind_is_informational_when_stamped_installed_manifest_is_intact(self):
        self._install_and_stamp()
        skill = self.source / "SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8") + "\nnew canonical line\n", encoding="utf-8")
        self._git("add", "SKILL.md", "agents/MANIFEST.md")
        self._git("commit", "-qm", "advance canonical source")

        completed = self._run(
            "install.py",
            "claude-code",
            "--root",
            self.root,
            "--check",
        )

        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("BEHIND", completed.stdout)

    def test_dirty_source_refuses_dry_run_and_install_before_writes(self):
        (self.source / "untracked.txt").write_text("dirty\n", encoding="utf-8")
        for extra_args in (("--dry-run",), ()):
            with self.subTest(extra_args=extra_args):
                target = self.base / ("dry-root" if extra_args else "write-root")
                completed = self._run(
                    "install.py",
                    "claude-code",
                    "--root",
                    target,
                    *extra_args,
                )
                self.assertNotEqual(0, completed.returncode)
                self.assertIn("release deployment refused", completed.stdout)
                self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
