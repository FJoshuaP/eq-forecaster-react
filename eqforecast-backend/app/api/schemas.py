from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RiskLevel(str, Enum):
    """Risk level enumeration for earthquake forecasts"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Coordinates(BaseModel):
    """Geographic coordinates"""
    latitude: float = Field(..., ge=-90, le=90, description="Latitude in decimal degrees")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude in decimal degrees")

class EarthquakeData(BaseModel):
    """Historical earthquake data model"""
    id: int
    date: datetime
    latitude: float
    longitude: float
    depth: float = Field(..., ge=0, description="Depth in kilometers")
    magnitude: float = Field(..., ge=0, le=10, description="Earthquake magnitude")
    location: str
    bin_id: int = Field(..., ge=1, le=4, description="Geographic bin ID")

class BinForecast(BaseModel):
    """Forecast data for a specific bin"""
    bin_id: int = Field(..., ge=1, le=4)
    max_magnitude: float = Field(..., ge=0, le=10)
    num_earthquakes: int = Field(..., ge=0)
    risk_level: RiskLevel
    confidence_level: Optional[float] = Field(None, ge=0, le=1)
    location: Optional[str] = None
    historical_pattern: Optional[str] = None
    recommendations: Optional[List[str]] = None

class RegionInfo(BaseModel):
    """Geographic region information"""
    bin_id: int
    name: str
    coordinates: Coordinates
    description: str

class ForecastRequest(BaseModel):
    """Request model for generating forecasts"""
    year: Optional[int] = Field(None, ge=2020, le=2030)
    region_id: Optional[int] = Field(None, ge=1, le=4)
    include_historical: bool = Field(True, description="Include historical data in response")
    confidence_threshold: Optional[float] = Field(None, ge=0.5, le=0.99)

class ForecastResponse(BaseModel):
    """Response model for forecast data"""
    year: int
    generated_at: datetime
    forecast_data: List[BinForecast]
    total_earthquakes: int
    max_expected_magnitude: float
    confidence_score: Optional[float] = None
    model_version: str = "1.0.0"
    data_source: str = "PHIVOLCS"

class HistoricalDataRequest(BaseModel):
    """Request model for historical data"""
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    min_magnitude: Optional[float] = Field(None, ge=0, le=10)
    max_magnitude: Optional[float] = Field(None, ge=0, le=10)
    region_id: Optional[int] = Field(None, ge=1, le=4)
    limit: Optional[int] = Field(100, ge=1, le=1000)

class HistoricalDataResponse(BaseModel):
    """Response model for historical data"""
    data: List[EarthquakeData]
    total_count: int
    filters_applied: Dict[str, Any]
    data_range: Optional[Dict[str, datetime]] = None

class APIError(BaseModel):
    """Standard API error response"""
    error: str
    detail: str
    timestamp: datetime
    status_code: int

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    timestamp: datetime
    version: str = "1.0.0"
    database_status: Optional[str] = None
    model_status: Optional[str] = None