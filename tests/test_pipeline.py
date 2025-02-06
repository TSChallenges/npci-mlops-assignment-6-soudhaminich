import sys
import os
import pandas as pd
import joblib
import pytest

# Ensure Python can find train_model.py in the project root
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def test_preprocessing():
    """Tests whether the preprocessing script runs without errors."""
    try:
        df = pd.read_csv("data/processed_data.csv")
        assert not df.isnull().sum().any(), "Preprocessed data has missing values!"
        assert 'y' in df.columns, "Target variable missing!"
    except Exception as e:
        pytest.fail(f"Preprocessing test failed: {e}")

def test_model_training():
    """Tests if the model is successfully trained."""
    try:
        model = joblib.load("models/bank_model.pkl")
        assert model is not None, "Model failed to train!"
    except Exception as e:
        pytest.fail(f"Model training test failed: {e}")
