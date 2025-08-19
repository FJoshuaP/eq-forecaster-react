from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
import uvicorn
import logging
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Earthquake Forecasting API",
    description="API for earthquake data and forecasting system",
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

# Sample data for development
SAMPLE_EARTHQUAKES = [
    {
        "id": "EQ_001",
        "timestamp": "2024-01-15T10:30:00Z",
        "latitude": 14.5995,
        "longitude": 120.9842,
        "depth": 45.2,
        "magnitude": 4.5,
        "region": "NCR",
        "location_description": "Manila Bay Area",
        "source": "PHIVOLCS"
    },
    {
        "id": "EQ_002",
        "timestamp": "2024-01-14T15:20:00Z",
        "latitude": 16.4023,
        "longitude": 120.5960,
        "depth": 67.8,
        "magnitude": 3.8,
        "region": "CAR",
        "location_description": "Baguio City Area",
        "source": "PHIVOLCS"
    },
    {
        "id": "EQ_003",
        "timestamp": "2024-01-13T08:45:00Z",
        "latitude": 13.7563,
        "longitude": 121.0583,
        "depth": 23.4,
        "magnitude": 5.2,
        "region": "Region IV-A",
        "location_description": "Laguna Lake Area",
        "source": "PHIVOLCS"
    }
]

PHILIPPINE_REGIONS = [
    {"name": "NCR", "code": "NCR", "earthquake_count": 45, "last_earthquake": "2024-01-15T10:30:00Z", "avg_magnitude": 4.2},
    {"name": "CAR", "code": "CAR", "earthquake_count": 32, "last_earthquake": "2024-01-14T15:20:00Z", "avg_magnitude": 3.8},
    {"name": "Region I", "code": "REGION_1", "earthquake_count": 28, "last_earthquake": "2024-01-12T14:15:00Z", "avg_magnitude": 4.1},
    {"name": "Region II", "code": "REGION_2", "earthquake_count": 35, "last_earthquake": "2024-01-11T09:30:00Z", "avg_magnitude": 4.5},
    {"name": "Region III", "code": "REGION_3", "earthquake_count": 52, "last_earthquake": "2024-01-10T16:45:00Z", "avg_magnitude": 4.3},
    {"name": "Region IV-A", "code": "REGION_4A", "earthquake_count": 41, "last_earthquake": "2024-01-13T08:45:00Z", "avg_magnitude": 4.7},
    {"name": "Region IV-B", "code": "REGION_4B", "earthquake_count": 23, "last_earthquake": "2024-01-09T11:20:00Z", "avg_magnitude": 3.9},
    {"name": "Region V", "code": "REGION_5", "earthquake_count": 38, "last_earthquake": "2024-01-08T13:10:00Z", "avg_magnitude": 4.0},
    {"name": "Region VI", "code": "REGION_6", "earthquake_count": 29, "last_earthquake": "2024-01-07T07:55:00Z", "avg_magnitude": 3.7},
    {"name": "Region VII", "code": "REGION_7", "earthquake_count": 34, "last_earthquake": "2024-01-06T12:40:00Z", "avg_magnitude": 4.1},
    {"name": "Region VIII", "code": "REGION_8", "earthquake_count": 31, "last_earthquake": "2024-01-05T18:25:00Z", "avg_magnitude": 4.4},
    {"name": "Region IX", "code": "REGION_9", "earthquake_count": 26, "last_earthquake": "2024-01-04T10:15:00Z", "avg_magnitude": 3.6},
    {"name": "Region X", "code": "REGION_10", "earthquake_count": 33, "last_earthquake": "2024-01-03T14:50:00Z", "avg_magnitude": 4.2},
    {"name": "Region XI", "code": "REGION_11", "earthquake_count": 27, "last_earthquake": "2024-01-02T09:35:00Z", "avg_magnitude": 3.9},
    {"name": "Region XII", "code": "REGION_12", "earthquake_count": 24, "last_earthquake": "2024-01-01T16:20:00Z", "avg_magnitude": 3.8},
    {"name": "Region XIII", "code": "REGION_13", "earthquake_count": 22, "last_earthquake": "2023-12-31T11:05:00Z", "avg_magnitude": 3.5},
    {"name": "ARMM", "code": "ARMM", "earthquake_count": 19, "last_earthquake": "2023-12-30T08:30:00Z", "avg_magnitude": 3.7}
]

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Earthquake Forecasting API",
        "version": "1.0.0",
        "status": "running",
        "description": "API for earthquake data and forecasting system in the Philippines"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy", 
        "timestamp": datetime.now().isoformat(),
        "service": "Earthquake Forecasting API"
    }

