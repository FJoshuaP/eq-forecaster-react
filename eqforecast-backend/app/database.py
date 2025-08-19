"""
Database models and connection management
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import func
from datetime import datetime
from typing import Generator
from app.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Database Models
class Earthquake(Base):
    """Earthquake data model"""
    __tablename__ = "earthquakes"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False, index=True)
    time = Column(String(20))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    depth = Column(Float)
    magnitude = Column(Float, nullable=False, index=True)
    magnitude_type = Column(String(10))
    location = Column(String(200))
    region = Column(String(200))
    bin_id = Column(Integer, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Forecast(Base):
    """Forecast data model"""
    __tablename__ = "forecasts"
    
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    bin_id = Column(Integer, nullable=False, index=True)
    max_magnitude = Column(Float, nullable=False)
    num_earthquakes = Column(Integer, nullable=False)
    risk_level = Column(String(20), nullable=False)
    confidence_level = Column(Float)
    location = Column(String(200))
    historical_pattern = Column(Text)
    recommendations = Column(Text)
    generated_at = Column(DateTime, default=func.now())
    model_version = Column(String(20))
    data_source = Column(String(50))

class ModelMetadata(Base):
    """Machine learning model metadata"""
    __tablename__ = "model_metadata"
    
    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String(100), nullable=False)
    version = Column(String(20), nullable=False)
    architecture = Column(String(100))
    training_date = Column(DateTime)
    accuracy = Column(Float)
    file_path = Column(String(500))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

# Database dependency
def get_db() -> Generator[Session, None, None]:
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create all tables
def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)

# Initialize database
def init_db():
    """Initialize database with tables"""
    create_tables()
    print("Database initialized successfully")