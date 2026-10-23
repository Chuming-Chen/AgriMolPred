# AgriMolPred: Multi-Source Molecular Foundation Models Fused with a Dynamic-Routing Capsule Network for Rice Pathogen Inhibitor Prediction

AgriMolPred is a deep-learning framework for **agricultural antimicrobial discovery**. Given a single compound as a canonical **SMILES** string, it encodes the molecule from three complementary molecular views — **1D SMILES sequence**, **2D molecular graph**, and **3D conformer** — using a battery of frozen molecular foundation models, fuses the views through pairwise cross-attention and a gated cross-fusion module, and then routes the unified embedding through a **capsule network** to predict, for each rice pathogen, whether the compound is **active** (inhibitory) or **inactive**. Every prediction is accompanied by a **SHAP** explanation that attributes the decision to atoms and representations, and high-confidence candidates are further validated by **molecular docking** and binding-pocket analysis.

> **Status:** the repository skeleton, curated datasets, and figures are released. The training/inference code is being finalized and will be added under `src/agrimolpred/` and `scripts/`.

## Highlights

- **Multi-view molecular encoders.** Six frozen foundation models cover three views:
  - **1D (sequence):** ChemBERTa-2, SmolBERT, MolFormer
  - **2D (graph):** MolBERT, MolCLR
  - **3D (conformer):** Uni-Mol / 3D-MoLM
- **Hierarchical cross-fusion.** Stage 1 performs pairwise multi-head cross-attention (1D×2D → f₁₂; 2D×3D → f₂₃); Stage 2 applies a gated cross-fusion of f₁₂ and f₂₃ into one unified embedding.
- **Capsule classifier.** PrimaryCaps (p1–p6) → dynamic routing → ClassCaps, with one exclusive binary head per pathogen.
- **Interpretable and closed-loop.** SHAP attribution at the representation and atom level, followed by 3D docking and binding-pocket characterization.
- **Curated, traceable data.** Whole-cell labels from ChEMBL and PubChem; positives and negatives drawn from the same library; no generic/cross-species strains; balanced ~1:1.

## Repository Structure

```
AgriMolPred/
├── README.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── data/
│   ├── README.md
│   ├── processed/                 # balanced SMILES + label datasets
│   │   ├── xanthomonas_oryzae.csv
│   │   ├── magnaporthe_oryzae.csv
│   │   ├── rhizoctonia_solani.csv
│   │   └── three_pathogens.csv
│   └── raw/                       # assay-level data with provenance (assay ID)
│       ├── xanthomonas_oryzae_assay.csv
│       ├── magnaporthe_oryzae_assay.csv
│       ├── rhizoctonia_solani_assay.csv
│       └── dataset_summary.csv
├── configs/
│   └── default.yaml               # model & training configuration
├── src/
│   └── agrimolpred/
│       ├── __init__.py
│       ├── data/                  # dataset / scaffold-split utilities
│       ├── models/                # encoders, cross-fusion, capsule network
│       └── utils/                 # metrics, SHAP helpers
├── scripts/
│   ├── train.py                   # training entry point (TODO)
│   └── predict.py                 # inference entry point (TODO)
├── checkpoints/                   # saved model weights (TODO)
├── figures/
│   ├── Figure1.png                # overview figure (landscape)
│   └── Figure1_A4_4panels.pptx    # editable A4 4-panel figure
└── docs/
```

## Environment Setup

### Core dependencies

- Python 3.9
- PyTorch 2.0+
- PyTorch Geometric (for graph encoders)
- Transformers / HuggingFace (for 1D and 3D foundation models)
- RDKit (SMILES canonicalization, atom-level features)
- scikit-learn (scaffold splits, metrics)
- SHAP (attribution)
- AutoDock Vina / related tools (optional, for docking)

### Installation

```bash
conda env create -f environment.yml
conda activate agrimolpred
# or
pip install -r requirements.txt
```

## Data

Each processed dataset is a two-column CSV (`smiles`, `label`), where `label = 1` denotes active and `label = 0` inactive. The `raw/` files additionally retain the measured value, assay type, source database, and assay ID for full provenance.

| Pathogen (disease) | Activity threshold | Original | Reclassified (+/−) | Balanced (+/−) |
|---|---|---|---|---|
| *Xanthomonas oryzae* (bacterial blight) | ≤ 0.4 μM | 6,506 | 5,499 / 1,007 | 1,007 / 1,007 |
| *Magnaporthe oryzae* (rice blast) | ≤ 1.0 μM | 5,060 | 3,721 / 1,339 | 1,339 / 1,339 |
| *Rhizoctonia solani* (sheath blight) | ≤ 1.0 μM | 2,749 | 1,138 / 1,611 | 1,138 / 1,138 |

## Quick Start

```bash
# Prediction (interface to be finalized)
python scripts/predict.py --smiles "CCO"

# Training (interface to be finalized)
python scripts/train.py --data data/processed/three_pathogens.csv \
                        --config configs/default.yaml
```

## Citation

If you use AgriMolPred or its datasets, please cite the accompanying manuscript (citation details to be updated upon publication).

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
