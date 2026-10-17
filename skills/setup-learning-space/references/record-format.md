# Learning-issue record format 1

Setup and collection share this specification. One entry represents one specific English-learning problem; evidence from several conversations may belong to it. Different meanings or rules remain separate even if their titles or categories are similar. Write learning content in the learner's language and keep the three body headings below.

## Database fields

Use these definitions when initializing a database. During collection, read the actual fields and use compatible existing fields/options. Do not change the schema or guess an ambiguous mapping. Report differences that prevent a correct write; unrelated custom fields need not prevent collection.

| Field | Type | Meaning or options |
| --- | --- | --- |
| Topic | title | English knowledge point plus a short Chinese description of the problem; adapt the description to the learner's language when needed |
| Category | select | Vocabulary; Grammar; Pronunciation; Discourse & Pragmatics; Fluency; Writing Conventions |
| Difficulty | multi_select | Unknown; Misuse; Retrieval; Comprehension; Naturalness |
| Mode | multi_select | Speaking; Listening; Writing; Reading |
| Occurrence Count | number | Distinct conversations that independently expose this problem, excluding repeated source material |
| First Observed | date | Earliest supported occurrence date |
| Last Observed | date | Latest supported occurrence date |
| Status | select | New; Learning; Reviewing; Mastered |
| Created Time | created_time | System-managed record creation time |
| Last Edited | last_edited_time | System-managed record edit time |

Difficulty describes the problem, not its severity: Unknown for unfamiliar words or rules, Misuse for actual errors, Retrieval for difficulty producing a known expression, Comprehension for difficulty interpreting context, and Naturalness for an evidenced contextual usage problem. Optional stylistic improvements are not problems. Choose Mode from evidence and leave it unset when unknown.

New issues start as New. Update an existing status only when learning evidence supports the change; otherwise preserve it. Mastered requires sufficient evidence of independent, unprompted correct use. Frequency, copying, prompted repetition, or one isolated correct answer does not establish mastery.

## Counts, dates, and sources

Count the same problem at most once per conversation. Another conversation increases the count only when an independent question or unprompted response exposes the problem again. Copying, prompted repetition, annotations of the same original material, reposts, and repeated retrieval do not add occurrences, even across conversations. Useful new evidence from an already counted conversation may be appended without increasing the count. Correct use may inform status but does not add a problem occurrence.

A new entry with one countable conversation starts at 1. A retrospective collection with several distinct countable conversations uses their actual count. Compare new evidence with existing history before increasing the total. When source dates or duplication are unclear, do not count the uncertain evidence. Preserve existing totals whose history cannot be reconciled; do not replace them with the number found in the current run or assume every new candidate is additional.

Preserve First Observed unless verified earlier evidence is found. Update Last Observed using the latest supported actual occurrence date. Never substitute the collection date or database creation/edit time. Unknown dates remain unknown. For a precise time window, material whose eligibility cannot be established stays pending outside writes. For an approximate range, available time information and learning context may establish relevance without an exact date; this does not justify inventing a date or counting undated evidence.

Retain available source links, identifiers, and enough context to trace the evidence and assess duplication. Missing technical IDs alone do not disqualify clear original evidence. If duplication cannot be resolved, leave the affected addition pending. Do not reconstruct quotations from memory or invent dates, identifiers, or occurrence numbers.

## Entry body

Keep one Problem and one Explanation. Revise them when evidence supports a correction or clarification; preserve historical learner wording and manual notes. Append useful new evidence under Occurrences using this outline. A reliable occurrence number is optional; additional source detail is optional.

```markdown
## Problem
Specific difficulty and necessary context.

## Explanation
Correct usage or meaning applicable to that context.

## Occurrences
**YYYY-MM-DD**
- Original: [Question / diary / voice; necessary context and available source] Learner's words or question.
- Correct: Correction preserving the intended meaning, or the meaning for a vocabulary/comprehension question.
```

Localize the Original and Correct labels if useful. Use Date unknown when a date genuinely cannot be established and the evidence is otherwise eligible to append. Keep source text distinct from the page structure. Existing entries may use a different readable occurrence layout; preserve it when the same meaning and evidence can be maintained. Unclear structure or conflicting evidence calls for resolving the affected change, not replacing the whole page.

## Format changes

This format version is independent of the plugin release version. Check the actual database and affected entries before writing; a plugin upgrade alone does not migrate them. Compatible differences in presentation can be preserved. Changes to field meaning, counting, or required structure need an explicit specification update and a maintenance plan for existing records. Collection does not silently migrate incompatible records.
