from .model import Model
from fastapi import FastAPI, UploadFile, HTTPException, File
from .schemas import PredictionsResponse

model = Model()

app = FastAPI()

@app.post("/predict", response_model=PredictionsResponse, tags=["Inference"])
async def predict(file: UploadFile = File(...)):
    if file.content_type not in {"image/jpeg", "image/png"}:
        raise HTTPException(status_code=415, detail="Only JPEG/PNG images are supported")
    try:
        image_bytes = await file.read()
        tensor = model.preprocess_image(image_bytes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Image could not be preprocessed: {e}")
    try:
        probabilities = model.predict(tensor)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Response could not be generated: {e}")
    return PredictionsResponse(probabilities=probabilities)

@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy"
    }

def start_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)