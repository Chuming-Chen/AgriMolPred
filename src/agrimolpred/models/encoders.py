# -*- coding: utf-8 -*-
"""Frozen multi-view molecular encoders.

TODO (code being finalized):
    1D (sequence): ChemBERTa-2, SmolBERT, MolFormer
    2D (graph):    MolBERT, MolCLR
    3D (conformer): Uni-Mol / 3D-MoLM
All encoders are used with frozen weights and projected to a common
embedding dimension before fusion.
"""
# TODO: import from transformers / torch_geometric and wrap each encoder.
