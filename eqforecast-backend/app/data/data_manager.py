"""
Data Manager for PHIVOLCS Earthquake Data

This module handles the loading, processing, and management of earthquake data
from PHIVOLCS (Philippine Institute of Volcanology and Seismology).

Author: [Your Name]
Date: [Current Date]
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
import requests
import json
import logging
from datetime import datetime, timedelta
import sqlite3
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataManager:
    """
    Manages earthquake data from PHIVOLCS and other sources
    
    Responsibilities:
    - Load and parse PHIVOLCS data
    - Store data in local database
    - Provide data access methods
    - Data validation and cleaning
    """
    
    def __init__(self, db_path: str = "earthquake_data.db"):
        """
        Initialize the data manager
        
        Args:
            db_path: Path to SQLite database
        """
        self.db_path = db_path
        self.db_connection = None
        self._init_database()
        
        # PHIVOLCS data structure
        self.required_columns = [
            'date', 'time', 'latitude', 'longitude', 'depth', 
            'magnitude', 'magnitude_type', 'location', 'region'
        ]
        
        # Geographic bins for Philippines
        self.geographic_bins = {
            1: {
                "name": "Northern Luzon",
                "lat_range": (16.0, 18.0),
                "lng_range": (120.0, 121.0),
                "description": "Baguio, La Union, Ilocos region"
            },
            2: {
                "name": "Central Luzon", 
                "lat_range": (14.5, 16.0),
                "lng_range": (120.0, 121.0),
                "description": "Angeles, Pampanga, Tarlac region"
            },
            3: {
                "name": "Metro Manila",
                "lat_range": (14.0, 15.0),
                "lng_range": (120.5, 121.5),
                "description": "Manila, Quezon City, surrounding areas"
            },
            4: {
                "name": "Southern Philippines",
                "lat_range": (6.0, 8.0),
                "lng_range": (125.0, 126.0),
                "description": "Davao, Mindanao region"
            }
        }
    
    def _init_database(self):
        """Initialize SQLite database with required tables"""
        try:
            self.db_connection = sqlite3.connect(self.db_path)
            cursor = self.db_connection.cursor()
            
            # Create earthquakes table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS earthquakes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    time TEXT,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    depth REAL,
                    magnitude REAL NOT NULL,
                    magnitude_type TEXT,
                    location TEXT,
                    region TEXT,
                    bin_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create forecasts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS forecasts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    year INTEGER NOT NULL,
                    bin_id INTEGER NOT NULL,
                    max_magnitude REAL NOT NULL,
                    num_earthquakes INTEGER NOT NULL,
                    risk_level TEXT NOT NULL,
                    confidence_level REAL,
                    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create indexes for better performance
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_earthquakes_date ON earthquakes(date)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_earthquakes_bin ON earthquakes(bin_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_earthquakes_magnitude ON earthquakes(magnitude)')
            
            self.db_connection.commit()
            logger.info("Database initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing database: {str(e)}")
            raise
    
    def load_phivolcs_data(self, file_path: str = None, url: str = None) -> pd.DataFrame:
        """
        Load earthquake data from PHIVOLCS
        
        Args:
            file_path: Path to local CSV/Excel file
            url: URL to download data from
            
        Returns:
            DataFrame containing earthquake data
        """
        try:
            if file_path and os.path.exists(file_path):
                logger.info(f"Loading data from local file: {file_path}")
                return self._load_from_file(file_path)
            elif url:
                logger.info(f"Downloading data from URL: {url}")
                return self._download_from_url(url)
            else:
                logger.warning("No file path or URL provided, loading sample data")
                return self._generate_sample_data()
                
        except Exception as e:
            logger.error(f"Error loading PHIVOLCS data: {str(e)}")
            return self._generate_sample_data()
    
    def _load_from_file(self, file_path: str) -> pd.DataFrame:
        """Load data from local file"""
        file_ext = Path(file_path).suffix.lower()
        
        if file_ext == '.csv':
            df = pd.read_csv(file_path)
        elif file_ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
        elif file_ext == '.json':
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
        
        return self._clean_and_validate_data(df)
    
    def _download_from_url(self, url: str) -> pd.DataFrame:
        """Download data from URL"""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Try to determine file type from response headers
            content_type = response.headers.get('content-type', '')
            
            if 'csv' in content_type:
                df = pd.read_csv(pd.StringIO(response.text))
            elif 'json' in content_type:
                df = pd.read_json(response.text)
            else:
                # Default to CSV
                df = pd.read_csv(pd.StringIO(response.text))
            
            return self._clean_and_validate_data(df)
            
        except Exception as e:
            logger.error(f"Error downloading data: {str(e)}")
            raise
    
    def _generate_sample_data(self) -> pd.DataFrame:
        """Generate sample earthquake data for development/testing"""
        logger.info("Generating sample earthquake data")
        
        # Generate realistic sample data based on Philippine earthquake patterns
        np.random.seed(42)  # For reproducible results
        
        # Date range: 2015 to present
        start_date = datetime(2015, 1, 1)
        end_date = datetime.now()
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # Generate earthquakes (not every day)
        earthquake_dates = np.random.choice(date_range, size=500, replace=False)
        
        sample_data = []
        for date in earthquake_dates:
            # Randomly select a bin
            bin_id = np.random.randint(1, 5)
            bin_info = self.geographic_bins[bin_id]
            
            # Generate coordinates within the bin
            lat = np.random.uniform(bin_info["lat_range"][0], bin_info["lat_range"][1])
            lng = np.random.uniform(bin_info["lng_range"][0], bin_info["lng_range"][1])
            
            # Generate magnitude (following Gutenberg-Richter law)
            magnitude = np.random.exponential(scale=1.5) + 3.0  # 3.0 to ~8.0
            magnitude = min(8.0, magnitude)
            
            # Generate depth (0-100 km)
            depth = np.random.uniform(0, 100)
            
            # Generate time
            time = f"{np.random.randint(0, 24):02d}:{np.random.randint(0, 60):02d}:{np.random.randint(0, 60):02d}"
            
            sample_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'time': time,
                'latitude': round(lat, 4),
                'longitude': round(lng, 4),
                'depth': round(depth, 1),
                'magnitude': round(magnitude, 1),
                'magnitude_type': 'ML',  # Local magnitude
                'location': bin_info["name"],
                'region': bin_info["description"],
                'bin_id': bin_id
            })
        
        df = pd.DataFrame(sample_data)
        logger.info(f"Generated {len(df)} sample earthquake records")
        return df
    
    def _clean_and_validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and validate earthquake data
        
        Args:
            df: Raw earthquake data
            
        Returns:
            Cleaned and validated DataFrame
        """
        logger.info("Cleaning and validating earthquake data")
        
        # Check required columns
        missing_cols = [col for col in self.required_columns if col not in df.columns]
        if missing_cols:
            logger.warning(f"Missing columns: {missing_cols}")
            # Add missing columns with default values
            for col in missing_cols:
                if col == 'bin_id':
                    df[col] = 0  # Will be calculated later
                else:
                    df[col] = None
        
        # Clean date column
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df = df.dropna(subset=['date'])
        
        # Clean numeric columns
        numeric_cols = ['latitude', 'longitude', 'depth', 'magnitude']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Validate coordinate ranges
        if 'latitude' in df.columns:
            df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]
        if 'longitude' in df.columns:
            df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]
        
        # Validate magnitude range
        if 'magnitude' in df.columns:
            df = df[(df['magnitude'] >= 0) & (df['magnitude'] <= 10)]
        
        # Calculate bin_id if not present
        if 'bin_id' not in df.columns or df['bin_id'].isna().all():
            df['bin_id'] = df.apply(self._assign_bin_id, axis=1)
        
        # Remove rows with invalid data
        df = df.dropna(subset=['latitude', 'longitude', 'magnitude'])
        
        logger.info(f"Data cleaning completed. {len(df)} valid records remaining")
        return df
    
    def _assign_bin_id(self, row: pd.Series) -> int:
        """Assign geographic bin ID based on coordinates"""
        try:
            lat = row['latitude']
            lng = row['longitude']
            
            for bin_id, bin_info in self.geographic_bins.items():
                lat_range = bin_info["lat_range"]
                lng_range = bin_info["lng_range"]
                
                if (lat_range[0] <= lat <= lat_range[1] and 
                    lng_range[0] <= lng <= lng_range[1]):
                    return bin_id
            
            # If no bin matches, assign to closest one
            return self._find_closest_bin(lat, lng)
            
        except (KeyError, TypeError):
            return 1  # Default to first bin
    
    def _find_closest_bin(self, lat: float, lng: float) -> int:
        """Find the closest geographic bin to given coordinates"""
        min_distance = float('inf')
        closest_bin = 1
        
        for bin_id, bin_info in self.geographic_bins.items():
            bin_lat = (bin_info["lat_range"][0] + bin_info["lat_range"][1]) / 2
            bin_lng = (bin_info["lng_range"][0] + bin_info["lng_range"][1]) / 2
            
            distance = ((lat - bin_lat) ** 2 + (lng - bin_lng) ** 2) ** 0.5
            
            if distance < min_distance:
                min_distance = distance
                closest_bin = bin_id
        
        return closest_bin
    
    def store_data(self, df: pd.DataFrame) -> bool:
        """
        Store earthquake data in database
        
        Args:
            df: DataFrame containing earthquake data
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if self.db_connection is None:
                self._init_database()
            
            cursor = self.db_connection.cursor()
            
            # Prepare data for insertion
            data_to_insert = []
            for _, row in df.iterrows():
                data_to_insert.append((
                    row.get('date', ''),
                    row.get('time', ''),
                    row.get('latitude', 0),
                    row.get('longitude', 0),
                    row.get('depth', 0),
                    row.get('magnitude', 0),
                    row.get('magnitude_type', ''),
                    row.get('location', ''),
                    row.get('region', ''),
                    row.get('bin_id', 1)
                ))
            
            # Insert data
            cursor.executemany('''
                INSERT INTO earthquakes 
                (date, time, latitude, longitude, depth, magnitude, 
                 magnitude_type, location, region, bin_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', data_to_insert)
            
            self.db_connection.commit()
            logger.info(f"Stored {len(data_to_insert)} earthquake records")
            return True
            
        except Exception as e:
            logger.error(f"Error storing data: {str(e)}")
            return False
    
    def get_earthquake_data(self, 
                           start_date: str = None,
                           end_date: str = None,
                           bin_id: int = None,
                           min_magnitude: float = None,
                           max_magnitude: float = None,
                           limit: int = 1000) -> List[Dict]:
        """
        Retrieve earthquake data from database
        
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            bin_id: Geographic bin ID
            min_magnitude: Minimum magnitude
            max_magnitude: Maximum magnitude
            limit: Maximum number of records to return
            
        Returns:
            List of earthquake records
        """
        try:
            if self.db_connection is None:
                self._init_database()
            
            cursor = self.db_connection.cursor()
            
            # Build query
            query = "SELECT * FROM earthquakes WHERE 1=1"
            params = []
            
            if start_date:
                query += " AND date >= ?"
                params.append(start_date)
            
            if end_date:
                query += " AND date <= ?"
                params.append(end_date)
            
            if bin_id:
                query += " AND bin_id = ?"
                params.append(bin_id)
            
            if min_magnitude is not None:
                query += " AND magnitude >= ?"
                params.append(min_magnitude)
            
            if max_magnitude is not None:
                query += " AND magnitude <= ?"
                params.append(max_magnitude)
            
            query += " ORDER BY date DESC LIMIT ?"
            params.append(limit)
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            # Convert to list of dictionaries
            columns = [description[0] for description in cursor.description]
            data = []
            for row in rows:
                data.append(dict(zip(columns, row)))
            
            logger.info(f"Retrieved {len(data)} earthquake records")
            return data
            
        except Exception as e:
            logger.error(f"Error retrieving data: {str(e)}")
            return []
    
    def get_statistics(self) -> Dict:
        """Get statistics about stored earthquake data"""
        try:
            if self.db_connection is None:
                self._init_database()
            
            cursor = self.db_connection.cursor()
            
            # Total count
            cursor.execute("SELECT COUNT(*) FROM earthquakes")
            total_count = cursor.fetchone()[0]
            
            # Magnitude statistics
            cursor.execute("""
                SELECT 
                    MIN(magnitude) as min_mag,
                    MAX(magnitude) as max_mag,
                    AVG(magnitude) as avg_mag,
                    COUNT(*) as count
                FROM earthquakes
            """)
            mag_stats = cursor.fetchone()
            
            # Bin distribution
            cursor.execute("""
                SELECT bin_id, COUNT(*) as count
                FROM earthquakes
                GROUP BY bin_id
                ORDER BY bin_id
            """)
            bin_distribution = dict(cursor.fetchall())
            
            # Date range
            cursor.execute("""
                SELECT MIN(date) as earliest, MAX(date) as latest
                FROM earthquakes
            """)
            date_range = cursor.fetchone()
            
            return {
                "total_earthquakes": total_count,
                "magnitude_stats": {
                    "min": mag_stats[0],
                    "max": mag_stats[1],
                    "average": mag_stats[2],
                    "count": mag_stats[3]
                },
                "bin_distribution": bin_distribution,
                "date_range": {
                    "earliest": date_range[0],
                    "latest": date_range[1]
                }
            }
            
        except Exception as e:
            logger.error(f"Error getting statistics: {str(e)}")
            return {}
    
    def close_connection(self):
        """Close database connection"""
        if self.db_connection:
            self.db_connection.close()
            self.db_connection = None
            logger.info("Database connection closed")
    
    def __del__(self):
        """Cleanup when object is destroyed"""
        self.close_connection()