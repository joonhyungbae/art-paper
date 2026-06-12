# Citation Format Switcher — Multi-Citation Format Switching

Quick-reference for switching between citation formats. Used by `citation_compliance_agent` and `formatter_agent`.

> **Default for art-paper: ACM Reference Format** (SIGGRAPH Asia / ACM Digital Library), wired to the `acmart` document class. See `shared/references/acm_reference_format.md`. The formats below (APA 7, Chicago, MLA 9, IEEE, Vancouver) are **supported alternates** for non-ACM venues; they are not the default. The "APA → X" conversion recipes below predate the fork and are retained for alternate-to-alternate conversion; for the common art-paper case, convert *from ACM* to an alternate (or vice versa) using the same field mappings.

### ACM Reference Format (DEFAULT)
**Venue**: SIGGRAPH Asia / ACM Digital Library and adjacent art-and-technology venues.

**In-text**: class-driven — `acmart` `sigconf` renders numeric `[1]`; journal classes (`acmsmall`/`acmtog`) render author-year `[Smith 2024]`. Do not hand-format; use `\cite`/`\citet`/`\citep` and let the class decide.

**Conference paper / journal article** (BibTeX → `ACM-Reference-Format.bst`):
```
Jane A. Smith and Betty C. Jones. 2024. Article or work title.
    In Proceedings of ... (or Journal Name) 45, 2 (2024), 123-145.
    https://doi.org/10.1145/xxxxxxx
```

**Artwork / exhibition** (art-paper specific — cite the work as a source; NO fabricated DOI):
```
Artist Name. 2023. Work Title. Medium / installation.
    Exhibited at [Venue], [City]. https://www.example.org/work
```

**Key rules**: artwork citations use venue+date as the L3 locator (not a DOI); never invent DOIs for artworks; let the `acmart` class option drive numeric vs. author-year rendering.

---

## Format Comparison Matrix

### In-Text Citation Patterns

| Scenario | APA 7th | Chicago (Notes) | Chicago (Author-Date) | MLA 9th | IEEE | Vancouver |
|----------|---------|-----------------|----------------------|---------|------|-----------|
| Single author | (Smith, 2024) | ¹ (footnote) | (Smith 2024) | (Smith 45) | [1] | ¹ (superscript) |
| Two authors | (Smith & Jones, 2024) | ¹ | (Smith and Jones 2024) | (Smith and Jones 45) | [1] | ¹ |
| 3+ authors | (Smith et al., 2024) | ¹ | (Smith et al. 2024) | (Smith et al. 45) | [1] | ¹ |
| Direct quote | (Smith, 2024, p. 45) | ¹ | (Smith 2024, 45) | (Smith 45) | [1, p. 45] | ¹⁽ᵖ⁴⁵⁾ |
| Multiple works | (Chen, 2023; Smith, 2024) | ¹ ² | (Chen 2023; Smith 2024) | (Chen 12; Smith 45) | [1], [2] | ¹˒² |
| Order | Alphabetical | Order of appearance | Alphabetical | Alphabetical | Order of appearance | Order of appearance |

### Reference List Naming

| Format | Section Title | Entry Order |
|--------|--------------|-------------|
| APA 7th | References | Alphabetical |
| Chicago (Notes) | Bibliography | Alphabetical |
| Chicago (Author-Date) | References | Alphabetical |
| MLA 9th | Works Cited | Alphabetical |
| IEEE | References | Order of appearance |
| Vancouver | References | Order of appearance |

## Format Details

### APA 7th Edition
**Discipline**: Education, Psychology, Social Sciences

**Journal Article**:
```
Smith, J. A., & Jones, B. C. (2024). Article title in sentence case.
    Journal Title in Title Case, 45(2), 123-145. https://doi.org/10.xxxx
```

**Book**:
```
Smith, J. A. (2024). Book title in sentence case (2nd ed.). Publisher.
```

**Key rules**: Hanging indent, DOI as URL, sentence case for titles, "&" before last author.

---

### Chicago 17th (Notes-Bibliography)
**Discipline**: History, Humanities, some Social Sciences

