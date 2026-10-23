# Data

## `processed/` — balanced datasets

Two-column CSV files with a header `smiles,label`:

- `smiles` — canonical SMILES of the compound.
- `label` — binary whole-cell activity: `1` = active (inhibitory), `0` = inactive.

| File | Pathogen | Active | Inactive | Total |
|---|---|---|---|---|
| `xanthomonas_oryzae.csv` | *Xanthomonas oryzae* | 1,007 | 1,007 | 2,014 |
| `magnaporthe_oryzae.csv` | *Magnaporthe oryzae* | 1,339 | 1,339 | 2,678 |
| `rhizoctonia_solani.csv` | *Rhizoctonia solani* | 1,138 | 1,138 | 2,276 |
| `three_pathogens.csv` | combined (multitask) | — | — | 4,647 |

## `raw/` — assay-level data with provenance

Seven-column CSV files with a header `smiles,label,value,type,organism,source,aid`:

- `value` — measured activity (e.g. IC50 in μM).
- `type` — assay measurement type (IC50, MIC, etc.).
- `organism` — pathogen the assay was run against.
- `source` — source database (`ChEMBL` or `PubChem`).
- `aid` — assay / record ID for traceability.

`dataset_summary.csv` records the activity thresholds, original and reclassified counts, and the balanced totals.

## Curation rules

- Whole-cell (not molecular target) assay labels only.
- Positives and negatives drawn from the same library.
- Generic / cross-species strains excluded.
- Activity thresholds: *X. oryzae* ≤ 0.4 μM; *M. oryzae* and *R. solani* ≤ 1.0 μM.
- Deduplicated by canonical SMILES; balanced ~1:1.
- No MIC/IC50 regression task — binary classification only.
