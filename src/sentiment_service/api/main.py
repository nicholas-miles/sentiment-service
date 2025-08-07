import pickle
from fastapi import FastAPI, HTTPException
from .schemas import SentimentIn, SentimentOut

with open(__file__.replace("api/main.py", "models/model.pkl"), "rb") as f:
    MODEL = pickle.load(f)

app = FastAPI(
    title="Sentiment-as-a-Service",
    version="0.1.0",
    contact={"name": "Nicholas Miles"},
)


@app.get("/")
def root():
    return {"message": "Sentiment Analysis API", "docs": "/docs"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=SentimentOut)
def predict(inp: SentimentIn):
    try:
        proba = MODEL.predict_proba([inp.text])[0]
    except Exception as e:  # pragma: no cover
        raise HTTPException(status_code=400, detail=str(e))
    idx = int(proba.argmax())
    return {
        "prediction": [
            "very negative",
            "negative",
            "neutral",
            "positive",
            "very positive",
        ][idx],
        "score": float(proba[idx]),
    }