**Footnote (first citation)**:
```
1. John A. Smith and Betty C. Jones, "Article Title in Title Case,"
Journal Title 45, no. 2 (2024): 123, https://doi.org/10.xxxx.
```

**Footnote (subsequent)**:
```
2. Smith and Jones, "Article Title," 130.
```

**Bibliography entry**:
```
Smith, John A., and Betty C. Jones. "Article Title in Title Case."
    Journal Title 45, no. 2 (2024): 123-145.
    https://doi.org/10.xxxx.
```

**Key rules**: Full names, title case throughout, footnotes + bibliography, period after URL.

---

### Chicago 17th (Author-Date)
**Discipline**: Natural Sciences, some Social Sciences

**In-text**: (Smith 2024, 45)

**Reference**:
```
Smith, John A. 2024. "Article Title in Title Case." Journal Title
    45 (2): 123-145. https://doi.org/10.xxxx.
```

**Key rules**: Year after author name, full names in reference, title case.

---

### MLA 9th Edition
**Discipline**: Literature, Languages, Cultural Studies

**In-text**: (Smith 45) — author + page, no comma, no year

**Works Cited**:
```
Smith, John A., and Betty C. Jones. "Article Title in Title Case."
    Journal Title, vol. 45, no. 2, 2024, pp. 123-45.
```

**Key rules**: No year in in-text, page numbers always, containers model, no DOI in basic format (include if online), title case for all titles.

---

### IEEE
**Discipline**: Engineering, Computer Science, Technology

**In-text**: [1] — numbered brackets in order of appearance

**Reference**:
```
[1] J. A. Smith and B. C. Jones, "Article title in sentence case,"
    Journal Title, vol. 45, no. 2, pp. 123-145, Feb. 2024,
    doi: 10.xxxx.
```

**Key rules**: Numbered [N], initials before surname, abbreviated month, "doi:" prefix (not URL).

---

### Vancouver
**Discipline**: Medicine, Biomedical Sciences, Nursing

**In-text**: Superscript numbers ¹ or (1) in order of appearance

**Reference**:
```
1. Smith JA, Jones BC. Article title in sentence case. Journal Title.
   2024;45(2):123-145. doi:10.xxxx
```

**Key rules**: Numbered in order of appearance, no spaces in initials, abbreviated journal titles (per NLM), semicolon before volume, colon before pages.

## Conversion Quick Reference

### APA → Chicago (Notes-Bibliography)
1. Change in-text (Author, Year) → footnotes
2. Expand first names in reference list
3. Change sentence case → title case for article titles
4. Add period after URLs
5. Rename "References" → "Bibliography"

### APA → MLA
1. Remove years from in-text, add page numbers
2. Expand first names, change "&" → "and"
3. Change format: vol., no., year order
4. Remove DOIs (unless online-only source)
5. Rename "References" → "Works Cited"

### APA → IEEE
1. Change (Author, Year) → [N] numbered brackets
2. Reorder references by appearance (not alphabetical)
3. Change to initials-first format
4. Add "doi:" prefix to DOIs
5. Abbreviate month names

### APA → Vancouver
1. Change (Author, Year) → superscript numbers
2. Reorder references by appearance
3. Remove spaces between initials
4. Abbreviate journal titles (NLM catalog)
5. Use semicolons/colons for volume/page separators

## AI-Generated Content Citation (by Format)

| Format | How to Cite AI |
|--------|---------------|
| APA 7th | OpenAI. (2024). ChatGPT (Version 4) [Large language model]. https://chat.openai.com |
| Chicago | OpenAI. ChatGPT. Version 4. 2024. Large language model. https://chat.openai.com. |
| MLA | "ChatGPT response to [prompt description]." OpenAI, 15 Mar. 2024, chat.openai.com. |
| IEEE | [N] OpenAI, "ChatGPT," ver. 4, 2024. [Online]. Available: https://chat.openai.com |
| Vancouver | OpenAI. ChatGPT [Large language model]. 2024. Available from: https://chat.openai.com |
