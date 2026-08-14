# DelegateOps Decision and Outcome Record Surfaces: Schema Inventory

**Export Commit**: `ac1635e945d1132754f7ac9d0716c5e795bfa608` ([EXPORTED_AT_COMMIT.txt:1](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/EXPORTED_AT_COMMIT.txt#L1))

---

## 1. Field Inventory of Decision & Outcome Record Surfaces

Classification legend:
* **CODE**: Enum, UUID/identifier, numerical metric, timestamp, boolean, content hash (safe for privacy-stripped export).
* **CONTENT**: Natural language text, free-form rationale, prompt, locator/filesystem path, unstructured payload dictionary, user identifier, arbitrary vendor extension (content-bearing / privacy-sensitive).

---

### 1.1 Decision Records & Associated Interfaces

#### `DecisionRecord`
*Source: [`packages/protocol/src/decision.ts:76-96`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L76-L96); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:667-859`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L667-L859)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Unique identifier for decision ([decision.ts:77](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L77)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Work unit being decided ([decision.ts:78](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L78)) |
| `planId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Governing plan version ID ([decision.ts:79](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L79)) |
| `supervisorSessionId` | `ExternalIdSchema` (string min 1) | No | **CODE** | Supervisor's session handle ([decision.ts:80](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L80)) |
| `policyVersion` | `string` (min 1) | No | **CODE** | Policy version string ([decision.ts:81](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L81)) |
| `candidates` | `ExecutionCandidate[]` | No | **CODE** (nested) | Array of evaluated execution candidates ([decision.ts:82](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L82)) |
| `choice` | `ExecutionChoice` | No | **CODE** (nested) | Committed routing choice ([decision.ts:83](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L83)) |
| `reasonCodes` | `ReasonCode[]` | No | **CODE** | Array of standardized reason code enums ([decision.ts:84](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L84)) |
| `rationale` | `string` | Yes | **CONTENT** | Free-form natural language decision rationale ([decision.ts:85](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L85)) |
| `authorityEnvelopeId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Governing authority envelope ID ([decision.ts:86](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L86)) |
| `resourceEnvelopeId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Governing resource envelope ID ([decision.ts:87](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L87)) |
| `verificationPlanId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Associated verification plan ID ([decision.ts:88](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L88)) |
| `contextSnapshotId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Pointer to context snapshot ID ([decision.ts:89](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L89)) |
| `committedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Decision commitment timestamp ([decision.ts:90](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L90)) |
| `treatmentMode` | `"prospective" \| "retrospective"` | No | **CODE** | Treatment mode enum ([decision.ts:91](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L91)) |
| `counterfactual` | `CounterfactualDisposition` | Yes | **CONTENT** (nested) | Counterfactual escalation record ([decision.ts:92](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L92)) |
| `contextPositionAtDecision` | `ContextPosition` | Yes | **CODE** (nested) | Context window usage metrics ([decision.ts:93](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L93)) |
| `consultations` | `ConsultationRecord[]` | Yes | **CONTENT** (nested) | Consultations informing decision ([decision.ts:94](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L94)) |

#### `CounterfactualDisposition`
*Source: [`packages/protocol/src/decision.ts:16-23`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L16-L23); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:695-738`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L695-L738)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `escalatedTo` | `"parent" \| "human"` | No | **CODE** | Escalation destination enum ([decision.ts:17](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L17)) |
| `wouldHaveDecided` | `string` (min 1) | No | **CONTENT** | Free-form explanation of intended decision ([decision.ts:18](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L18)) |
| `wouldHaveChosenCandidateId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Candidate that would have been chosen ([decision.ts:19](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L19)) |
| `recordedBeforeAnswer` | `boolean` | No | **CODE** | Truth flag if captured before escalation answer ([decision.ts:20](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L20)) |
| `recordedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Disposition record timestamp ([decision.ts:21](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L21)) |

#### `ContextPosition`
*Source: [`packages/protocol/src/decision.ts:32-38`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L32-L38); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:673-694`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L673-L694)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `tokensUsed` | `number` (integer >= 0) | No | **CODE** | Measured tokens used ([decision.ts:33](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L33)) |
| `contextWindowTokens` | `number` (integer > 0) | Yes | **CODE** | Total context window size ([decision.ts:34](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L34)) |
| `source` | `"harness_reported" \| "estimated"` | No | **CODE** | Measurement source classification ([decision.ts:35](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L35)) |
| `observedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Observation timestamp ([decision.ts:36](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L36)) |

#### `ConsultationRecord`
*Source: [`packages/protocol/src/decision.ts:49-62`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L49-L62); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:595-666`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L595-L666)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Consultation identifier ([decision.ts:50](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L50)) |
| `decisionId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Associated decision ID ([decision.ts:51](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L51)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Associated work unit ID ([decision.ts:52](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L52)) |
| `question` | `string` (min 1) | No | **CONTENT** | Free-form consultation prompt/question ([decision.ts:53](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L53)) |
| `candidates` | `ExecutionCandidate[]` | No | **CODE** (nested) | Advisor candidate menu ([decision.ts:54](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L54)) |
| `choice` | `ExecutionChoice` | Yes | **CODE** (nested) | Advisor execution choice ([decision.ts:55](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L55)) |
| `attemptId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Associated attempt ID ([decision.ts:56](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L56)) |
| `charterDigest` | `string` (min 1) | Yes | **CODE** | Digest hash of charter read by advisor ([decision.ts:57](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L57)) |
| `outcome` | `"followed" \| "partly_followed" \| "not_followed" \| "no_answer" \| "unrecorded"` | No | **CODE** | Consultation outcome enum ([decision.ts:58](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L58)) |
| `requestedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Request timestamp ([decision.ts:59](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L59)) |
| `answeredAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | Answer timestamp ([decision.ts:60](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L60)) |

#### `PolicyDecision` (Discriminated Union on `randomized`)
*Source: [`packages/protocol/src/decision.ts:104-124`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L104-L124); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:2138-2244`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L2138-L2244)*

*Branch 1: `randomized: false` (Deterministic Policy)*:
| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Policy decision record ID ([decision.ts:106](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L106)) |
| `decisionId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Associated decision ID ([decision.ts:107](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L107)) |
| `policyVersion` | `string` (min 1) | No | **CODE** | Policy version identifier ([decision.ts:108](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L108)) |
| `candidateIds` | `IdSchema[]` | No | **CODE** | Candidate IDs considered ([decision.ts:109](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L109)) |
| `randomized` | `literal(false)` | No | **CODE** | Discriminator flag ([decision.ts:110](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L110)) |
| `assignedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Policy assignment timestamp ([decision.ts:111](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L111)) |

*Branch 2: `randomized: true` (Randomized Experiment Assignment)*:
| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Policy decision record ID ([decision.ts:114](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L114)) |
| `decisionId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Associated decision ID ([decision.ts:115](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L115)) |
| `policyVersion` | `string` (min 1) | No | **CODE** | Policy version identifier ([decision.ts:116](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L116)) |
| `candidateIds` | `IdSchema[]` | No | **CODE** | Candidate IDs considered ([decision.ts:117](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L117)) |
| `randomized` | `literal(true)` | No | **CODE** | Discriminator flag ([decision.ts:118](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L118)) |
| `assignmentProbability` | `number` (0 < p <= 1) | No | **CODE** | Exact assignment propensity ([decision.ts:119](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L119)) |
| `arm` | `string` (min 1) | No | **CODE** | Assigned experiment arm name ([decision.ts:120](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L120)) |
| `assignedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Policy assignment timestamp ([decision.ts:121](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L121)) |

#### `ExecutionCandidate`
*Source: [`packages/protocol/src/execution.ts:124-131`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L124-L131); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:1015-1075`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L1015-L1075)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Candidate ID ([execution.ts:125](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L125)) |
| `recipe` | `ExecutionRecipe` | No | **CODE/CONTENT** (nested) | Execution recipe spec ([execution.ts:126](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L126)) |
| `eligibility` | `"eligible" \| "rejected"` | No | **CODE** | Candidate eligibility status ([execution.ts:127](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L127)) |
| `reasonCodes` | `ReasonCode[]` | No | **CODE** | Why candidate was ranked or rejected ([execution.ts:128](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L128)) |
| `rank` | `number` (integer >= 0) | Yes | **CODE** | Numerical ranking order ([execution.ts:129](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L129)) |

#### `ExecutionChoice` (Discriminated Union on `kind`)
*Source: [`packages/protocol/src/execution.ts:139-151`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L139-L151); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:1076-1193`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L1076-L1193)*

*Branch 1: `kind: "INLINE"`*:
| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `kind` | `literal("INLINE")` | No | **CODE** | Discriminator for inline execution ([execution.ts:141](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L141)) |
| `candidateId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Selected candidate ID ([execution.ts:142](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L142)) |
| `recipe` | `ClaudeInlineRecipeSchema` | No | **CODE/CONTENT** (nested) | Fixed `claude.inline` recipe ([execution.ts:143](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L143)) |

*Branch 2: `kind: "DELEGATED"`*:
| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `kind` | `literal("DELEGATED")` | No | **CODE** | Discriminator for delegated execution ([execution.ts:146](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L146)) |
| `candidateId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Selected candidate ID ([execution.ts:147](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L147)) |
| `recipe` | `ExecutionRecipe` | No | **CODE/CONTENT** (nested) | Chosen execution recipe ([execution.ts:148](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L148)) |

#### `ExecutionRecipe` (Common & Surface Variants)
*Source: [`packages/protocol/src/execution.ts:74-122`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L74-L122); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:1194-1890`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L1194-L1890)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Recipe ID ([execution.ts:75](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L75)) |
| `surface` | `SurfaceKind` enum | No | **CODE** | Execution surface kind discriminator ([execution.ts:89, 105](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L89)) |
| `model` | `string` (min 1) | Optional (Required on `antigravity.headless`) | **CODE** | Model lineage / identifier ([execution.ts:90, 106](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L90)) |
| `effort` | `string` (min 1) | Yes | **CODE** | Reasoning/thinking effort level ([execution.ts:76](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L76)) |
| `authDomain` | `string` (min 1) | No | **CODE** | Auth domain partition tag ([execution.ts:77](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L77)) |
| `permissionMode` | `string` (min 1) | Yes | **CODE** | Permission mode identifier ([execution.ts:78](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L78)) |
| `toolProfile` | `string` (min 1) | Yes | **CODE** | Tool profile identifier ([execution.ts:79](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L79)) |
| `contextMode` | `"shared" \| "fresh" \| "resumed" \| "unknown"` | No | **CODE** | Context boundary mode enum ([execution.ts:80](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L80)) |
| `configurationHash` | `string` (min 1) | No | **CODE** | Hash of surface configuration ([execution.ts:81](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L81)) |
| `capabilitySnapshotId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Capability probe snapshot ID ([execution.ts:82](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L82)) |
| `vendorExtensions` | `Record<string, unknown>` | No | **CONTENT** | Surface-specific extension attributes ([execution.ts:83](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L83)) |

