from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RegionEnum(str, Enum):
    """Philippine regions for earthquake forecasting"""
    NCR = "NCR"
    CAR = "CAR"
    REGION_1 = "Region I"
    REGION_2 = "Region II"
    REGION_3 = "Region III"
    REGION_4A = "Region IV-A"
    REGION_4B = "Region IV-B"
    REGION_5 = "Region V"
    REGION_6 = "Region VI"
    REGION_7 = "Region VII"
    REGION_8 = "Region VIII"
    REGION_9 = "Region IX"
    REGION_10 = "Region X"
    REGION_11 = "Region XI"
    REGION_12 = "Region XII"
    REGION_13 = "Region XIII"
    ARMM = "ARMM"

class EarthquakeData(BaseModel):
    """Schema for earthquake data"""
    id: str
    timestamp: datetime
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    depth: float = Field(..., ge=0)
    magnitude: float = Field(..., ge=0)
    region: RegionEnum
    location_description: Optional[str] = None
    source: str = "PHIVOLCS"
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class PredictionRequest(BaseModel):
    """Schema for earthquake prediction request"""
    region: RegionEnum
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    depth: float = Field(..., ge=0)
    time_horizon_days: int = Field(..., ge=1, le=365)
    historical_window_days: int = Field(..., ge=30, le=365)
    confidence_level: float = Field(0.95, ge=0.5, le=0.99)
    
    @validator('time_horizon_days')
    def validate_time_horizon(cls, v):
        if v > 365:
            raise ValueError('Time horizon cannot exceed 1 year')
        return v

class PredictionResponse(BaseModel):
    """Schema for earthquake prediction response"""
    prediction_id: str
    region: RegionEnum
    latitude: float
    longitude: float
    depth: float
    predicted_magnitude: float
    confidence_interval_lower: float
    confidence_interval_upper: float
    confidence_level: float
    prediction_date: datetime
    time_horizon_days: int
    model_confidence: float
    risk_level: str
    recommendations: List[str]
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class StatisticsResponse(BaseModel):
    """Schema for earthquake statistics response"""
    region: Optional[RegionEnum]
    total_earthquakes: int
    date_range: Dict[str, datetime]
    magnitude_stats: Dict[str, float]
    depth_stats: Dict[str, float]
    monthly_distribution: Dict[str, int]
    risk_assessment: Dict[str, Any]

class ModelInfoResponse(BaseModel):
    """Schema for ML model information response"""
    model_name: str
    model_version: str
    training_date: datetime
    accuracy_metrics: Dict[str, float]
    feature_importance: Dict[str, float]
    model_architecture: str
    training_data_size: int
    last_updated: datetime
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }