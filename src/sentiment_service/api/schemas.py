from pydantic import BaseModel, Field


class SentimentIn(BaseModel):
    text: str = Field(..., min_length=5, max_length=5_000)


class SentimentOut(BaseModel):
    prediction: (
        str  # "very positive" | "positive" | "neutral" | "negative" | "very negative"
    )
    score: float  # probability of the predicted class