---

### 1.2 Outcome, Execution, Adjudication, Rework & Cost Records

#### `Attempt`
*Source: [`packages/protocol/src/execution.ts:182-196`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L182-L196); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:144-224`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L144-L224)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Attempt identifier ([execution.ts:183](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L183)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Work unit being executed ([execution.ts:184](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L184)) |
| `decisionId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Authorizing decision ID ([execution.ts:185](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L185)) |
| `attemptNumber` | `number` (integer >= 1) | No | **CODE** | Monotonic attempt index ([execution.ts:186](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L186)) |
| `status` | `AttemptStatus` enum | No | **CODE** | Attempt lifecycle status ([execution.ts:187](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L187)) |
| `startedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Attempt start timestamp ([execution.ts:188](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L188)) |
| `endedAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | Attempt end timestamp ([execution.ts:189](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L189)) |
| `sourceSessionId` | `ExternalIdSchema` (string min 1) | Yes | **CODE** | Native surface session ID ([execution.ts:190](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L190)) |
| `exitCode` | `number` (integer) | Yes | **CODE** | Process exit code ([execution.ts:191](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L191)) |
| `stopRequestedAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | Timestamp stop was requested ([execution.ts:192](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L192)) |
| `cessationObservedAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | Timestamp process cessation observed ([execution.ts:193](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L193)) |
| `externalEffectReconciledAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | Timestamp side-effects reconciled ([execution.ts:194](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L194)) |

#### `Claim`
*Source: [`packages/protocol/src/evidence.ts:19-28`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L19-L28); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:538-594`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L538-L594)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Claim ID ([evidence.ts:20](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L20)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Work unit claimed complete ([evidence.ts:21](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L21)) |
| `attemptId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Attempt generating claim ([evidence.ts:22](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L22)) |
| `statement` | `string` (min 1) | No | **CONTENT** | Free-form completion statement ([evidence.ts:23](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L23)) |
| `madeBy` | `"worker" \| "orchestrator" \| "human"` | No | **CODE** | Claim maker role enum ([evidence.ts:24](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L24)) |
| `submittedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Claim submission timestamp ([evidence.ts:25](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L25)) |
| `evidenceIds` | `IdSchema[]` | No | **CODE** | Array of supporting evidence IDs ([evidence.ts:26](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L26)) |

#### `Evidence`
*Source: [`packages/protocol/src/evidence.ts:30-46`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L30-L46); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:949-1014`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L949-L1014)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Evidence ID ([evidence.ts:31](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L31)) |
| `claimId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Associated claim ID ([evidence.ts:32](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L32)) |
| `kind` | `"command_result" \| "artifact" \| "human_attestation" \| "agent_verification" \| "event_trace"` | No | **CODE** | Evidence kind enum ([evidence.ts:33-39](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L33-L39)) |
| `producedBy` | `"command" \| "adapter" \| "agent" \| "human"` | No | **CODE** | Producer type enum ([evidence.ts:40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L40)) |
| `collectedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Collection timestamp ([evidence.ts:41](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L41)) |
| `artifactRefs` | `IdSchema[]` | No | **CODE** | Array of artifact reference IDs ([evidence.ts:42](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L42)) |
| `summary` | `string` (min 1) | No | **CONTENT** | Free-form textual evidence summary ([evidence.ts:43](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L43)) |
| `contentHash` | `string` (min 1) | Yes | **CODE** | Cryptographic content hash ([evidence.ts:44](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L44)) |

#### `ArtifactReference`
*Source: [`packages/protocol/src/evidence.ts:5-12`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L5-L12); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:102-143`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L102-L143)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Artifact reference ID ([evidence.ts:6](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L6)) |
| `kind` | `"file" \| "directory" \| "url" \| "commit" \| "opaque"` | No | **CODE** | Artifact kind enum ([evidence.ts:7](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L7)) |
| `locator` | `string` (min 1) | No | **CONTENT** | Path, URL, commit hash, or URI ([evidence.ts:8](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L8)) |
| `contentHash` | `string` (min 1) | Yes | **CODE** | Content hash ([evidence.ts:9](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L9)) |
| `observedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Observation timestamp ([evidence.ts:10](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L10)) |

#### `VerificationObligation`
*Source: [`packages/protocol/src/evidence.ts:49-55`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L49-L55); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:2770-2807`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L2770-L2807)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Obligation identifier ([evidence.ts:50](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L50)) |
| `kind` | `VerificationMethod` enum (`"command" \| "artifact" \| "human" \| "agent"`) | No | **CODE** | Verification method enum ([evidence.ts:51](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L51)) |
| `spec` | `Record<string, unknown>` | No | **CONTENT** | Verification test spec, script, commands ([evidence.ts:52](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L52)) |
| `blocking` | `boolean` | No | **CODE** | Whether failure blocks acceptance ([evidence.ts:53](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L53)) |

#### `VerificationPlan`
*Source: [`packages/protocol/src/evidence.ts:62-70`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L62-L70); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:2808-2856`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L2808-L2856)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Verification plan ID ([evidence.ts:63](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L63)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Associated work unit ID ([evidence.ts:64](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L64)) |
| `obligations` | `VerificationObligation[]` | No | **CONTENT** (nested) | Typed obligations list ([evidence.ts:65](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L65)) |
| `reserveEnvelopeId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Protected reserve envelope ID ([evidence.ts:66](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L66)) |
| `independenceRequirement` | `"none" \| "independent_agent" \| "human"` | No | **CODE** | Independence requirement enum ([evidence.ts:67](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L67)) |
| `createdAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Verification plan creation timestamp ([evidence.ts:68](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L68)) |

#### `Adjudication`
*Source: [`packages/protocol/src/evidence.ts:72-82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L72-L82); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:38-101`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L38-L101)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Adjudication record ID ([evidence.ts:73](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L73)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Work unit adjudicated ([evidence.ts:74](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L74)) |
| `claimIds` | `IdSchema[]` | No | **CODE** | Claims being evaluated ([evidence.ts:75](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L75)) |
| `verdict` | `"VERIFIED" \| "REJECTED" \| "NEEDS_EVIDENCE" \| "UNKNOWN"` | No | **CODE** | Final verification verdict enum ([evidence.ts:76](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L76)) |
| `adjudicatedBy` | `"human" \| "agent" \| "command"` | No | **CODE** | Adjudicator class enum ([evidence.ts:77](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L77)) |
| `rationale` | `string` | Yes | **CONTENT** | Free-form adjudication rationale text ([evidence.ts:78](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L78)) |
| `blind` | `boolean` | No | **CODE** | Blind adjudication flag ([evidence.ts:79](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L79)) |
| `adjudicatedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Adjudication timestamp ([evidence.ts:80](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L80)) |

#### `DeviationRecord`
*Source: [`packages/protocol/src/plan.ts:60-78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L60-L78); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:860-948`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L860-L948)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Deviation record ID ([plan.ts:61](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L61)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Work unit where deviation occurred ([plan.ts:62](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L62)) |
| `attemptId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Attempt where deviation occurred ([plan.ts:63](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L63)) |
| `planId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Governing plan version ID ([plan.ts:64](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L64)) |
| `category` | `"execution_method" \| "resource_consumption" \| "tool_use" \| "schedule" \| "trace_gap" \| "worker_substitution"` | No | **CODE** | Deviation category enum ([plan.ts:65-72](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L65-L72)) |
| `description` | `string` (min 1) | No | **CONTENT** | Free-form deviation description ([plan.ts:73](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L73)) |
| `detectedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Detection timestamp ([plan.ts:74](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L74)) |
| `recordedBy` | `"orchestrator" \| "worker" \| "human" \| "adapter"` | No | **CODE** | Observer role enum ([plan.ts:75](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L75)) |
| `anticipatedBy` | `AnticipationLink` | Yes | **CODE** (nested) | Charter prediction link ([plan.ts:76](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L76)) |

#### `AnticipationLink`
*Source: [`packages/protocol/src/plan.ts:49-54`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L49-L54); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:866-886`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L866-L886)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `charterEntryId` | `string` (min 1) | No | **CODE** | Charter entry ID ([plan.ts:50](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L50)) |
| `charterVersion` | `string` (min 1) | No | **CODE** | Charter version identifier ([plan.ts:51](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L51)) |
| `charterDigest` | `string` (min 1) | Yes | **CODE** | Charter digest hash ([plan.ts:52](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L52)) |

#### `ReplanRecord`
*Source: [`packages/protocol/src/plan.ts:119-130`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L119-L130); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:2487-2567`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L2487-L2567)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Replan record ID ([plan.ts:120](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L120)) |
| `objectiveId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Root objective ID ([plan.ts:121](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L121)) |
| `fromPlanId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Predecessor plan version ID ([plan.ts:122](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L122)) |
| `toPlanId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Successor plan version ID ([plan.ts:123](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L123)) |
| `triggers` | `ReplanTrigger[]` (min 1) | No | **CODE** | Array of standard replan triggers ([plan.ts:124](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L124)) |
| `rationale` | `string` (min 1) | No | **CONTENT** | Free-form explanation for replan ([plan.ts:125](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L125)) |
| `authorizedBy` | `"root_supervisor" \| "human"` | No | **CODE** | Authorizer authority enum ([plan.ts:126](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L126)) |
| `origin` | `"material" \| "inline_admission"` | No (defaults to `"material"`) | **CODE** | Origin classification enum ([plan.ts:127](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L127)) |
| `committedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Replan commitment timestamp ([plan.ts:128](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L128)) |

#### `ResourceGrant`
*Source: [`packages/protocol/src/resources.ts:38-63`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L38-L63); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:2608-2669`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L2608-L2669)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `dimension` | `ResourceDimension` enum | No | **CODE** | Non-fungible resource dimension enum ([resources.ts:40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L40)) |
| `governance` | `ResourceGovernance` enum | No | **CODE** | Enforcement class enum ([resources.ts:41](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L41)) |
| `target` | `number` (finite >= 0) | Yes | **CODE** | Advisory budget target ([resources.ts:42](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L42)) |
| `hard` | `number` (finite >= 0) | Yes | **CODE** | Enforceable hard ceiling ([resources.ts:43](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L43)) |
| `reserve` | `number` (finite >= 0) | Yes | **CODE** | Protected verification reserve ([resources.ts:44](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L44)) |
| `unit` | `string` (min 1) | No | **CODE** | Unit label (e.g., `USD`, `tokens`, `ms`) ([resources.ts:45](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L45)) |
| `confidence` | `"exact" \| "estimated" \| "observed" \| "unknown"` | No | **CODE** | Measurement confidence enum ([resources.ts:46](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L46)) |

#### `ResourceEnvelope`
*Source: [`packages/protocol/src/resources.ts:80-95`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L80-L95); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:2568-2607`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L2568-L2607)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | Envelope ID ([resources.ts:82](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L82)) |
| `parentEnvelopeId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | Parent resource envelope ID ([resources.ts:83](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L83)) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | Associated work unit ID ([resources.ts:84](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L84)) |
| `grants` | `ResourceGrant[]` | No | **CODE** (nested) | Array of dimension grants ([resources.ts:85](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L85)) |
| `createdAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | Envelope creation timestamp ([resources.ts:86](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L86)) |

#### `ReserveRelease` (Interface)
*Source: [`packages/protocol/src/resources.ts:270-278`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L270-L278)*

| Field Name | Type | Optional | Classification | Description / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `newEnvelopeId` | `string` (UUIDv7 string) | No | **CODE** | Minted successor envelope ID ([resources.ts:272](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L272)) |
| `dimension` | `ResourceDimension` enum | No | **CODE** | Dimension being released ([resources.ts:273](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L273)) |
| `amount` | `number` | No | **CODE** | Released reserve amount ([resources.ts:274](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L274)) |
| `authorizedByReplanId` | `string` (UUIDv7 string) | No | **CODE** | Authorizing replan record ID ([resources.ts:276](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L276)) |
| `releasedAt` | `string` (UTC ISO-8601) | No | **CODE** | Release timestamp ([resources.ts:277](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L277)) |

---

## 2. Verbatim Enum Vocabularies

### 2.1 Disposition & Outcome-Like Enums
* **`WorkUnitStatus`** ([`packages/protocol/src/execution.ts:154-163`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L154-L163)):
  ```typescript
  "PLANNED",
  "DECIDED",
  "EXECUTING",
  "SUBMITTED",
  "VERIFIED",
  "REJECTED",
  "NEEDS_EVIDENCE",
  "UNKNOWN"
  ```
* **`AttemptStatus`** ([`packages/protocol/src/execution.ts:166-173`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L166-L173)):
  ```typescript
  "STARTED",
  "RUNNING",
  "SUBMITTED",
  "HALT_REQUESTED",
  "ABANDONED",
  "FAILED"
  ```
* **`AdjudicationVerdict` (`AdjudicationSchema.verdict`)** ([`packages/protocol/src/evidence.ts:76`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L76)):
  ```typescript
  "VERIFIED",
  "REJECTED",
  "NEEDS_EVIDENCE",
  "UNKNOWN"
  ```
* **`AdjudicationAdjudicator` (`AdjudicationSchema.adjudicatedBy`)** ([`packages/protocol/src/evidence.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L77)):
  ```typescript
  "human",
  "agent",
  "command"
  ```
* **`ConsultationOutcome` (`ConsultationRecordSchema.outcome`)** ([`packages/protocol/src/decision.ts:58`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L58)):
  ```typescript
  "followed",
  "partly_followed",
  "not_followed",
  "no_answer",
  "unrecorded"
  ```
* **`TreatmentMode` (`DecisionRecordSchema.treatmentMode`)** ([`packages/protocol/src/decision.ts:91`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L91)):
  ```typescript
  "prospective",
  "retrospective"
  ```
* **`CounterfactualEscalatedTo` (`CounterfactualDispositionSchema.escalatedTo`)** ([`packages/protocol/src/decision.ts:17`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L17)):
  ```typescript
  "parent",
  "human"
  ```
* **`CandidateEligibility` (`ExecutionCandidateSchema.eligibility`)** ([`packages/protocol/src/execution.ts:127`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L127)):
  ```typescript
  "eligible",
  "rejected"
  ```
* **`ClaimMadeBy` (`ClaimSchema.madeBy`)** ([`packages/protocol/src/evidence.ts:24`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L24)):
  ```typescript
  "worker",
  "orchestrator",
  "human"
  ```
* **`EvidenceKind` (`EvidenceSchema.kind`)** ([`packages/protocol/src/evidence.ts:33-39`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L33-L39)):
  ```typescript
  "command_result",
  "artifact",
  "human_attestation",
  "agent_verification",
  "event_trace"
  ```
* **`EvidenceProducedBy` (`EvidenceSchema.producedBy`)** ([`packages/protocol/src/evidence.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L40)):
  ```typescript
  "command",
  "adapter",
  "agent",
  "human"
  ```
* **`ArtifactReferenceKind` (`ArtifactReferenceSchema.kind`)** ([`packages/protocol/src/evidence.ts:7`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L7)):
  ```typescript
  "file",
  "directory",
  "url",
  "commit",
  "opaque"
  ```
* **`DeviationCategory` (`DeviationRecordSchema.category`)** ([`packages/protocol/src/plan.ts:65-72`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L65-L72)):
  ```typescript
  "execution_method",
  "resource_consumption",
  "tool_use",
  "schedule",
  "trace_gap",
  "worker_substitution"
  ```
* **`DeviationRecordedBy` (`DeviationRecordSchema.recordedBy`)** ([`packages/protocol/src/plan.ts:75`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L75)):
  ```typescript
  "orchestrator",
  "worker",
  "human",
  "adapter"
  ```
* **`ReplanAuthorizer` (`ReplanRecordSchema.authorizedBy`)** ([`packages/protocol/src/plan.ts:126`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L126)):
  ```typescript
  "root_supervisor",
  "human"
  ```
* **`ReplanOrigin` (`REPLAN_ORIGINS` / `ReplanOriginSchema`)** ([`packages/protocol/src/plan.ts:115-116`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L115-L116)):
  ```typescript
  "material",
  "inline_admission"
  ```
* **`TraceHealthStatus` (`TraceHealthStatusSchema`)** ([`packages/protocol/src/events.ts:98-104`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L98-L104)):
  ```typescript
  "HEALTHY",
  "PARTIAL",
  "DEGRADED",
  "UNTRUSTWORTHY",
  "UNKNOWN"
  ```
* **`TraceHealthScope` (`TraceHealthSchema.scope`)** ([`packages/protocol/src/events.ts:114`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L114)):
  ```typescript
  "attempt",
  "work_unit",
  "plan"
  ```
* **`RawEventParseStatus` (`RawEventEnvelopeSchema.parseStatus`)** ([`packages/protocol/src/events.ts:47`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L47)):
  ```typescript
  "parsed",
  "partial",
  "unparsed",
  "invalid"
  ```
* **`RetentionClass` (`RetentionClassSchema`)** ([`packages/protocol/src/events.ts:13-18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L13-L18)):
  ```typescript
  "transient",
  "operational",
  "sensitive",
  "unclassified"
  ```

---

### 2.2 Candidate, Recipe & Surface Kinds
* **`SURFACE_KINDS` (`SurfaceKindSchema`)** ([`packages/protocol/src/execution.ts:11-22`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L11-L22)):
  ```typescript
  "claude.inline",
  "claude.subagent",
  "claude.workflow",
  "claude.agent_team",
  "claude.headless",
  "claude.headless_bare",
  "antigravity.headless",
  "codex.app_server",
  "codex.cli",
  "api.deepseek"
  ```
* **`ExecutionChoiceKind` (`ExecutionChoiceSchema` Discriminator)** ([`packages/protocol/src/execution.ts:141, 146`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L141)):
  ```typescript
  "INLINE",
  "DELEGATED"
  ```
* **`ContextMode` (`ContextModeSchema`)** ([`packages/protocol/src/execution.ts:71`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L71)):
  ```typescript
  "shared",
  "fresh",
  "resumed",
  "unknown"
  ```

---

### 2.3 Reason Codes & Replan Triggers
* **`REASON_CODES` (`ReasonCodeSchema`)** ([`packages/protocol/src/execution.ts:46-66`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L46-L66)):
  ```typescript
  "AUTHORITY_LIMIT",
  "CACHE_WARMTH",
  "CAPABILITY_UNSUPPORTED",
  "CODE_SPECIALIZATION",
  "CONTEXT_ISOLATION",
  "COST_POLICY",
  "CRITICAL_PATH",
  "EXPERIMENT_ASSIGNMENT",
  "HARD_REQUIREMENT_UNMET",
  "MODEL_DIVERSIFICATION",
  "PARALLEL_INDEPENDENT",
  "PARENT_STEERING_REQUIRED",
  "PEER_COMMUNICATION",
  "PROVIDER_CAPACITY",
  "PROVIDER_DISABLED",
  "ROOT_OVERRIDE",
  "STABLE_TOPOLOGY",
  "TIGHT_COUPLING",
  "VERIFICATION_INDEPENDENCE"
  ```
* **`REPLAN_TRIGGERS` (`ReplanTriggerSchema`)** ([`packages/protocol/src/plan.ts:81-92`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L81-L92)):
  ```typescript
  "critical_path_changed",
  "deliverable_or_acceptance_changed",
  "dependency_edges_changed",
  "hard_ceiling_or_reserve_changed",
  "parent_authority_changed",
  "sub_orchestrator_created",
  "surface_or_model_family_changed",
  "target_grant_changed_over_25_percent",
  "verification_method_changed",
  "work_unit_set_changed"
  ```
