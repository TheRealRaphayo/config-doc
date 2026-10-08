> **SECTION TEMPLATE** — English version of `fr/_modele-section.md`. A new piece of
> equipment needs a file with the same name in `fr/` and in `en/`, and one row in `index.md`.
>
> - No passwords, client names or project names: make them `{{NAME}}` variables.
> - Use the same variable names as the French file; only the text is translated.
> - Markers are the same in both languages: `<!-- IF: condition -->` … `<!-- END IF -->`,
>   `<!-- INSTRUCTION: ... -->`, `<!-- IMAGE NEEDED: ... -->`.

# Manufacturer Model Configuration

**Reference firmware version:** (version validated for this procedure)
**Section last revised:** YYYY-MM-DD

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address | (standard address, or "none") |
| {{USERNAME}} / {{PASSWORD}} | Administrator account | none |

## Content

(One or two sentences: role of the equipment in the system.) The following items are covered in this section:

- (subsection)
- (subsection)

## Network configuration

1. (step)
2. (step)

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |

![Screenshot description](../../assets/images/manufacturer-model_subject.png)

<!-- IF: condition in plain words -->
## Optional subsection

1. (step)
<!-- END IF -->

## Notes

- (maintenance notes for the section; not copied into the document)
