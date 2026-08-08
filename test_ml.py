import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import compute_model_metrics, inference, train_model


def test_train_model():
    """
    Test the train_model function.
    """
    X_train = np.array(
        [
            [0, 1],
            [1, 0],
            [1, 1],
            [0, 0],
        ]
    )
    y_train = np.array([0, 1, 1, 0])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


def test_inference():
    """
    Test the inference function.
    """
    X_train = np.array(
        [
            [0, 1],
            [1, 0],
            [1, 1],
            [0, 0],
        ]
    )
    y_train = np.array([0, 1, 1, 0])

    model = train_model(X_train, y_train)
    predictions = inference(model, X_train)

    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == len(X_train)


def test_compute_model_metrics():
    """
    Test the compute_model_metrics function.
    """
    y = np.array([1, 0, 1, 1])
    predictions = np.array([1, 0, 1, 0])

    precision, recall, fbeta = compute_model_metrics(y, predictions)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= fbeta <= 1.0