* **`PROTOCOL_INVARIANT_CODES`** ([`packages/protocol/src/errors.ts:6-28`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/errors.ts#L6-L28)):
  ```typescript
  "AUTHORITY_DEPTH_NOT_DECREASING",
  "AUTHORITY_DESCENDANTS_EXCEED_PARENT",
  "AUTHORITY_EXPIRY_EXTENDED",
  "AUTHORITY_MODEL_ESCALATION",
  "AUTHORITY_RIGHT_ESCALATION",
  "AUTHORITY_SURFACE_ESCALATION",
  "AUTHORITY_TOOL_DENIAL_RELAXED",
  "DUPLICATE_WORK_UNIT",
  "ENVELOPE_PARENT_MISMATCH",
  "GOVERNANCE_ESCALATION",
  "GRANT_EXCEEDS_PARENT",
  "MISSING_WORK_UNIT",
  "PLAN_CYCLE",
  "RESERVE_NOT_RELEASED",
  "RESERVE_RELEASE_EXCEEDS_RESERVE",
  "RESERVE_RELEASE_UNAUTHORIZED",
  "RETROSPECTIVE_DECISION",
  "STRATUM_MISMATCH",
  "UNGRANTED_DIMENSION",
  "UNKNOWN_DEPENDENCY",
  "WORK_UNIT_NOT_IN_PLAN"
  ```

---

### 2.4 Verification Outcomes, Methods & Independence
* **`VerificationMethod` (`VerificationMethodSchema`)** ([`packages/protocol/src/objective.ts:4`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/objective.ts#L4)):
  ```typescript
  "command",
  "artifact",
  "human",
  "agent"
  ```
* **`IndependenceRequirement` (`VerificationPlanSchema.independenceRequirement`)** ([`packages/protocol/src/evidence.ts:67`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L67)):
  ```typescript
  "none",
  "independent_agent",
  "human"
  ```

---

### 2.5 Policy & Experiment Types
* **`PolicyDecision` (`PolicyDecisionSchema` Discriminated Union)** ([`packages/protocol/src/decision.ts:104-123`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L104-L123)):
  * `randomized: false` (Deterministic policy assignment):
    * `id: IdSchema`
    * `decisionId: IdSchema`
    * `policyVersion: string`
    * `candidateIds: IdSchema[]`
    * `randomized: literal(false)`
    * `assignedAt: TimestampSchema`
  * `randomized: true` (Randomized experiment arm):
    * `id: IdSchema`
    * `decisionId: IdSchema`
    * `policyVersion: string`
    * `candidateIds: IdSchema[]`
    * `randomized: literal(true)`
    * `assignmentProbability: number (0 < p <= 1)`
    * `arm: string`
    * `assignedAt: TimestampSchema`
* **Experiment Reason Code**: `"EXPERIMENT_ASSIGNMENT"` in `REASON_CODES` ([`packages/protocol/src/execution.ts:54`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L54))

---

### 2.6 Additional Protocol Vocabularies
* **`OrchestratorRole` (`ORCHESTRATOR_ROLES` / `OrchestratorRoleSchema`)** ([`packages/protocol/src/authority.ts:6-14`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L6-L14)):
  ```typescript
  "ROOT_SUPERVISOR",
  "SUB_ORCHESTRATOR",
  "ADAPTIVE_WORKER",
  "LEAF"
  ```
* **`SupportLevel` (`SUPPORT_LEVELS` / `SupportLevelSchema`)** ([`packages/protocol/src/capability.ts:11-21`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L11-L21)):
  ```typescript
  "enforced",
  "supported",
  "best_effort",
  "observed_only",
  "unsupported",
  "unknown"
  ```
* **`ResourceGovernance` (`RESOURCE_GOVERNANCE` / `ResourceGovernanceSchema`)** ([`packages/protocol/src/resources.ts:10-18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L10-L18)):
  ```typescript
  "hard_delegateops",
  "hard_surface",
  "soft_observed",
  "opaque_external"
  ```
* **`ResourceDimension` (`RESOURCE_DIMENSIONS` / `ResourceDimensionSchema`)** ([`packages/protocol/src/resources.ts:21-34`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L21-L34)):
  ```typescript
  "api_usd",
  "input_tokens",
  "output_tokens",
  "wall_clock_ms",
  "attempts",
  "children",
  "concurrency",
  "provider_quota_estimate",
  "human_review_minutes"
  ```
* **`AuthStatus` (`AuthStatusSchema`)** ([`packages/protocol/src/provider-state.ts:11-18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L11-L18)):
  ```typescript
  "authenticated_subscription",
  "authenticated_api",
  "unauthenticated",
  "expired",
  "unknown"
  ```
* **`QuotaPressure` (`QuotaPressureSchema`)** ([`packages/protocol/src/provider-state.ts:25-33`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L25-L33)):
  ```typescript
  "plentiful",
  "normal",
  "constrained",
  "nearly_exhausted",
  "exhausted",
  "unknown"
  ```
* **`NORMALIZED_EVENT_NAMES` (`NormalizedEventNameSchema`)** ([`packages/protocol/src/events.ts:55-78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L55-L78)):
  ```typescript
  "objective_created",
  "plan_committed",
  "decision_committed",
  "attempt_started",
  "attempt_progress",
  "usage_observed",
  "budget_soft_crossed",
  "budget_hard_crossed",
  "artifact_produced",
  "claim_submitted",
  "deviation_recorded",
  "replan_committed",
  "halt_requested",
  "cessation_observed",
  "verification_started",
  "verification_completed",
  "adjudication_recorded",
  "human_intervention",
  "provider_state_changed",
  "trace_gap_detected"
  ```

---

## 3. Fields Presupposing a SINGLE Decision-Maker or Single Root

The following fields enforce a single hierarchical authority, single root supervisor, single session, or singular root structure with no multi-writer / multi-agent consensus affordances:

1. **`supervisorSessionId: ExternalIdSchema`**
   * File & Line: [`packages/protocol/src/decision.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L80)
   * Singular supervisor session minting the decision: *"candidates is the menu the supervisor actually had... committed before activation"* ([decision.ts:65-66](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L65-L66)).
2. **`choice: ExecutionChoiceSchema`**
   * File & Line: [`packages/protocol/src/decision.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L83)
   * Singular choice commit (`candidateId` + single `recipe`), admitting no split, committee, or weighted multi-choice.
3. **`authorityEnvelopeId: IdSchema`**
   * File & Line: [`packages/protocol/src/decision.ts:86`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L86)
   * Points to exactly one `AuthorityEnvelope` holding the delegation rights.
4. **`escalatedTo: z.enum(["parent", "human"])`**
   * File & Line: [`packages/protocol/src/decision.ts:17`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L17)
   * Binary choice between single immediate parent supervisor or a human.
5. **`authorizedBy: z.enum(["root_supervisor", "human"])`**
   * File & Line: [`packages/protocol/src/plan.ts:126`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L126)
   * Replan authorization restricted strictly to a singular `"root_supervisor"` or `"human"`.
6. **`parentWorkUnitId: IdSchema.optional()`**
   * File & Line: [`packages/protocol/src/plan.ts:29`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L29)
   * Strict single-parent tree structure for work decomposition.
7. **`parentPlanId: IdSchema.optional()`**
   * File & Line: [`packages/protocol/src/plan.ts:15`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L15)
   * Single linear ancestry for plan revisions (`previous.id` in `nextPlanVersion`, [plan.ts:300](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L300)).
8. **`parentEnvelopeId: IdSchema.optional()`**
   * File & Line: [`packages/protocol/src/resources.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L83)
   * Resource budgets drawn from a single parent envelope (`assertChildEnvelopeAllowed`, [resources.ts:187](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L187)).
9. **`owner: z.string().min(1)`**
   * File & Line: [`packages/protocol/src/objective.ts:26`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/objective.ts#L26)
   * Single objective owner (*"only the owner or a human-authorized root path may change acceptance"*, [objective.ts:19-20](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/objective.ts#L19-L20)).
10. **`role: OrchestratorRoleSchema`**
    * File & Line: [`packages/protocol/src/authority.ts:30`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L30)
    * Single hierarchical role assigned per work unit ([`ROOT_SUPERVISOR`, `SUB_ORCHESTRATOR`, `ADAPTIVE_WORKER`, `LEAF`]).
11. **`escalation: z.enum(["parent", "human"])`**
    * File & Line: [`packages/protocol/src/authority.ts:41`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L41)
    * Authority envelope escalation route targeting a single parent or human.
12. **`madeBy: z.enum(["worker", "orchestrator", "human"])`**
    * File & Line: [`packages/protocol/src/evidence.ts:24`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L24)
    * Single author for completion claim.
13. **`adjudicatedBy: z.enum(["human", "agent", "command"])`**
    * File & Line: [`packages/protocol/src/evidence.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L77)
    * Single adjudicator entity verifying the work.
14. **`ReasonCode` Single-Root Codes**:
    * `"PARENT_STEERING_REQUIRED"` ([`packages/protocol/src/execution.ts:58`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L58))
    * `"ROOT_OVERRIDE"` ([`packages/protocol/src/execution.ts:62`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L62))

---

## 4. Fields Recording SITUATION at Decision Time

### 4.1 Budgets & Resource Envelopes
* **`resourceEnvelopeId: IdSchema`** ([`packages/protocol/src/decision.ts:87`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L87)): Links decision to active resource envelope.
* **`ResourceEnvelope.grants: ResourceGrant[]`** ([`packages/protocol/src/resources.ts:85`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L85)):
  * `dimension: ResourceDimension` ([resources.ts:40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L40)) — 9 dimensions: `api_usd`, `input_tokens`, `output_tokens`, `wall_clock_ms`, `attempts`, `children`, `concurrency`, `provider_quota_estimate`, `human_review_minutes`.
  * `governance: ResourceGovernance` ([resources.ts:41](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L41)) — `hard_delegateops`, `hard_surface`, `soft_observed`, `opaque_external`.
  * `target: number` ([resources.ts:42](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L42)): Advisory budget.
  * `hard: number` ([resources.ts:43](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L43)): Hard spending ceiling.
  * `reserve: number` ([resources.ts:44](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L44)): Protected verification budget carved out of `hard`.
  * `unit: string` ([resources.ts:45](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L45)): Unit label.
  * `confidence: "exact" | "estimated" | "observed" | "unknown"` ([resources.ts:46](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L46)).
* **`VerificationPlan.reserveEnvelopeId: IdSchema.optional()`** ([`packages/protocol/src/evidence.ts:66`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L66)): Protected reserve allocation for verification.
* **Reason Codes**: `"COST_POLICY"` ([execution.ts:52](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L52)), `"AUTHORITY_LIMIT"` ([execution.ts:47](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L47)).

### 4.2 Provider & Capacity State
* **`ProviderStateSnapshot`** ([`packages/protocol/src/provider-state.ts:56-73`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L56-L73)):
  * `provider: string` ([provider-state.ts:58](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L58))
  * `surface: SurfaceKind` ([provider-state.ts:59](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L59))
  * `enabled: boolean` ([provider-state.ts:60](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L60))
  * `installedVersion: string.optional()` ([provider-state.ts:61](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L61))
  * `authDomain: string` ([provider-state.ts:62](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L62))
  * `authStatus: AuthStatus` ([provider-state.ts:63](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L63)) (`authenticated_subscription`, `authenticated_api`, `unauthenticated`, `expired`, `unknown`)
  * `availableModels: string[].optional()` ([provider-state.ts:64](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L64))
  * `quotaPressure: QuotaPressure` ([provider-state.ts:65](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L65)) (`plentiful`, `normal`, `constrained`, `nearly_exhausted`, `exhausted`, `unknown`)
  * `quotaSource: "user_supplied" | "machine_observed" | "unknown"` ([provider-state.ts:66](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L66))
  * `observedUsage: ObservedUsage.optional()` ([provider-state.ts:67](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L67)): `inputTokenCount`, `outputTokenCount`, `cacheReadTokenCount`, `cacheCreationTokenCount`, `windowResetAt` ([provider-state.ts:36-40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L36-L40)).
  * `concurrencyInUse: number` ([provider-state.ts:68](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L68))
  * `concurrencyLimit: number.optional()` ([provider-state.ts:69](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L69))
  * `recentErrors: AdapterError[]` ([provider-state.ts:70](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L70)): `occurredAt`, `code`, `summary`.
  * `capturedAt: TimestampSchema` ([provider-state.ts:71](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L71)).
* **`CapabilitySnapshot`** (linked via `ExecutionRecipe.capabilitySnapshotId`, [`packages/protocol/src/execution.ts:82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L82); defined in [`packages/protocol/src/capability.ts:23-44`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L23-L44)):
  * Feature Support Levels ([`capability.ts:29-40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L29-L40)): `launch`, `message`, `steer`, `requestStop`, `observeCessation`, `pauseResume`, `sessionResume`, `nestedDelegation`, `eventStream`, `tokenUsage`, `cacheUsage`, `hardBudget`.
  * `knownLimitations: string[]` ([capability.ts:41](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L41))
  * `rawProbe: Record<string, unknown>` ([capability.ts:42](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L42))
* **Reason Codes**: `"PROVIDER_CAPACITY"` ([execution.ts:60](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L60)), `"PROVIDER_DISABLED"` ([execution.ts:61](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L61)), `"CAPABILITY_UNSUPPORTED"` ([execution.ts:49](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L49)), `"CACHE_WARMTH"` ([execution.ts:48](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L48)).

### 4.3 Time Constraints & Expiries
* **`AuthorityEnvelope.expiresAt: TimestampSchema.optional()`** ([`packages/protocol/src/authority.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L40)): Expiry bounding authority validity window.
* **`ObservedUsage.windowResetAt: TimestampSchema.optional()`** ([`packages/protocol/src/provider-state.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L40)): Provider quota rate-limit reset boundary.
* **`ResourceGrant` dimension `"wall_clock_ms"`** ([`packages/protocol/src/resources.ts:25`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L25)): Execution wall clock time constraint.
* **`DecisionRecord.committedAt: TimestampSchema`** ([`packages/protocol/src/decision.ts:90`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L90)): Timestamp of prospective commitment.
* **Reason Code**: `"CRITICAL_PATH"` ([execution.ts:53](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L53)).

### 4.4 Context Snapshots & Agent State
* **`contextSnapshotId: IdSchema`** ([`packages/protocol/src/decision.ts:89`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L89)): Snapshot ID capturing context at decision time.
* **`contextPositionAtDecision: ContextPosition.optional()`** ([`packages/protocol/src/decision.ts:93`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L93)):
  * `tokensUsed: number` ([decision.ts:33](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L33))
  * `contextWindowTokens: number.optional()` ([decision.ts:34](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L34))
  * `source: "harness_reported" | "estimated"` ([decision.ts:35](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L35))
  * `observedAt: TimestampSchema` ([decision.ts:36](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L36))
* **`ExecutionRecipe.contextMode: ContextMode`** ([`packages/protocol/src/execution.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L80)): `"shared" | "fresh" | "resumed" | "unknown"`.
* **`ExecutionRecipe.toolProfile: string.optional()`** ([`packages/protocol/src/execution.ts:79`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L79)): Tool access profile available at decision time.
* **`ExecutionRecipe.configurationHash: string`** ([`packages/protocol/src/execution.ts:81`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L81)): Digest of tool, plugin, prompt configuration.
* **`counterfactual: CounterfactualDisposition.optional()`** ([`packages/protocol/src/decision.ts:92`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L92)): Prior disposition before supervisor steering / escalation.
* **
# DelegateOps Decision and Outcome Record Surfaces: Schema Inventory

**Export Commit**: `ac1635e945d1132754f7ac9d0716c5e795bfa608` ([EXPORTED_AT_COMMIT.txt:1](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/EXPORTED_AT_COMMIT.txt#L1))

---

## 1. Field Inventory: Decision & Outcome Records

Classification:
* **CODE**: Enum, UUIDv7 / external ID, number, timestamp, boolean, content hash (safe for privacy-stripped export).
* **CONTENT**: Free text, prompt, file/URL locator, open-ended payload dictionary, user identifier, vendor extensions.

### 1.1 Decision Records & Routing Choice

#### `DecisionRecord`
*Source: [`packages/protocol/src/decision.ts:76-96`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L76-L96); Schema: [`docs/schemas/delegateops-v0alpha1.schema.json:667-859`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json#L667-L859)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L77) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L78) |
| `planId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:79`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L79) |
| `supervisorSessionId` | `ExternalIdSchema` (string min 1) | No | **CODE** | [`decision.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L80) |
| `policyVersion` | `string` (min 1) | No | **CODE** | [`decision.ts:81`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L81) |
| `candidates` | `ExecutionCandidate[]` | No | **CODE** (nested) | [`decision.ts:82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L82) |
| `choice` | `ExecutionChoice` | No | **CODE** (nested) | [`decision.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L83) |
| `reasonCodes` | `ReasonCode[]` | No | **CODE** | [`decision.ts:84`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L84) |
| `rationale` | `string` | Yes | **CONTENT** | [`decision.ts:85`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L85) |
| `authorityEnvelopeId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:86`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L86) |
| `resourceEnvelopeId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:87`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L87) |
| `verificationPlanId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:88`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L88) |
| `contextSnapshotId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:89`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L89) |
| `committedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`decision.ts:90`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L90) |
| `treatmentMode` | `"prospective" \| "retrospective"` | No | **CODE** | [`decision.ts:91`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L91) |
| `counterfactual` | `CounterfactualDisposition` | Yes | **CONTENT** (nested) | [`decision.ts:92`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L92) |
| `contextPositionAtDecision` | `ContextPosition` | Yes | **CODE** (nested) | [`decision.ts:93`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L93) |
| `consultations` | `ConsultationRecord[]` | Yes | **CONTENT** (nested) | [`decision.ts:94`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L94) |

#### `CounterfactualDisposition`
*Source: [`packages/protocol/src/decision.ts:16-23`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L16-L23)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `escalatedTo` | `"parent" \| "human"` | No | **CODE** | [`decision.ts:17`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L17) |
| `wouldHaveDecided` | `string` (min 1) | No | **CONTENT** | [`decision.ts:18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L18) |
| `wouldHaveChosenCandidateId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`decision.ts:19`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L19) |
| `recordedBeforeAnswer` | `boolean` | No | **CODE** | [`decision.ts:20`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L20) |
| `recordedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`decision.ts:21`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L21) |

#### `ContextPosition`
*Source: [`packages/protocol/src/decision.ts:32-38`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L32-L38)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `tokensUsed` | `number` (integer >= 0) | No | **CODE** | [`decision.ts:33`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L33) |
| `contextWindowTokens` | `number` (integer > 0) | Yes | **CODE** | [`decision.ts:34`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L34) |
| `source` | `"harness_reported" \| "estimated"` | No | **CODE** | [`decision.ts:35`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L35) |
| `observedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`decision.ts:36`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L36) |

#### `ConsultationRecord`
*Source: [`packages/protocol/src/decision.ts:49-62`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L49-L62)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:50`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L50) |
| `decisionId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`decision.ts:51`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L51) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`decision.ts:52`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L52) |
| `question` | `string` (min 1) | No | **CONTENT** | [`decision.ts:53`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L53) |
| `candidates` | `ExecutionCandidate[]` | No | **CODE** (nested) | [`decision.ts:54`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L54) |
| `choice` | `ExecutionChoice` | Yes | **CODE** (nested) | [`decision.ts:55`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L55) |
| `attemptId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`decision.ts:56`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L56) |
| `charterDigest` | `string` (min 1) | Yes | **CODE** | [`decision.ts:57`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L57) |
| `outcome` | `"followed" \| "partly_followed" \| "not_followed" \| "no_answer" \| "unrecorded"` | No | **CODE** | [`decision.ts:58`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L58) |
| `requestedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`decision.ts:59`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L59) |
| `answeredAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | [`decision.ts:60`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L60) |

#### `PolicyDecision` (Discriminated Union on `randomized`)
*Source: [`packages/protocol/src/decision.ts:104-124`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L104-L124)*

*Branch 1: `randomized: false` (Deterministic Policy)*:
| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:106`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L106) |
| `decisionId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:107`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L107) |
| `policyVersion` | `string` (min 1) | No | **CODE** | [`decision.ts:108`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L108) |
| `candidateIds` | `IdSchema[]` | No | **CODE** | [`decision.ts:109`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L109) |
| `randomized` | `literal(false)` | No | **CODE** | [`decision.ts:110`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L110) |
| `assignedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`decision.ts:111`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L111) |

*Branch 2: `randomized: true` (Randomized Policy / Experiment Assignment)*:
| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:114`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L114) |
| `decisionId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`decision.ts:115`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L115) |
| `policyVersion` | `string` (min 1) | No | **CODE** | [`decision.ts:116`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L116) |
| `candidateIds` | `IdSchema[]` | No | **CODE** | [`decision.ts:117`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L117) |
| `randomized` | `literal(true)` | No | **CODE** | [`decision.ts:118`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L118) |
| `assignmentProbability` | `number` (0 < p <= 1) | No | **CODE** | [`decision.ts:119`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L119) |
| `arm` | `string` (min 1) | No | **CODE** | [`decision.ts:120`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L120) |
| `assignedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`decision.ts:121`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L121) |

#### `ExecutionCandidate`
*Source: [`packages/protocol/src/execution.ts:124-131`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L124-L131)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:125`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L125) |
| `recipe` | `ExecutionRecipe` | No | **CODE/CONTENT** (nested) | [`execution.ts:126`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L126) |
| `eligibility` | `"eligible" \| "rejected"` | No | **CODE** | [`execution.ts:127`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L127) |
| `reasonCodes` | `ReasonCode[]` | No | **CODE** | [`execution.ts:128`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L128) |
| `rank` | `number` (integer >= 0) | Yes | **CODE** | [`execution.ts:129`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L129) |

#### `ExecutionChoice` (Discriminated Union on `kind`)
*Source: [`packages/protocol/src/execution.ts:139-151`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L139-L151)*

*Branch 1: `kind: "INLINE"`*:
| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `kind` | `literal("INLINE")` | No | **CODE** | [`execution.ts:141`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L141) |
| `candidateId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:142`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L142) |
| `recipe` | `ClaudeInlineRecipeSchema` | No | **CODE/CONTENT** (nested) | [`execution.ts:143`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L143) |

*Branch 2: `kind: "DELEGATED"`*:
| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `kind` | `literal("DELEGATED")` | No | **CODE** | [`execution.ts:146`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L146) |
| `candidateId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:147`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L147) |
| `recipe` | `ExecutionRecipe` | No | **CODE/CONTENT** (nested) | [`execution.ts:148`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L148) |

#### `ExecutionRecipe` (Common & Surface Variants)
*Source: [`packages/protocol/src/execution.ts:74-122`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L74-L122)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:75`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L75) |
| `surface` | `SurfaceKind` enum | No | **CODE** | [`execution.ts:89, 105`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L89) |
| `model` | `string` (min 1) | Optional (Required on `antigravity.headless`) | **CODE** | [`execution.ts:90, 106`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L90) |
| `effort` | `string` (min 1) | Yes | **CODE** | [`execution.ts:76`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L76) |
| `authDomain` | `string` (min 1) | No | **CODE** | [`execution.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L77) |
| `permissionMode` | `string` (min 1) | Yes | **CODE** | [`execution.ts:78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L78) |
| `toolProfile` | `string` (min 1) | Yes | **CODE** | [`execution.ts:79`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L79) |
| `contextMode` | `"shared" \| "fresh" \| "resumed" \| "unknown"` | No | **CODE** | [`execution.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L80) |
| `configurationHash` | `string` (min 1) | No | **CODE** | [`execution.ts:81`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L81) |
| `capabilitySnapshotId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L82) |
| `vendorExtensions` | `Record<string, unknown>` | No | **CONTENT** | [`execution.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L83) |

---

### 1.2 Outcomes, Verification, Adjudication, Rework & Costs

#### `Attempt`
*Source: [`packages/protocol/src/execution.ts:182-196`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L182-L196)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:183`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L183) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:184`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L184) |
| `decisionId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`execution.ts:185`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L185) |
| `attemptNumber` | `number` (integer >= 1) | No | **CODE** | [`execution.ts:186`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L186) |
| `status` | `AttemptStatus` enum | No | **CODE** | [`execution.ts:187`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L187) |
| `startedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`execution.ts:188`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L188) |
| `endedAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | [`execution.ts:189`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L189) |
| `sourceSessionId` | `ExternalIdSchema` (string min 1) | Yes | **CODE** | [`execution.ts:190`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L190) |
| `exitCode` | `number` (integer) | Yes | **CODE** | [`execution.ts:191`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L191) |
| `stopRequestedAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | [`execution.ts:192`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L192) |
| `cessationObservedAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | [`execution.ts:193`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L193) |
| `externalEffectReconciledAt` | `TimestampSchema` (UTC ISO-8601) | Yes | **CODE** | [`execution.ts:194`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L194) |

#### `Claim`
*Source: [`packages/protocol/src/evidence.ts:19-28`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L19-L28)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:20`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L20) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:21`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L21) |
| `attemptId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:22`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L22) |
| `statement` | `string` (min 1) | No | **CONTENT** | [`evidence.ts:23`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L23) |
| `madeBy` | `"worker" \| "orchestrator" \| "human"` | No | **CODE** | [`evidence.ts:24`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L24) |
| `submittedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`evidence.ts:25`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L25) |
| `evidenceIds` | `IdSchema[]` | No | **CODE** | [`evidence.ts:26`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L26) |

#### `Evidence`
*Source: [`packages/protocol/src/evidence.ts:30-46`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L30-L46)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:31`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L31) |
| `claimId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`evidence.ts:32`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L32) |
| `kind` | `"command_result" \| "artifact" \| "human_attestation" \| "agent_verification" \| "event_trace"` | No | **CODE** | [`evidence.ts:33-39`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L33-L39) |
| `producedBy` | `"command" \| "adapter" \| "agent" \| "human"` | No | **CODE** | [`evidence.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L40) |
| `collectedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`evidence.ts:41`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L41) |
| `artifactRefs` | `IdSchema[]` | No | **CODE** | [`evidence.ts:42`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L42) |
| `summary` | `string` (min 1) | No | **CONTENT** | [`evidence.ts:43`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L43) |
| `contentHash` | `string` (min 1) | Yes | **CODE** | [`evidence.ts:44`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L44) |

#### `ArtifactReference`
*Source: [`packages/protocol/src/evidence.ts:5-12`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L5-L12)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:6`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L6) |
| `kind` | `"file" \| "directory" \| "url" \| "commit" \| "opaque"` | No | **CODE** | [`evidence.ts:7`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L7) |
| `locator` | `string` (min 1) | No | **CONTENT** | [`evidence.ts:8`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L8) |
| `contentHash` | `string` (min 1) | Yes | **CODE** | [`evidence.ts:9`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L9) |
| `observedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`evidence.ts:10`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L10) |

#### `VerificationObligation`
*Source: [`packages/protocol/src/evidence.ts:49-55`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L49-L55)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:50`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L50) |
| `kind` | `VerificationMethod` enum (`"command" \| "artifact" \| "human" \| "agent"`) | No | **CODE** | [`evidence.ts:51`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L51) |
| `spec` | `Record<string, unknown>` | No | **CONTENT** | [`evidence.ts:52`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L52) |
| `blocking` | `boolean` | No | **CODE** | [`evidence.ts:53`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L53) |

#### `VerificationPlan`
*Source: [`packages/protocol/src/evidence.ts:62-70`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L62-L70)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:63`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L63) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:64`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L64) |
| `obligations` | `VerificationObligation[]` | No | **CONTENT** (nested) | [`evidence.ts:65`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L65) |
| `reserveEnvelopeId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`evidence.ts:66`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L66) |
| `independenceRequirement` | `"none" \| "independent_agent" \| "human"` | No | **CODE** | [`evidence.ts:67`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L67) |
| `createdAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`evidence.ts:68`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L68) |

#### `Adjudication`
*Source: [`packages/protocol/src/evidence.ts:72-82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L72-L82)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:73`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L73) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`evidence.ts:74`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L74) |
| `claimIds` | `IdSchema[]` | No | **CODE** | [`evidence.ts:75`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L75) |
| `verdict` | `"VERIFIED" \| "REJECTED" \| "NEEDS_EVIDENCE" \| "UNKNOWN"` | No | **CODE** | [`evidence.ts:76`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L76) |
| `adjudicatedBy` | `"human" \| "agent" \| "command"` | No | **CODE** | [`evidence.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L77) |
| `rationale` | `string` | Yes | **CONTENT** | [`evidence.ts:78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L78) |
| `blind` | `boolean` | No | **CODE** | [`evidence.ts:79`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L79) |
| `adjudicatedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`evidence.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L80) |

#### `DeviationRecord` & `AnticipationLink`
*Source: [`packages/protocol/src/plan.ts:49-78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L49-L78)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:61`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L61) |
| `workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:62`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L62) |
| `attemptId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:63`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L63) |
| `planId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:64`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L64) |
| `category` | `"execution_method" \| "resource_consumption" \| "tool_use" \| "schedule" \| "trace_gap" \| "worker_substitution"` | No | **CODE** | [`plan.ts:65-72`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L65-L72) |
| `description` | `string` (min 1) | No | **CONTENT** | [`plan.ts:73`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L73) |
| `detectedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`plan.ts:74`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L74) |
| `recordedBy` | `"orchestrator" \| "worker" \| "human" \| "adapter"` | No | **CODE** | [`plan.ts:75`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L75) |
| `anticipatedBy.charterEntryId` | `string` (min 1) | Yes (on parent) | **CODE** | [`plan.ts:50`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L50) |
| `anticipatedBy.charterVersion` | `string` (min 1) | Yes (on parent) | **CODE** | [`plan.ts:51`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L51) |
| `anticipatedBy.charterDigest` | `string` (min 1) | Yes | **CODE** | [`plan.ts:52`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L52) |

#### `ReplanRecord`
*Source: [`packages/protocol/src/plan.ts:119-130`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L119-L130)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:120`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L120) |
| `objectiveId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:121`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L121) |
| `fromPlanId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:122`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L122) |
| `toPlanId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`plan.ts:123`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L123) |
| `triggers` | `ReplanTrigger[]` (min 1) | No | **CODE** | [`plan.ts:124`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L124) |
| `rationale` | `string` (min 1) | No | **CONTENT** | [`plan.ts:125`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L125) |
| `authorizedBy` | `"root_supervisor" \| "human"` | No | **CODE** | [`plan.ts:126`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L126) |
| `origin` | `"material" \| "inline_admission"` | No (defaults to `"material"`) | **CODE** | [`plan.ts:127`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L127) |
| `committedAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`plan.ts:128`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L128) |

#### `ResourceGrant` & `ResourceEnvelope`
*Source: [`packages/protocol/src/resources.ts:38-95`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L38-L95)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `ResourceEnvelope.id` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`resources.ts:82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L82) |
| `ResourceEnvelope.parentEnvelopeId` | `IdSchema` (UUIDv7 string) | Yes | **CODE** | [`resources.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L83) |
| `ResourceEnvelope.workUnitId` | `IdSchema` (UUIDv7 string) | No | **CODE** | [`resources.ts:84`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L84) |
| `ResourceEnvelope.grants` | `ResourceGrant[]` | No | **CODE** (nested) | [`resources.ts:85`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L85) |
| `ResourceEnvelope.createdAt` | `TimestampSchema` (UTC ISO-8601) | No | **CODE** | [`resources.ts:86`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L86) |
| `ResourceGrant.dimension` | `ResourceDimension` enum | No | **CODE** | [`resources.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L40) |
| `ResourceGrant.governance` | `ResourceGovernance` enum | No | **CODE** | [`resources.ts:41`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L41) |
| `ResourceGrant.target` | `number` (finite >= 0) | Yes | **CODE** | [`resources.ts:42`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L42) |
| `ResourceGrant.hard` | `number` (finite >= 0) | Yes | **CODE** | [`resources.ts:43`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L43) |
| `ResourceGrant.reserve` | `number` (finite >= 0) | Yes | **CODE** | [`resources.ts:44`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L44) |
| `ResourceGrant.unit` | `string` (min 1) | No | **CODE** | [`resources.ts:45`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L45) |
| `ResourceGrant.confidence` | `"exact" \| "estimated" \| "observed" \| "unknown"` | No | **CODE** | [`resources.ts:46`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L46) |

#### `ReserveRelease` (Interface)
*Source: [`packages/protocol/src/resources.ts:270-278`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L270-L278)*

| Field Name | Type | Optional | Class | Source Citation |
| :--- | :--- | :--- | :--- | :--- |
| `newEnvelopeId` | `string` (UUIDv7 string) | No | **CODE** | [`resources.ts:272`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L272) |
| `dimension` | `ResourceDimension` enum | No | **CODE** | [`resources.ts:273`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L273) |
| `amount` | `number` | No | **CODE** | [`resources.ts:274`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L274) |
| `authorizedByReplanId` | `string` (UUIDv7 string) | No | **CODE** | [`resources.ts:276`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L276) |
| `releasedAt` | `string` (UTC ISO-8601) | No | **CODE** | [`resources.ts:277`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L277) |

---

## 2. Verbatim Enum Vocabularies

### 2.1 Disposition & Outcome Enums
* **`WorkUnitStatus`** ([`packages/protocol/src/execution.ts:154-163`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L154-L163)):
  `"PLANNED"`, `"DECIDED"`, `"EXECUTING"`, `"SUBMITTED"`, `"VERIFIED"`, `"REJECTED"`, `"NEEDS_EVIDENCE"`, `"UNKNOWN"`
* **`AttemptStatus`** ([`packages/protocol/src/execution.ts:166-173`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L166-L173)):
  `"STARTED"`, `"RUNNING"`, `"SUBMITTED"`, `"HALT_REQUESTED"`, `"ABANDONED"`, `"FAILED"`
* **`AdjudicationVerdict`** ([`packages/protocol/src/evidence.ts:76`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L76)):
  `"VERIFIED"`, `"REJECTED"`, `"NEEDS_EVIDENCE"`, `"UNKNOWN"`
* **`AdjudicationAdjudicator`** ([`packages/protocol/src/evidence.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L77)):
  `"human"`, `"agent"`, `"command"`
