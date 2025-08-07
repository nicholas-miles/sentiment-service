import hashlib
import pickle

import mlflow
from sklearn.datasets import fetch_openml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline


def train_model():
    """
    Train a sentiment analysis model using the SST-5 dataset.
    Returns the trained model pipeline.
    """
    mlflow.set_experiment("sentiment-analysis")
    mlflow.sklearn.autolog(
        log_datasets=False
    )  # Disable dataset logging to avoid Series warning

    sst5 = fetch_openml("sst5")
    X = sst5.data["text"]
    y = sst5.target.map(
        {
            "very negative": 0,
            "negative": 1,
            "neutral": 2,
            "positive": 3,
            "very positive": 4,
        }
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipe = make_pipeline(
        TfidfVectorizer(),
        LogisticRegression(
            multi_class="multinomial",
            class_weight="balanced",
        ),
    )
    pipe.fit(X_train, y_train)

    print(classification_report(y_val, pipe.predict(X_val)))

    model_path = "src/sentiment_service/models/model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(pipe, f)

    sha = hashlib.sha1(open(model_path, "rb").read()).hexdigest()[:8]
    mlflow.log_param("model_sha", sha)
    print(f"[✓] model saved ➜ {model_path} (sha:{sha})")

    return pipe


def main() -> None:
    """
    Train a sentiment analysis model using the SST-5 dataset.
    """
    train_model()


if __name__ == "__main__":
    main()
