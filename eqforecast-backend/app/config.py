"""
Configuration management for the Earthquake Forecasting API
"""

import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings loaded from environment variables"""
    
    # Basic App Settings
    APP_NAME: str = os.getenv("APP_NAME", "Earthquake Forecasting API")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # Server Settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Database Settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///earthquake_data.db")
    
    # CORS Settings
    CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
    
    # API Settings
    API_PREFIX: str = os.getenv("API_PREFIX", "/api")
    API_V1_STR: str = os.getenv("API_V1_STR", "/v1")
    
    # Logging Settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Model Settings
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/")
    DEFAULT_CONFIDENCE_THRESHOLD: float = float(os.getenv("DEFAULT_CONFIDENCE_THRESHOLD", "0.8"))
    
    # Data Settings
    DATA_SOURCE: str = os.getenv("DATA_SOURCE", "PHIVOLCS")
    MAX_HISTORICAL_RECORDS: int = int(os.getenv("MAX_HISTORICAL_RECORDS", "10000"))
    
    # Geographic Bins Configuration
    GEOGRAPHIC_BINS = {
        1: {
            "name": "Northern Luzon",
            "coordinates": {"latitude": 16.5, "longitude": 120.5},
            "description": "Baguio, La Union, Ilocos region",
            "color": "#28a745"
        },
        2: {
            "name": "Central Luzon",
            "coordinates": {"latitude": 15.1, "longitude": 120.6},
            "description": "Angeles, Pampanga, Tarlac region",
            "color": "#ffc107"
        },
        3: {
            "name": "Metro Manila",
            "coordinates": {"latitude": 14.6, "longitude": 121.0},
            "description": "Manila, Quezon City, surrounding areas",
            "color": "#dc3545"
        },
        4: {
            "name": "Southern Philippines",
            "coordinates": {"latitude": 7.1, "longitude": 125.6},
            "description": "Davao, Mindanao region",
            "color": "#6f42c1"
        }
    }
    
    # Risk Level Configuration
    RISK_LEVELS = {
        "low": {"color": "#28a745", "threshold": 5.0},
        "medium": {"color": "#ffc107", "threshold": 6.0},
        "high": {"color": "#fd7e14", "threshold": 7.0},
        "critical": {"color": "#dc3545", "threshold": 8.0}
    }

# Create global settings instance
settings = Settings()