* **`ConsultationOutcome`** ([`packages/protocol/src/decision.ts:58`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L58)):
  `"followed"`, `"partly_followed"`, `"not_followed"`, `"no_answer"`, `"unrecorded"`
* **`TreatmentMode`** ([`packages/protocol/src/decision.ts:91`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L91)):
  `"prospective"`, `"retrospective"`
* **`CounterfactualEscalatedTo`** ([`packages/protocol/src/decision.ts:17`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L17)):
  `"parent"`, `"human"`
* **`CandidateEligibility`** ([`packages/protocol/src/execution.ts:127`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L127)):
  `"eligible"`, `"rejected"`
* **`ClaimMadeBy`** ([`packages/protocol/src/evidence.ts:24`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L24)):
  `"worker"`, `"orchestrator"`, `"human"`
* **`EvidenceKind`** ([`packages/protocol/src/evidence.ts:33-39`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L33-L39)):
  `"command_result"`, `"artifact"`, `"human_attestation"`, `"agent_verification"`, `"event_trace"`
* **`EvidenceProducedBy`** ([`packages/protocol/src/evidence.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L40)):
  `"command"`, `"adapter"`, `"agent"`, `"human"`
* **`ArtifactReferenceKind`** ([`packages/protocol/src/evidence.ts:7`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L7)):
  `"file"`, `"directory"`, `"url"`, `"commit"`, `"opaque"`
* **`DeviationCategory`** ([`packages/protocol/src/plan.ts:65-72`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L65-L72)):
  `"execution_method"`, `"resource_consumption"`, `"tool_use"`, `"schedule"`, `"trace_gap"`, `"worker_substitution"`
* **`DeviationRecordedBy`** ([`packages/protocol/src/plan.ts:75`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L75)):
  `"orchestrator"`, `"worker"`, `"human"`, `"adapter"`
* **`ReplanAuthorizer`** ([`packages/protocol/src/plan.ts:126`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L126)):
  `"root_supervisor"`, `"human"`
* **`ReplanOrigin`** ([`packages/protocol/src/plan.ts:115-116`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L115-L116)):
  `"material"`, `"inline_admission"`
* **`TraceHealthStatus`** ([`packages/protocol/src/events.ts:98-104`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L98-L104)):
  `"HEALTHY"`, `"PARTIAL"`, `"DEGRADED"`, `"UNTRUSTWORTHY"`, `"UNKNOWN"`
* **`RawEventParseStatus`** ([`packages/protocol/src/events.ts:47`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L47)):
  `"parsed"`, `"partial"`, `"unparsed"`, `"invalid"`
* **`RetentionClass`** ([`packages/protocol/src/events.ts:13-18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L13-L18)):
  `"transient"`, `"operational"`, `"sensitive"`, `"unclassified"`

### 2.2 Candidate, Recipe & Surface Kinds
* **`SURFACE_KINDS`** ([`packages/protocol/src/execution.ts:11-22`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L11-L22)):
  `"claude.inline"`, `"claude.subagent"`, `"claude.workflow"`, `"claude.agent_team"`, `"claude.headless"`, `"claude.headless_bare"`, `"antigravity.headless"`, `"codex.app_server"`, `"codex.cli"`, `"api.deepseek"`
* **`ExecutionChoiceKind`** ([`packages/protocol/src/execution.ts:141, 146`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L141)):
  `"INLINE"`, `"DELEGATED"`
* **`ContextMode`** ([`packages/protocol/src/execution.ts:71`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L71)):
  `"shared"`, `"fresh"`, `"resumed"`, `"unknown"`

### 2.3 Reason Codes & Replan Triggers
* **`REASON_CODES`** ([`packages/protocol/src/execution.ts:46-66`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L46-L66)):
  `"AUTHORITY_LIMIT"`, `"CACHE_WARMTH"`, `"CAPABILITY_UNSUPPORTED"`, `"CODE_SPECIALIZATION"`, `"CONTEXT_ISOLATION"`, `"COST_POLICY"`, `"CRITICAL_PATH"`, `"EXPERIMENT_ASSIGNMENT"`, `"HARD_REQUIREMENT_UNMET"`, `"MODEL_DIVERSIFICATION"`, `"PARALLEL_INDEPENDENT"`, `"PARENT_STEERING_REQUIRED"`, `"PEER_COMMUNICATION"`, `"PROVIDER_CAPACITY"`, `"PROVIDER_DISABLED"`, `"ROOT_OVERRIDE"`, `"STABLE_TOPOLOGY"`, `"TIGHT_COUPLING"`, `"VERIFICATION_INDEPENDENCE"`
* **`REPLAN_TRIGGERS`** ([`packages/protocol/src/plan.ts:81-92`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L81-L92)):
  `"critical_path_changed"`, `"deliverable_or_acceptance_changed"`, `"dependency_edges_changed"`, `"hard_ceiling_or_reserve_changed"`, `"parent_authority_changed"`, `"sub_orchestrator_created"`, `"surface_or_model_family_changed"`, `"target_grant_changed_over_25_percent"`, `"verification_method_changed"`, `"work_unit_set_changed"`