@app.get("/api/regions")
async def get_regions():
    """Get available Philippine regions for earthquake forecasting"""
    try:
        return {"regions": PHILIPPINE_REGIONS, "total": len(PHILIPPINE_REGIONS)}
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
        # For now, return sample data
        # Later you can implement actual data filtering
        earthquakes = SAMPLE_EARTHQUAKES.copy()
        
        # Simple filtering (basic implementation)
        if region:
            earthquakes = [eq for eq in earthquakes if eq["region"] == region]
        
        if min_magnitude is not None:
            earthquakes = [eq for eq in earthquakes if eq["magnitude"] >= min_magnitude]
        
        if max_magnitude is not None:
            earthquakes = [eq for eq in earthquakes if eq["magnitude"] <= max_magnitude]
        
        # Limit results
        earthquakes = earthquakes[:limit]
        
        return {
            "earthquakes": earthquakes, 
            "count": len(earthquakes),
            "filters_applied": {
                "region": region,
                "start_date": start_date,
                "end_date": end_date,
                "min_magnitude": min_magnitude,
                "max_magnitude": max_magnitude,
                "limit": limit
            }
        }
    except Exception as e:
        logger.error(f"Error fetching earthquakes: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch earthquake data")

@app.get("/api/statistics")
async def get_statistics(region: Optional[str] = None):
    """Get statistical information about earthquake data"""
    try:
        # For now, return sample statistics
        # Later you can implement actual statistical calculations
        
        if region:
            # Filter data for specific region
            region_data = [eq for eq in SAMPLE_EARTHQUAKES if eq["region"] == region]
            total_earthquakes = len(region_data)
            magnitudes = [eq["magnitude"] for eq in region_data]
            depths = [eq["depth"] for eq in region_data]
        else:
            # Use all data
            total_earthquakes = len(SAMPLE_EARTHQUAKES)
            magnitudes = [eq["magnitude"] for eq in SAMPLE_EARTHQUAKES]
            depths = [eq["depth"] for eq in SAMPLE_EARTHQUAKES]
        
        if magnitudes:
            magnitude_stats = {
                "mean": round(sum(magnitudes) / len(magnitudes), 2),
                "min": min(magnitudes),
                "max": max(magnitudes),
                "count": len(magnitudes)
            }
        else:
            magnitude_stats = {"mean": 0, "min": 0, "max": 0, "count": 0}
        
        if depths:
            depth_stats = {
                "mean": round(sum(depths) / len(depths), 2),
                "min": min(depths),
                "max": max(depths),
                "count": len(depths)
            }
        else:
            depth_stats = {"mean": 0, "min": 0, "max": 0, "count": 0}
        
        return {
            "region": region,
            "total_earthquakes": total_earthquakes,
            "magnitude_stats": magnitude_stats,
            "depth_stats": depth_stats,
            "data_source": "Sample Data (Development)",
            "last_updated": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error calculating statistics: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch statistics")

@app.get("/api/model-info")
async def get_model_info():
    """Get information about the ML model (placeholder for now)"""
    try:
        return {
            "model_name": "Earthquake Prediction Model",
            "model_version": "1.0.0",
            "status": "Development Mode",
            "description": "Attention-LSTM model for earthquake magnitude prediction",
            "current_state": "Not yet implemented - API structure ready",
            "planned_features": [
                "Attention-LSTM architecture",
                "PHIVOLCS data integration",
                "Spatio-temporal forecasting",
                "Confidence intervals",
                "Risk assessment"
            ],
            "last_updated": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error fetching model info: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch model info")

@app.get("/api/status")
async def get_api_status():
    """Get overall API status and readiness"""
    return {
        "api_status": "running",
        "backend_ready": True,
        "ml_model_ready": False,
        "data_service_ready": True,
        "prediction_service_ready": False,
        "development_phase": "Backend API Structure",
        "next_steps": [
            "Implement ML model integration",
            "Add real PHIVOLCS data",
            "Implement prediction endpoints",
            "Add data validation and error handling"
        ],
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )