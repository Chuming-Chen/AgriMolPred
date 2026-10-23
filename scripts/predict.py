# -*- coding: utf-8 -*-
"""AgriMolPred inference entry point.

TODO (code being finalized):
    python scripts/predict.py --smiles "CCO"
    python scripts/predict.py --input-csv molecules.csv --output batch.json
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Predict with AgriMolPred")
    parser.add_argument("--smiles", default=None, help="canonical SMILES")
    parser.add_argument("--input-csv", default=None, help="batch SMILES CSV")
    parser.add_argument("--checkpoint", default="checkpoints/agrimolpred.pth")
    parser.add_argument("--output", default=None, help="output JSON path")
    args = parser.parse_args()
    # TODO: encode -> fuse -> capsule head per pathogen, return active/inactive
    # and scores with SHAP attribution.
    raise NotImplementedError("Inference code is being finalized.")


if __name__ == "__main__":
    main()