* **`PROTOCOL_INVARIANT_CODES`** ([`packages/protocol/src/errors.ts:6-28`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/errors.ts#L6-L28)):
  `"AUTHORITY_DEPTH_NOT_DECREASING"`, `"AUTHORITY_DESCENDANTS_EXCEED_PARENT"`, `"AUTHORITY_EXPIRY_EXTENDED"`, `"AUTHORITY_MODEL_ESCALATION"`, `"AUTHORITY_RIGHT_ESCALATION"`, `"AUTHORITY_SURFACE_ESCALATION"`, `"AUTHORITY_TOOL_DENIAL_RELAXED"`, `"DUPLICATE_WORK_UNIT"`, `"ENVELOPE_PARENT_MISMATCH"`, `"GOVERNANCE_ESCALATION"`, `"GRANT_EXCEEDS_PARENT"`, `"MISSING_WORK_UNIT"`, `"PLAN_CYCLE"`, `"RESERVE_NOT_RELEASED"`, `"RESERVE_RELEASE_EXCEEDS_RESERVE"`, `"RESERVE_RELEASE_UNAUTHORIZED"`, `"RETROSPECTIVE_DECISION"`, `"STRATUM_MISMATCH"`, `"UNGRANTED_DIMENSION"`, `"UNKNOWN_DEPENDENCY"`, `"WORK_UNIT_NOT_IN_PLAN"`

### 2.4 Verification Outcomes, Methods & Independence
* **`VerificationMethod`** ([`packages/protocol/src/objective.ts:4`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/objective.ts#L4)):
  `"command"`, `"artifact"`, `"human"`, `"agent"`
* **`IndependenceRequirement`** ([`packages/protocol/src/evidence.ts:67`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L67)):
  `"none"`, `"independent_agent"`, `"human"`

### 2.5 Policy & Experiment Types
* **`PolicyDecision`** ([`packages/protocol/src/decision.ts:104-123`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L104-L123)):
  Discriminated union on `randomized` boolean:
  * Deterministic branch: `randomized: false`, `id`, `decisionId`, `policyVersion`, `candidateIds`, `assignedAt`.
  * Randomized experiment branch: `randomized: true`, `id`, `decisionId`, `policyVersion`, `candidateIds`, `assignmentProbability` (0 < p <= 1), `arm`, `assignedAt`.
* **Experiment Reason Code**: `"EXPERIMENT_ASSIGNMENT"` in `REASON_CODES` ([`packages/protocol/src/execution.ts:54`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L54))

### 2.6 Additional Protocol Vocabularies
* **`OrchestratorRole`** ([`packages/protocol/src/authority.ts:6-14`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L6-L14)):
  `"ROOT_SUPERVISOR"`, `"SUB_ORCHESTRATOR"`, `"ADAPTIVE_WORKER"`, `"LEAF"`
* **`SupportLevel`** ([`packages/protocol/src/capability.ts:11-21`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L11-L21)):
  `"enforced"`, `"supported"`, `"best_effort"`, `"observed_only"`, `"unsupported"`, `"unknown"`
* **`ResourceGovernance`** ([`packages/protocol/src/resources.ts:10-18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L10-L18)):
  `"hard_delegateops"`, `"hard_surface"`, `"soft_observed"`, `"opaque_external"`
* **`ResourceDimension`** ([`packages/protocol/src/resources.ts:21-34`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L21-L34)):
  `"api_usd"`, `"input_tokens"`, `"output_tokens"`, `"wall_clock_ms"`, `"attempts"`, `"children"`, `"concurrency"`, `"provider_quota_estimate"`, `"human_review_minutes"`
* **`AuthStatus`** ([`packages/protocol/src/provider-state.ts:11-18`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L11-L18)):
  `"authenticated_subscription"`, `"authenticated_api"`, `"unauthenticated"`, `"expired"`, `"unknown"`
* **`QuotaPressure`** ([`packages/protocol/src/provider-state.ts:25-33`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L25-L33)):
  `"plentiful"`, `"normal"`, `"constrained"`, `"nearly_exhausted"`, `"exhausted"`, `"unknown"`
* **`NORMALIZED_EVENT_NAMES`** ([`packages/protocol/src/events.ts:55-78`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts#L55-L78)):
  `"objective_created"`, `"plan_committed"`, `"decision_committed"`, `"attempt_started"`, `"attempt_progress"`, `"usage_observed"`, `"budget_soft_crossed"`, `"budget_hard_crossed"`, `"artifact_produced"`, `"claim_submitted"`, `"deviation_recorded"`, `"replan_committed"`, `"halt_requested"`, `"cessation_observed"`, `"verification_started"`, `"verification_completed"`, `"adjudication_recorded"`, `"human_intervention"`, `"provider_state_changed"`, `"trace_gap_detected"`

---

## 3. Fields Presupposing a SINGLE Decision-Maker or Single Root

The following fields enforce single-authority, single-parent, or single-session semantics without multi-writer / consensus affordances:

1. **`supervisorSessionId: ExternalIdSchema`** — [`packages/protocol/src/decision.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L80)
   * Singular supervisor session minting the decision (*"candidates is the menu the supervisor actually had... committed before activation"*, lines 65-66).
2. **`choice: ExecutionChoiceSchema`** — [`packages/protocol/src/decision.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L83)
   * Singular choice commit (`candidateId` + single `recipe`), admitting no committee voting or joint choice.
3. **`authorityEnvelopeId: IdSchema`** — [`packages/protocol/src/decision.ts:86`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L86)
   * Exact singular authority envelope governing the decision.
4. **`escalatedTo: z.enum(["parent", "human"])`** — [`packages/protocol/src/decision.ts:17`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L17)
   * Binary choice between single immediate parent supervisor or a human.
5. **`authorizedBy: z.enum(["root_supervisor", "human"])`** — [`packages/protocol/src/plan.ts:126`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L126)
   * Replan authorization restricted strictly to a singular `"root_supervisor"` or `"human"`.
6. **`parentWorkUnitId: IdSchema.optional()`** — [`packages/protocol/src/plan.ts:29`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L29)
   * Strict single-parent hierarchy for work decomposition.
7. **`parentPlanId: IdSchema.optional()`** — [`packages/protocol/src/plan.ts:15`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts#L15)
   * Single linear ancestry for plan revisions (`nextPlanVersion`, lines 295-312).
8. **`parentEnvelopeId: IdSchema.optional()`** — [`packages/protocol/src/resources.ts:83`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L83)
   * Resource budgets drawn from a single parent envelope (`assertChildEnvelopeAllowed`, line 187).
9. **`owner: z.string().min(1)`** — [`packages/protocol/src/objective.ts:26`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/objective.ts#L26)
   * Single objective owner (*"only the owner or a human-authorized root path may change acceptance"*, lines 19-20).
10. **`role: OrchestratorRoleSchema`** — [`packages/protocol/src/authority.ts:30`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L30)
    * Single hierarchical role assigned per work unit ([`ROOT_SUPERVISOR`, `SUB_ORCHESTRATOR`, `ADAPTIVE_WORKER`, `LEAF`]).
11. **`escalation: z.enum(["parent", "human"])`** — [`packages/protocol/src/authority.ts:41`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L41)
    * Single escalation route targeting one parent or human.
12. **`madeBy: z.enum(["worker", "orchestrator", "human"])`** — [`packages/protocol/src/evidence.ts:24`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L24)
    * Single maker entity for completion claims.
13. **`adjudicatedBy: z.enum(["human", "agent", "command"])`** — [`packages/protocol/src/evidence.ts:77`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L77)
    * Single adjudicator evaluating evidence.
14. **Reason Codes**: `"PARENT_STEERING_REQUIRED"` ([`execution.ts:58`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L58)) and `"ROOT_OVERRIDE"` ([`execution.ts:62`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L62)).

---

## 4. Fields Recording SITUATION at Decision Time

### 4.1 Budgets & Resource Envelopes
* **`DecisionRecord.resourceEnvelopeId`** ([`packages/protocol/src/decision.ts:87`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L87)): Pointer to `ResourceEnvelope`.
* **`ResourceEnvelope.grants`** ([`packages/protocol/src/resources.ts:85`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L85)): Array of `ResourceGrant` records containing:
  * `dimension` ([resources.ts:40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L40)): 9 dimensions (`api_usd`, `input_tokens`, `output_tokens`, `wall_clock_ms`, `attempts`, `children`, `concurrency`, `provider_quota_estimate`, `human_review_minutes`).
  * `governance` ([resources.ts:41](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L41)): `hard_delegateops`, `hard_surface`, `soft_observed`, `opaque_external`.
  * `target` ([resources.ts:42](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L42)): Advisory budget.
  * `hard` ([resources.ts:43](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L43)): Enforceable ceiling.
  * `reserve` ([resources.ts:44](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L44)): Protected verification reserve.
  * `unit` ([resources.ts:45](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L45)): Unit string.
  * `confidence` ([resources.ts:46](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L46)): `exact`, `estimated`, `observed`, `unknown`.
* **`VerificationPlan.reserveEnvelopeId`** ([`packages/protocol/src/evidence.ts:66`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts#L66)): Protected reserve allocation for verification.
* **Reason Codes**: `"COST_POLICY"` ([execution.ts:52](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L52)), `"AUTHORITY_LIMIT"` ([execution.ts:47](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L47)).

### 4.2 Provider & Capacity State
* **`ProviderStateSnapshot`** ([`packages/protocol/src/provider-state.ts:56-73`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L56-L73)):
  * `provider: string` ([provider-state.ts:58](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L58))
  * `surface: SurfaceKind` ([provider-state.ts:59](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L59))
  * `enabled: boolean` ([provider-state.ts:60](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L60))
  * `installedVersion: string.optional()` ([provider-state.ts:61](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L61))
  * `authDomain: string` ([provider-state.ts:62](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L62))
  * `authStatus: AuthStatus` ([provider-state.ts:63](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L63)) (`authenticated_subscription`, `authenticated_api`, `unauthenticated`, `expired`, `unknown`)
  * `availableModels: string[].optional()` ([provider-state.ts:64](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L64))
  * `quotaPressure: QuotaPressure` ([provider-state.ts:65](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L65)) (`plentiful`, `normal`, `constrained`, `nearly_exhausted`, `exhausted`, `unknown`)
  * `quotaSource: "user_supplied" | "machine_observed" | "unknown"` ([provider-state.ts:66](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L66))
  * `observedUsage: ObservedUsage.optional()` ([provider-state.ts:67](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L67)): `inputTokenCount`, `outputTokenCount`, `cacheReadTokenCount`, `cacheCreationTokenCount`, `windowResetAt` ([provider-state.ts:36-40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L36-L40)).
  * `concurrencyInUse: number` ([provider-state.ts:68](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L68))
  * `concurrencyLimit: number.optional()` ([provider-state.ts:69](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L69))
  * `recentErrors: AdapterError[]` ([provider-state.ts:70](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L70)): `occurredAt`, `code`, `summary`.
  * `capturedAt: TimestampSchema` ([provider-state.ts:71](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L71))
* **`CapabilitySnapshot`** (linked via `ExecutionRecipe.capabilitySnapshotId`, [`execution.ts:82`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L82); defined in [`packages/protocol/src/capability.ts:23-44`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L23-L44)):
  * Feature Support Levels: `launch`, `message`, `steer`, `requestStop`, `observeCessation`, `pauseResume`, `sessionResume`, `nestedDelegation`, `eventStream`, `tokenUsage`, `cacheUsage`, `hardBudget` ([capability.ts:29-40](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L29-L40)).
  * `knownLimitations: string[]` ([capability.ts:41](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L41))
  * `rawProbe: Record<string, unknown>` ([capability.ts:42](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts#L42))
* **Reason Codes**: `"PROVIDER_CAPACITY"` ([execution.ts:60](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L60)), `"PROVIDER_DISABLED"` ([execution.ts:61](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L61)), `"CAPABILITY_UNSUPPORTED"` ([execution.ts:49](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L49)), `"CACHE_WARMTH"` ([execution.ts:48](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L48)).

### 4.3 Time Constraints & Expiries
* **`AuthorityEnvelope.expiresAt`** ([`packages/protocol/src/authority.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts#L40)): Expiry timestamp bounding authority validity.
* **`ObservedUsage.windowResetAt`** ([`packages/protocol/src/provider-state.ts:40`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts#L40)): Provider quota rate-limit reset boundary.
* **`ResourceGrant` dimension `"wall_clock_ms"`** ([`packages/protocol/src/resources.ts:25`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts#L25)): Wall clock time allocation.
* **`DecisionRecord.committedAt`** ([`packages/protocol/src/decision.ts:90`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L90)): Timestamp of prospective commitment.
* **Reason Code**: `"CRITICAL_PATH"` ([execution.ts:53](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L53)).

### 4.4 Context Snapshots & Agent State
* **`DecisionRecord.contextSnapshotId`** ([`packages/protocol/src/decision.ts:89`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L89)): Snapshot ID capturing context at decision time.
* **`DecisionRecord.contextPositionAtDecision`** ([`packages/protocol/src/decision.ts:93`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L93)): `ContextPosition` recording `tokensUsed`, `contextWindowTokens`, `source`, `observedAt` ([decision.ts:33-36](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L33-L36)).
* **`ExecutionRecipe.contextMode`** ([`packages/protocol/src/execution.ts:80`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L80)): `"shared" | "fresh" | "resumed" | "unknown"`.
* **`ExecutionRecipe.toolProfile`** ([`packages/protocol/src/execution.ts:79`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L79)): Tool access profile available at decision time.
* **`ExecutionRecipe.configurationHash`** ([`packages/protocol/src/execution.ts:81`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L81)): Configuration hash at decision time.
* **`DecisionRecord.counterfactual`** ([`packages/protocol/src/decision.ts:92`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L92)): Agent's counterfactual disposition prior to escalation.
* **`DecisionRecord.consultations`** ([`packages/protocol/src/decision.ts:94`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts#L94)): In-flight advisor consultations that informed the choice.
* **Reason Codes**: `"CONTEXT_ISOLATION"` ([execution.ts:51](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L51)), `"TIGHT_COUPLING"` ([execution.ts:64](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts#L64)).

---

## 5. Declaration of Files Not Read

### 5.1 Workspace Files Inventory & Status
Every single file present in the workspace `s4-head` (16 files in total) was read and inspected in full:

1. [`EXPORTED_AT_COMMIT.txt`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/EXPORTED_AT_COMMIT.txt) — **READ**
2. [`docs/schemas/delegateops-v0alpha1.schema.json`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/docs/schemas/delegateops-v0alpha1.schema.json) — **READ**
3. [`packages/protocol/src/authority.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/authority.ts) — **READ**
4. [`packages/protocol/src/capability.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/capability.ts) — **READ**
5. [`packages/protocol/src/decision.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/decision.ts) — **READ**
6. [`packages/protocol/src/errors.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/errors.ts) — **READ**
7. [`packages/protocol/src/events.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/events.ts) — **READ**
8. [`packages/protocol/src/evidence.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/evidence.ts) — **READ**
9. [`packages/protocol/src/execution.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/execution.ts) — **READ**
10. [`packages/protocol/src/ids.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/ids.ts) — **READ**
11. [`packages/protocol/src/index.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/index.ts) — **READ**
12. [`packages/protocol/src/json-schema.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/json-schema.ts) — **READ**
13. [`packages/protocol/src/objective.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/objective.ts) — **READ**
14. [`packages/protocol/src/plan.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/plan.ts) — **READ**
15. [`packages/protocol/src/provider-state.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/provider-state.ts) — **READ**
16. [`packages/protocol/src/resources.ts`](file:///private/tmp/claude-501/-Users-rookslog-Development-delegate-ops/5f55ceae-1828-4c05-878b-28d5c2cb66c4/scratchpad/s4-head/packages/protocol/src/resources.ts) — **READ**

### 5.2 External / Unexported Documents Referenced in Code Comments (Not in Workspace)
The following documents are cited in source code comments but do not exist in this clean protocol export workspace:
* `docs/architecture/DECISION_CHARTER.md` (cited in `decision.ts:8`, `decision.ts:42`, `plan.ts:43`)
* `docs/architecture/PROTOCOL_INVARIANTS.md` (cited in `errors.ts:33`)
* `packages/protocol/test/schema.test.ts` (cited in `execution.ts:43`)
* `packages/core/src/repositories/envelope-writes.ts` (cited in `authority.ts:86`)
