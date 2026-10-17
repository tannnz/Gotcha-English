---
name: setup-learning-space
description: Set up or resume an English-learning space in Notion, or add missing fields to an existing learning database while preserving its records.
---

# Setup Learning Space

Build the shared learning-data space independently of any teaching skill. This version supports Notion: create a space with an empty learning-problem database and learner profile, resume an incomplete setup, or add missing fields to an existing database. It does not collect conversations, teach a lesson, assess proficiency, or schedule automation.

Read [references/notion-space.md](references/notion-space.md) for space setup and its linked shared record-format resources for the exact schema, body template, and evidence rules. Keep those conventions separate from the host's tool names so the skill can run with the Notion connection available in that host.

## Establish the request

- Determine whether the user wants a new space, an incomplete setup resumed, or missing fields added to an existing database. Requests to discuss the design or edit this skill do not call for Notion writes.
- Treat a supplied example space as a reference unless the user identifies it as the destination or the database to update. Use the generic schema in the reference; do not copy another learner's records or profile.
- For a fresh setup, create a new root page titled `English Learning` unless the user supplies another title. Put it under the user's specified parent. If no destination is named, use the connection's private-draft creation mode when supported and report where it was created; otherwise ask for the destination needed by that connection.
- Use goals, preferences, and level information already supplied for this learner. Missing information does not block setup. Mark missing proficiency information as `Not assessed`; distinguish self-report from assessed evidence.

## Add missing fields to an existing database

When the user asks to supplement an existing learning database, follow [references/add-missing-fields.md](references/add-missing-fields.md). Use only the missing properties from the baseline schema. Keep older records' new editable fields unset; do not backfill them, modify existing properties or options, or rewrite pages. Do not run the new-space steps or create a replacement database for this mode.

## Create or resume the space

1. Inspect the available Notion tools and their current input schemas. Read the connection's page-content syntax before writing page bodies. Use the tools' supported creation flow; do not assume a fixed MCP prefix or provide credentials in the skill. If the connection lacks a required read or write operation, explain the missing capability and return the setup specification without claiming creation.
2. Fetch the specified parent or an explicitly identified incomplete space. Inspect existing objects before resuming. An unrelated object with the same name is not proof that it belongs to this setup.
3. Create the root page, then the `Active Learning` database and ordinary `Learning Profile` child page. Use the schema and profile outline in the reference. Keep the database empty; do not add sample mistakes, guessed levels, or copied personal material. This baseline does not create Learning Sessions or Practice Methods databases.
4. Keep the actual root-page ID, database ID, data-source ID, and profile-page ID from successful results before continuing. Handle asynchronous results before dependent operations. Use the data-source ID for row operations, not the database's page ID.
5. Keep the root page as a short learning-space entrance: the database and profile entries, with a brief description only where useful. Native child blocks already serve as entry links; do not add a duplicate navigation list. Keep SQL, object IDs, format versions, maintenance handoffs, record-rule manuals, blank entry outlines, and test logs out of learner pages. These are execution details or skill references. For an explicitly requested test space, one short note identifying fictional material is enough. Create children through explicit parent arguments; preserve their existing blocks and unrelated learner content when updating the root.
6. Read back the root and both children. Check the minimal navigation, parent locations, database properties and option sets, profile sections and evidence labels. For a newly created database, confirm it contains no learning records using a bounded row read. When resuming, preserve existing records and check that setup did not change them. Treat unavailable or truncated readback as incomplete verification, not success.

## Resume and stop conditions

Resume only within the space identified by the user or by this run's successful results. Reuse matching components and create only missing components. Preserve populated profiles, existing records, and custom properties. Do not reset values or overwrite learner content with the initial outline.

After an uncertain creation result, inspect the known parent and created IDs before retrying. If the outcome cannot be established, report the completed objects and uncertainty instead of creating another copy. Use the missing-fields mode for absent properties. Preserve and report incompatible existing types or options; converting properties, mapping old values, and importing learning material are separate maintenance work.

## Return the result

Give the learner the space link, or the updated database link for missing-fields mode, and a short statement of what is ready or still needs action. Explain the setup's collection/automation boundary when relevant. Provide separate child links or technical details only when useful for the request, rather than returning a maintenance checklist by default.

Keep runtime identifiers in the execution context. Later maintenance can fetch the root and database to discover child and data-source IDs; it does not require an ID list or format marker on the learner's pages. Never put personal runtime identifiers in the distributed skill files. Claim a verified setup only after the readback checks pass.
