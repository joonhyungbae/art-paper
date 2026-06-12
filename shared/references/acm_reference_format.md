# ACM Reference Format — Citation Reference for art-paper

Replaces APA 7.0 as the **default** citation format for art-paper. Consumed by `art-paper` (`citation_compliance_agent`, `formatter_agent`) and the `citation-check` mode. Targets the ACM `acmart` document class (the standard SIGGRAPH Asia / ACM template, obtained from CTAN or the ACM).

> SIGGRAPH Asia / ACM venues require the **ACM Reference Format**. The genre-neutral L3 citation-faithfulness gate (three-layer emission, contamination/triangulation signals) is unchanged — only the *rendered format* differs from ARS.

---

## 1. Toolchain (ACM `acmart` package)

art-paper targets the ACM `acmart` document class as its output format. `acmart` is the standard ACM/SIGGRAPH template; authors install it from CTAN or obtain it from the ACM. The package provides:

| File | Purpose |
|---|---|
| `acmart.cls` | the ACM document class |
| `ACM-Reference-Format.bst` | BibTeX style for ACM Reference Format |
| `acmnumeric.bbx` / `acmnumeric.cbx` | biblatex numeric style |
| `acmauthoryear.bbx` / `acmauthoryear.cbx` | biblatex author-year style |
| `acmdatamodel.dbx` | biblatex data model |
| `samples/` | `sample-sigconf.tex`, `sample-acmsmall.tex`, etc. — working templates |
| `Makefile` | build targets |

## 2. BibTeX path (default)

```latex
\documentclass[sigconf]{acmart}   % class option = CFP-verified; sigconf is the default
...
\bibliographystyle{ACM-Reference-Format}
\bibliography{refs}               % refs.bib in BibTeX format
```

- In-text citations use `\cite{}`, `\citet{}`, `\citep{}` (acmart loads `natbib`).
- Default acmart numbering for `sigconf` is **numeric** ([1], [2]); journal classes (`acmsmall`/`acmtog`) default to **author-year**. The class option drives this — do not hand-format the rendered citation.

## 3. biblatex path (alternate)

```latex
\documentclass[sigconf,natbib=false]{acmart}
\usepackage[style=acmnumeric]{biblatex}   % or acmauthoryear
\addbibresource{refs.bib}
...
\printbibliography
```

## 4. `.bib` entry conventions for art papers

ACM Reference Format covers standard types; art papers lean on a few that ARS rarely used. Always populate enough fields for the L3 locator gate:

```bibtex
@inproceedings{key,        % conference / SIGGRAPH-type
  author    = {Last, First and Last, First},
  title     = {{Work or Paper Title}},
  booktitle = {Proceedings of ...},
  year      = {2024},
  doi       = {10.1145/...},
}

@article{key,              % journal incl. Leonardo
  author  = {Last, First},
  title   = {{Title}},
  journal = {Leonardo},
  volume  = {57}, number = {3}, pages = {...},
  year    = {2024},
  doi     = {10.1162/...},
}

@misc{artwork_key,         % an artwork / exhibition (art-paper specific)
  author       = {Artist, Name},
  title        = {{Work Title}},
  howpublished = {Medium / installation. Exhibited at {Venue}, {City}},
  year         = {2023},
  note         = {Accessed: 2026-05-22},
  url          = {...},
}

@online{web_key,           % online media, repos, documentation
  author = {...}, title = {{...}}, year = {2024},
  url = {...}, urldate = {2026-05-22},
}
```

**Artwork citations** (the genre-specific case): cite the work like a source — artist, title, year, medium, exhibition venue. Do NOT invent DOIs for artworks; use `@misc`/`@online` with `note`/`url` + access date. This is the locator channel the L3 gate checks.

## 5. Locator discipline (L3 gate, unchanged)

The art-paper three-layer citation emission still requires a locator anchor (`quote` / `page` / `section` / `paragraph` / `none`) after each `<!--ref:slug-->`. For artworks/exhibitions the natural locator is the **venue+date** or a timestamp into documentation media — encode it the same way. A citation with NO locator is still hard-gate-refused by the formatter.

## 6. citation-check mode output

The `citation-check` mode reports, per reference: (a) format compliance with ACM Reference Format, (b) BibTeX field completeness for its entry type, (c) L3 locator presence, (d) contamination/triangulation advisory signals (unchanged). Artwork/exhibition entries are checked for real-venue plausibility instead of DOI resolution.

## 7. What changes vs. ARS

| ARS | art-paper |
|---|---|
| `\bibliographystyle{apalike}`, apa7 class | `\bibliographystyle{ACM-Reference-Format}`, acmart class |
| APA in-text (Author, Year) as the rule | acmart class option decides numeric vs author-year |
| extended APA guides as default | retained as non-default fallback; ACM is default |
| DOI resolution as the verification spine | DOI for papers; **venue+date plausibility** for artworks |
