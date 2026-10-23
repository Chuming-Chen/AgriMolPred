# -*- coding: utf-8 -*-
"""Evaluation metrics for AgriMolPred.

TODO (code being finalized):
    AUC, AUPRC, sensitivity, specificity, MCC, F1;
    mean/std aggregation over cross-validation folds.
"""
from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    matthews_corrcoef,
    f1_score,
)


def compute_metrics(y_true, y_pred, y_score):
    """Return the six standard metrics for one fold."""
    return {
        "AUC": roc_auc_score(y_true, y_score),
        "AUPRC": average_precision_score(y_true, y_score),
        "MCC": matthews_corrcoef(y_true, y_pred),
        "F1": f1_score(y_true, y_pred),
    }
