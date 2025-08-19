"""
Main FastAPI application for Earthquake Forecasting API
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional, List

# Import our modules
from app.config import settings
from app.database import get_db, init_db, Earthquake, Forecast
from app.api.schemas import (
    ForecastResponse, 
    BinForecast, 
    EarthquakeData, 
    RegionInfo,
    HistoricalDataResponse
)

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="API for earthquake magnitude forecasting using Attention-LSTM models",
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data for development (will be replaced with real ML model)
MOCK_FORECAST_DATA = {
    "bins": [
        {"bin_id": 1, "max_magnitude": 4.2, "num_earthquakes": 15, "risk_level": "low"},
        {"bin_id": 2, "max_magnitude": 5.8, "num_earthquakes": 8, "risk_level": "medium"},
        {"bin_id": 3, "max_magnitude": 6.5, "num_earthquakes": 3, "risk_level": "high"},
        {"bin_id": 4, "max_magnitude": 7.2, "num_earthquakes": 1, "risk_level": "critical"}
    ]
}

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "active",
        "docs": "/docs"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy", 
        "timestamp": datetime.now().isoformat(),
        "version": settings.APP_VERSION
    }

# API endpoints
@app.get("/api/forecast", response_model=ForecastResponse)
async def get_forecast(
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    Get earthquake forecast for a specific year
    If no year provided, returns forecast for current year
    """
    if year is None:
        year = datetime.now().year
    
    if year < 2020 or year > 2030:
        raise HTTPException(status_code=400, detail="Year must be between 2020 and 2030")
    
    # TODO: Replace with actual ML model prediction
    # For now, use mock data
    forecast_data = []
    for bin_data in MOCK_FORECAST_DATA["bins"]:
        forecast_data.append(BinForecast(
            bin_id=bin_data["bin_id"],
            max_magnitude=bin_data["max_magnitude"],
            num_earthquakes=bin_data["num_earthquakes"],
            risk_level=bin_data["risk_level"],
            confidence_level=0.85,
            location=settings.GEOGRAPHIC_BINS[bin_data["bin_id"]]["name"]
        ))
    
    return ForecastResponse(
        year=year,
        generated_at=datetime.now(),
        forecast_data=forecast_data,
        total_earthquakes=sum(bin["num_earthquakes"] for bin in MOCK_FORECAST_DATA["bins"]),
        max_expected_magnitude=max(bin["max_magnitude"] for bin in MOCK_FORECAST_DATA["bins"]),
        confidence_score=0.82,
        model_version="1.0.0",
        data_source=settings.DATA_SOURCE
    )

@app.get("/api/forecast/{bin_id}")
async def get_bin_forecast(
    bin_id: int,
    db: Session = Depends(get_db)
):
    """Get detailed forecast for a specific bin"""
    if bin_id < 1 or bin_id > 4:
        raise HTTPException(status_code=400, detail="Bin ID must be between 1 and 4")
    
    bin_data = next((bin for bin in MOCK_FORECAST_DATA["bins"] if bin["bin_id"] == bin_id), None)
    
    if not bin_data:
        raise HTTPException(status_code=404, detail="Bin not found")
    
    # Get bin info from settings
    bin_info = settings.GEOGRAPHIC_BINS[bin_id]
    
    # Mock detailed analysis for the bin
    detailed_forecast = {
        **bin_data,
        "location": bin_info["name"],
        "confidence_level": 0.85,
        "historical_pattern": "Increasing seismic activity",
        "recommendations": [
            "Monitor seismic activity closely",
            "Review emergency preparedness plans",
            "Conduct safety inspections"
        ] if bin_data["risk_level"] in ["high", "critical"] else [
            "Continue routine monitoring",
            "Maintain standard safety protocols"
        ]
    }
    
    return detailed_forecast

@app.get("/api/historical-data", response_model=HistoricalDataResponse)
async def get_historical_data(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    min_magnitude: Optional[float] = None,
    max_magnitude: Optional[float] = None,
    bin_id: Optional[int] = None,
    limit: Optional[int] = 100,
    db: Session = Depends(get_db)
):
    """
    Get historical earthquake data with optional filters
    Date format: YYYY-MM-DD
    """
    # TODO: Replace with actual database query
    # For now, return mock data
    mock_historical = [
        {
            "id": 1,
            "date": "2023-12-01T10:30:00",
            "latitude": 14.5995,
            "longitude": 120.9842,
            "depth": 10.5,
            "magnitude": 4.2,
            "location": "Manila, Philippines",
            "bin_id": 1
        },
        {
            "id": 2,
            "date": "2023-12-05T15:45:00",
            "latitude": 16.4023,
            "longitude": 120.5960,
            "depth": 25.0,
            "magnitude": 5.8,
            "location": "Baguio, Philippines",
            "bin_id": 2
        },
        {
            "id": 3,
            "date": "2023-12-10T08:15:00",
            "latitude": 15.1448,
            "longitude": 120.5974,
            "depth": 15.2,
            "magnitude": 6.1,
            "location": "Angeles, Philippines",
            "bin_id": 3
        }
    ]
    
    # Apply filters (simplified for now)
    filtered_data = mock_historical
    
    if min_magnitude:
        filtered_data = [eq for eq in filtered_data if eq["magnitude"] >= min_magnitude]
    
    if max_magnitude:
        filtered_data = [eq for eq in filtered_data if eq["magnitude"] <= max_magnitude]
    
    if bin_id:
        filtered_data = [eq for eq in filtered_data if eq["bin_id"] == bin_id]
    
    # Apply limit
    filtered_data = filtered_data[:limit]
    
    return HistoricalDataResponse(
        data=filtered_data,
        total_count=len(filtered_data),
        filters_applied={
            "start_date": start_date,
            "end_date": end_date,
            "min_magnitude": min_magnitude,
            "max_magnitude": max_magnitude,
            "bin_id": bin_id,
            "limit": limit
        }
    )

@app.get("/api/regions")
async def get_regions():
    """Get available regions/bins for forecasting"""
    regions = []
    for bin_id, bin_info in settings.GEOGRAPHIC_BINS.items():
        regions.append(RegionInfo(
            bin_id=bin_id,
            name=bin_info["name"],
            coordinates=bin_info["coordinates"],
            description=bin_info["description"]
        ))
    
    return {"regions": regions}

@app.get("/api/stats")
async def get_statistics(db: Session = Depends(get_db)):
    """Get API and data statistics"""
    # TODO: Add real statistics from database
    return {
        "total_earthquakes": 0,  # Will be replaced with actual count
        "total_forecasts": 0,     # Will be replaced with actual count
        "last_update": datetime.now().isoformat(),
        "data_source": settings.DATA_SOURCE,
        "model_version": "1.0.0"
    }

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "timestamp": datetime.now().isoformat(),
            "status_code": exc.status_code
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )