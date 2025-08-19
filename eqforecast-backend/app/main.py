from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Optional

app = FastAPI(
    title="Earthquake Forecasting API",
    description="API for earthquake magnitude forecasting using Attention-LSTM models",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data for development (replace with actual ML model later)
MOCK_FORECAST_DATA = {
    "bins": [
        {"bin_id": 1, "max_magnitude": 4.2, "num_earthquakes": 15, "risk_level": "low"},
        {"bin_id": 2, "max_magnitude": 5.8, "num_earthquakes": 8, "risk_level": "medium"},
        {"bin_id": 3, "max_magnitude": 6.5, "num_earthquakes": 3, "risk_level": "high"},
        {"bin_id": 4, "max_magnitude": 7.2, "num_earthquakes": 1, "risk_level": "critical"}
    ]
}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Earthquake Forecasting API",
        "version": "1.0.0",
        "status": "active"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/forecast")
async def get_forecast(year: Optional[int] = None):
    """
    Get earthquake forecast for a specific year
    If no year provided, returns forecast for current year
    """
    if year is None:
        year = datetime.now().year
    
    # Mock forecast generation (replace with actual ML model later)
    forecast = {
        "year": year,
        "generated_at": datetime.now().isoformat(),
        "forecast_data": MOCK_FORECAST_DATA["bins"],
        "total_earthquakes": sum(bin["num_earthquakes"] for bin in MOCK_FORECAST_DATA["bins"]),
        "max_expected_magnitude": max(bin["max_magnitude"] for bin in MOCK_FORECAST_DATA["bins"])
    }
    
    return forecast

@app.get("/api/forecast/{bin_id}")
async def get_bin_forecast(bin_id: int):
    """Get detailed forecast for a specific bin"""
    if bin_id < 1 or bin_id > 4:
        raise HTTPException(status_code=400, detail="Bin ID must be between 1 and 4")
    
    bin_data = next((bin for bin in MOCK_FORECAST_DATA["bins"] if bin["bin_id"] == bin_id), None)
    
    if not bin_data:
        raise HTTPException(status_code=404, detail="Bin not found")
    
    # Mock detailed analysis for the bin
    detailed_forecast = {
        **bin_data,
        "location": f"Philippines Region {bin_id}",
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

@app.get("/api/historical-data")
async def get_historical_data(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    min_magnitude: Optional[float] = None,
    max_magnitude: Optional[float] = None
):
    """
    Get historical earthquake data with optional filters
    Date format: YYYY-MM-DD
    """
    # Mock historical data (replace with actual PHIVOLCS data)
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
    
    return {
        "data": filtered_data,
        "total_count": len(filtered_data),
        "filters_applied": {
            "start_date": start_date,
            "end_date": end_date,
            "min_magnitude": min_magnitude,
            "max_magnitude": max_magnitude
        }
    }

@app.get("/api/regions")
async def get_regions():
    """Get available regions/bins for forecasting"""
    return {
        "regions": [
            {
                "bin_id": 1,
                "name": "Northern Luzon",
                "coordinates": {"lat": 16.5, "lng": 120.5},
                "description": "Baguio, La Union, Ilocos region"
            },
            {
                "bin_id": 2,
                "name": "Central Luzon",
                "coordinates": {"lat": 15.1, "lng": 120.6},
                "description": "Angeles, Pampanga, Tarlac region"
            },
            {
                "bin_id": 3,
                "name": "Metro Manila",
                "coordinates": {"lat": 14.6, "lng": 121.0},
                "description": "Manila, Quezon City, surrounding areas"
            },
            {
                "bin_id": 4,
                "name": "Southern Philippines",
                "coordinates": {"lat": 7.1, "lng": 125.6},
                "description": "Davao, Mindanao region"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )