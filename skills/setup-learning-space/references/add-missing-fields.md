# Add missing fields to an existing Notion database

Use this mode when the user identifies an existing learning database and asks to add fields it lacks. The scope is additive schema changes; old records keep their content and values.

## Identify the target and differences

1. Fetch the supplied link and resolve the actual database and data source. If it is a space page, inspect its database entries. A page with multiple plausible databases or a database with multiple plausible data sources needs a clear target; do not update every candidate or create a replacement.
2. Read the field table in [record-format.md](record-format.md) for the target schema and its meaning. Compare property names with the live schema. Keep all existing properties, including custom fields. A differently named non-title property is not authorization to rename, copy, or merge it with a baseline property.
3. For an existing property with a baseline name, preserve its ID, type, options, and values. Record type or option differences as unresolved; do not alter it to match the template. Such differences do not prevent adding other independent missing fields.
4. Notion allows only one title property, and the schema update tool cannot add or replace it. If the existing title is named something other than `Topic`, keep that title and report the naming difference. Do not try to add another title, rename the original, or create a text property pretending to be a title.

## Apply additions only

Read the current schema-update tool's input format. For a connection with the SQL DDL interface, send only `ADD COLUMN` statements for absent, supported non-title properties, using the baseline types and option definitions. For example, when those two properties are actually absent:

```sql
ADD COLUMN "Occurrence Count" NUMBER;
ADD COLUMN "Last Observed" DATE
```

Use the verified data-source ID. Do not replay `CREATE TABLE`, or send `ALTER`, `RENAME`, or `DROP` statements. Do not change existing select options, view filters, relations, layouts, titles, descriptions, or profile pages. In particular, do not extend or replace an existing option list to make it match the baseline.

Leave new editable properties unset on older records. Do not set defaults such as `0`, `1`, `New`, `Unknown`, today's date, or `Not assessed` across those records, and do not infer historical counts or observation dates. Native created/edited-time properties may display Notion's existing system metadata automatically; do not populate them manually or treat them as learning-event dates.

This mode performs no record writes: do not create, copy, merge, delete, or update learning entries, and do not reorganize their bodies. Do not recreate the space or add setup notes to its pages. If nothing is missing, perform no writes.

## Verify and resume

- Keep the pre-change schema and a bounded faithful sample of existing rows in the execution context when rows are available. After the update, fetch the live schema again: planned additions should exist with the right types/options; pre-existing definitions and custom fields should be unchanged. Compare property IDs where the connection exposes them, and state any unavailable checks rather than inventing IDs.
- Read back a bounded sample to check that old values remain and new editable fields are unset. State the verification coverage accurately; sampling is not a full audit of every record or page body. System-managed metadata may reflect platform activity.
- If an update result is partial or uncertain, re-fetch the schema and add only properties still absent. Do not rerun the original batch blindly. A second completed run should require no writes.
- Report fields added and any preserved conflicts in a short response. A preserved conflict means the database has not been fully standardized; do not claim conversion or historical data migration. If a required addition is unsupported, retain the existing database and explain what remains.

Keep SQL, object IDs, comparison notes, and test output in the execution context, not the learner's pages or distributed plugin source.
