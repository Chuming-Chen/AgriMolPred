# -*- coding: utf-8 -*-
"""Dataset utilities for AgriMolPred.

TODO (code being finalized):
    - load a `smiles,label` CSV into a torch Dataset
    - canonicalize SMILES with RDKit
    - build 1D / 2D / 3D inputs for each molecule
    - scaffold split (Bemis-Murcko) with StratifiedKFold
"""
import pandas as pd


def load_dataset(csv_path, smiles_col="smiles", label_col="label"):
    """Load a balanced SMILES+label dataset."""
    df = pd.read_csv(csv_path)
    return df[[smiles_col, label_col]].dropna()


# TODO: implement SmilesDataset, scaffold_split, kfold indices.
