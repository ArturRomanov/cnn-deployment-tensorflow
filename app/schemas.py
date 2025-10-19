from pydantic import BaseModel, Field
from typing import List

class PredictionsResponse(BaseModel):
    probabilities: List[float] = Field(frozen=True)