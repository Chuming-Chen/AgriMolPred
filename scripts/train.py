# -*- coding: utf-8 -*-
"""AgriMolPred training entry point.

TODO (code being finalized):
    python scripts/train.py --data data/processed/three_pathogens.csv \
                           --config configs/default.yaml
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Train AgriMolPred")
    parser.add_argument("--data", default="data/processed/three_pathogens.csv")
    parser.add_argument("--config", default="configs/default.yaml")
    args = parser.parse_args()
    # TODO: build encoders -> fusion -> capsule, train, save checkpoint.
    raise NotImplementedError("Training code is being finalized.")


if __name__ == "__main__":
    main()
