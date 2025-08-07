import mlflow
import pytest

from sentiment_service.training.train import train_model


def test_train_model():
    """Test that the training function works and returns a model."""
    # Disable MLflow logging for tests
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    with mlflow.start_run():
        model = train_model()
        assert model is not None
        # Test that the model can make predictions
        predictions = model.predict(["This is a test"])
        assert len(predictions) == 1
        assert predictions[0] in [0, 1, 2, 3, 4]  # 5-class classification


def test_model_predict_proba():
    """Test that the model can return probability predictions."""
    # Disable MLflow logging for tests
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    with mlflow.start_run():
        model = train_model()
        proba = model.predict_proba(["This is a test"])
        assert proba.shape == (1, 5)  # 1 sample, 5 classes
        assert proba.sum() == pytest.approx(1.0, abs=1e-6)  # Probabilities sum to 1
