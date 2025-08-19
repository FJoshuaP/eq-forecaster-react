from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import logging
import os
from dotenv import load_dotenv

# Import our modules
from models.earthquake_model import EarthquakePredictor
from schemas.earthquake import EarthquakeData, PredictionRequest, PredictionResponse
from services.data_service import DataService
from services.prediction_service import PredictionService

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Earthquake Forecasting API",
    description="API for earthquake magnitude prediction using Attention-LSTM model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
data_service = DataService()
prediction_service = PredictionService()

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    try:
        logger.info("Initializing earthquake forecasting services...")
        # Initialize the ML model
        await prediction_service.initialize_model()
        logger.info("Services initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")
        raise

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Earthquake Forecasting API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

@app.get("/api/regions")
async def get_regions():
    """Get available Philippine regions for earthquake forecasting"""
    try:
        regions = data_service.get_philippine_regions()
        return {"regions": regions}
    except Exception as e:
        logger.error(f"Error fetching regions: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch regions")

@app.get("/api/earthquakes")
async def get_earthquakes(
    region: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    min_magnitude: Optional[float] = None,
    max_magnitude: Optional[float] = None,
    limit: int = 100
):
    """Get historical earthquake data with optional filters"""
    try:
        earthquakes = await data_service.get_earthquakes(
            region=region,
            start_date=start_date,
            end_date=end_date,
            min_magnitude=min_magnitude,
            max_magnitude=max_magnitude,
            limit=limit
        )
        return {"earthquakes": earthquakes, "count": len(earthquakes)}
    except Exception as e:
        logger.error(f"Error fetching earthquakes: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch earthquake data")

@app.post("/api/predict", response_model=PredictionResponse)
async def predict_earthquake(request: PredictionRequest):
    """Predict earthquake magnitude for a given region and time period"""
    try:
        prediction = await prediction_service.predict_magnitude(request)
        return prediction
    except Exception as e:
        logger.error(f"Error making prediction: {e}")
        raise HTTPException(status_code=500, detail="Failed to make prediction")

@app.get("/api/statistics")
async def get_statistics(region: Optional[str] = None):
    """Get statistical information about earthquake data"""
    try:
        stats = await data_service.get_statistics(region=region)
        return stats
    except Exception as e:
        logger.error(f"Error fetching statistics: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch statistics")

@app.get("/api/model-info")
async def get_model_info():
    """Get information about the trained ML model"""
    try:
        model_info = prediction_service.get_model_info()
        return model_info
    except Exception as e:
        logger.error(f"Error fetching model info: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch model info")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )