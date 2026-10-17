# Notion learning-space format 1

Use this baseline for a fresh space. Read [record-format.md](record-format.md) for the shared learning-record contract. Preserve its field names, types, and options; write explanatory page content in the learner's language.

## Objects

- One root page, default title `English Learning`.
- One empty `Active Learning` database under that page.
- One ordinary `Learning Profile` page under that page.

The profile is a page, not another database. Training logs and method catalogs are outside this baseline.

## Active Learning schema

Create the ten properties defined in the shared record specification’s field table. Map `title`, `select`, `multi_select`, `number`, `date`, `created_time`, and `last_edited_time` to the connection's supported types, using the exact option names. If the connection accepts SQL DDL, translate those definitions to its database-creation `schema` argument and pass `Active Learning` as the database title. Do not send creation DDL to a row-query tool or create a local database as a substitute.

`Status` is a select property. System time properties are read-only. A normal table view is enough; additional views and native templates are optional and must not be claimed unless created and checked. Fixed broad categories and free-text Topic remain separate dimensions; no subcategory tree or custom knowledge-point ID is required.

## Root-page content

The root is a learning-space entrance. Show the native child entries for Active Learning and Learning Profile; add at most a brief explanation of their purpose where useful. Do not duplicate those entries with another list of mentions. For a test explicitly requested by the user, a single sentence saying the material is fictional is sufficient.

Do not put creation SQL, object IDs, format versions, maintenance instructions, test progress/results, record conventions, or a blank entry outline on the root or profile. Keep technical instructions in the skill references and execution context. The learner's pages should contain navigation and learning content.

## Internal record conventions

Use the record unit, evidence rules, conversation-level count, deduplication rules, and three-section body template in [record-format.md](record-format.md). Setup creates an empty database; knowing the contract does not collect material or authorize a schedule. Do not display the blank body outline on the learner's pages or claim a native template was created.

The format contract's canonical source is bundled here. Collection carries a generated identical copy so either skill can be installed alone. A format version is independent of the plugin release version.

## Learning Profile outline

Populate only information supplied by this learner or evidence explicitly provided for setup. Do not search unrelated personal sources to fill gaps. Missing goals and preferences may say `Not provided`; missing level information must say `Not assessed`. Localize those labels with the surrounding prose when appropriate.

Keep profile claims tied to their basis. Update broader capability judgments only from an explicit assessment or sufficient evidence across occasions. A text transcript alone does not support acoustic pronunciation judgments.

Use these five sections:

1. **Learner overview** — Relevant background the learner supplied, such as language background and preferred explanation language. Do not require personal identifiers.
2. **Learning goals** — Supplied goals and use cases; otherwise not provided.
3. **Proficiency information** — Overall level and separate speaking, listening, reading, and writing entries, each with a level or `Not assessed` and its basis. Label a self-reported level as self-report. Do not turn one overall level into assessed levels for every skill, or convert a casual description into an unsupported CEFR rating. No placement test is required for setup.
4. **Learning preferences and observations** — Supplied preferences and evidence-based observations, with their source or uncertainty. Do not infer permanent weaknesses from one error.
5. **Current focus** — A focus the learner has already chosen, or not set. Reference Active Learning as the place for specific problems and occurrence evidence instead of duplicating them here.

On a fresh setup, an otherwise empty profile with these sections and honest missing-information labels is complete. On a resumed setup, preserve all existing learner content; complete only clearly missing structure within the requested scope.

## Verification

Read back the actual objects and check the ten database properties and their types/options against the schema, both child locations, the minimal root navigation, and the profile's five sections and level-evidence labels. Confirm the learner pages contain no setup SQL, technical metadata, handoff lists, rule manuals, or test reports. A newly created learning-problem database must be empty; a resumed one must retain its existing records. Do not claim that future collection, deduplication, or mastery judgments have been tested by verifying the initial structure.

Keep the actual object identifiers in the execution context, not a visible handoff section. Later collection or maintenance must fetch the live root and data-source schema to discover the current objects before writing. Keep runtime identifiers and personal content outside the public plugin source.
