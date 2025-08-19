import pandas as pd
import numpy as np
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
import logging
from schemas.earthquake import EarthquakeData, RegionEnum, StatisticsResponse
import json
import os

logger = logging.getLogger(__name__)

class DataService:
    """Service for handling earthquake data operations"""
    
    def __init__(self):
        self.data_path = "data/earthquakes.csv"
        self.earthquake_data = None
        self._load_data()
    
    def _load_data(self):
        """Load earthquake data from CSV file"""
        try:
            if os.path.exists(self.data_path):
                self.earthquake_data = pd.read_csv(self.data_path)
                # Convert timestamp to datetime
                self.earthquake_data['timestamp'] = pd.to_datetime(self.earthquake_data['timestamp'])
                logger.info(f"Loaded {len(self.earthquake_data)} earthquake records")
            else:
                logger.warning(f"Data file not found at {self.data_path}. Creating sample data.")
                self._create_sample_data()
        except Exception as e:
            logger.error(f"Error loading earthquake data: {e}")
            self._create_sample_data()
    
    def _create_sample_data(self):
        """Create sample earthquake data for development/testing"""
        np.random.seed(42)
        
        # Philippine coordinates (approximate bounds)
        philippine_bounds = {
            'lat_min': 4.5, 'lat_max': 21.5,
            'lon_min': 116.5, 'lon_max': 126.5
        }
        
        # Generate sample data
        n_samples = 1000
        dates = pd.date_range(start='2015-01-01', end='2024-01-01', periods=n_samples)
        
        sample_data = {
            'id': [f"EQ_{i:06d}" for i in range(n_samples)],
            'timestamp': dates,
            'latitude': np.random.uniform(philippine_bounds['lat_min'], philippine_bounds['lat_max'], n_samples),
            'longitude': np.random.uniform(philippine_bounds['lon_min'], philippine_bounds['lon_max'], n_samples),
            'depth': np.random.exponential(50, n_samples),
            'magnitude': np.random.exponential(3, n_samples) + 2,  # 2-8 range
            'region': np.random.choice(list(RegionEnum), n_samples),
            'location_description': [f"Location {i}" for i in range(n_samples)],
            'source': ['PHIVOLCS'] * n_samples
        }
        
        self.earthquake_data = pd.DataFrame(sample_data)
        
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        
        # Save sample data
        self.earthquake_data.to_csv(self.data_path, index=False)
        logger.info(f"Created and saved {n_samples} sample earthquake records")
    
    def get_philippine_regions(self) -> List[Dict[str, Any]]:
        """Get available Philippine regions with metadata"""
        regions = []
        for region in RegionEnum:
            region_data = self.earthquake_data[self.earthquake_data['region'] == region.value]
            
            regions.append({
                'name': region.value,
                'code': region.name,
                'earthquake_count': len(region_data),
                'last_earthquake': region_data['timestamp'].max().isoformat() if len(region_data) > 0 else None,
                'avg_magnitude': region_data['magnitude'].mean() if len(region_data) > 0 else 0.0
            })
        
        return regions
    
    async def get_earthquakes(
        self,
        region: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        min_magnitude: Optional[float] = None,
        max_magnitude: Optional[float] = None,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """Get filtered earthquake data"""
        try:
            data = self.earthquake_data.copy()
            
            # Apply filters
            if region:
                data = data[data['region'] == region]
            
            if start_date:
                start_dt = pd.to_datetime(start_date)
                data = data[data['timestamp'] >= start_dt]
            
            if end_date:
                end_dt = pd.to_datetime(end_date)
                data = data[data['timestamp'] <= end_dt]
            
            if min_magnitude is not None:
                data = data[data['magnitude'] >= min_magnitude]
            
            if max_magnitude is not None:
                data = data[data['magnitude'] <= max_magnitude]
            
            # Sort by timestamp (newest first) and limit results
            data = data.sort_values('timestamp', ascending=False).head(limit)
            
            # Convert to list of dictionaries
            earthquakes = []
            for _, row in data.iterrows():
                earthquake = {
                    'id': row['id'],
                    'timestamp': row['timestamp'].isoformat(),
                    'latitude': float(row['latitude']),
                    'longitude': float(row['longitude']),
                    'depth': float(row['depth']),
                    'magnitude': float(row['magnitude']),
                    'region': row['region'],
                    'location_description': row['location_description'],
                    'source': row['source']
                }
                earthquakes.append(earthquake)
            
            return earthquakes
            
        except Exception as e:
            logger.error(f"Error filtering earthquake data: {e}")
            raise
    
    async def get_statistics(self, region: Optional[str] = None) -> StatisticsResponse:
        """Get statistical information about earthquake data"""
        try:
            data = self.earthquake_data.copy()
            
            if region:
                data = data[data['region'] == region]
            
            # Basic statistics
            total_earthquakes = len(data)
            date_range = {
                'start': data['timestamp'].min().isoformat(),
                'end': data['timestamp'].max().isoformat()
            }
            
            # Magnitude statistics
            magnitude_stats = {
                'mean': float(data['magnitude'].mean()),
                'median': float(data['magnitude'].median()),
                'std': float(data['magnitude'].std()),
                'min': float(data['magnitude'].min()),
                'max': float(data['magnitude'].max())
            }
            
            # Depth statistics
            depth_stats = {
                'mean': float(data['depth'].mean()),
                'median': float(data['depth'].median()),
                'std': float(data['depth'].std()),
                'min': float(data['depth'].min()),
                'max': float(data['depth'].max())
            }
            
            # Monthly distribution
            monthly_distribution = data.groupby(data['timestamp'].dt.to_period('M')).size().to_dict()
            monthly_distribution = {str(k): int(v) for k, v in monthly_distribution.items()}
            
            # Risk assessment
            risk_assessment = self._assess_risk(data)
            
            return StatisticsResponse(
                region=region,
                total_earthquakes=total_earthquakes,
                date_range=date_range,
                magnitude_stats=magnitude_stats,
                depth_stats=depth_stats,
                monthly_distribution=monthly_distribution,
                risk_assessment=risk_assessment
            )
            
        except Exception as e:
            logger.error(f"Error calculating statistics: {e}")
            raise
    
    def _assess_risk(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Assess earthquake risk based on data"""
        try:
            # Recent activity (last 30 days)
            recent_cutoff = datetime.now() - timedelta(days=30)
            recent_data = data[data['timestamp'] >= recent_cutoff]
            
            # High magnitude earthquakes (>= 6.0)
            high_magnitude = data[data['magnitude'] >= 6.0]
            
            # Shallow earthquakes (depth < 70km)
            shallow_earthquakes = data[data['depth'] < 70]
            
            risk_factors = {
                'recent_activity_count': len(recent_data),
                'high_magnitude_count': len(high_magnitude),
                'shallow_earthquake_count': len(shallow_earthquakes),
                'avg_magnitude_trend': self._calculate_trend(data, 'magnitude'),
                'frequency_trend': self._calculate_frequency_trend(data)
            }
            
            # Risk level calculation
            risk_score = 0
            if risk_factors['recent_activity_count'] > 10:
                risk_score += 3
            elif risk_factors['recent_activity_count'] > 5:
                risk_score += 2
            elif risk_factors['recent_activity_count'] > 0:
                risk_score += 1
            
            if risk_factors['high_magnitude_count'] > 5:
                risk_score += 3
            elif risk_factors['high_magnitude_count'] > 2:
                risk_score += 2
            elif risk_factors['high_magnitude_count'] > 0:
                risk_score += 1
            
            # Determine risk level
            if risk_score >= 5:
                risk_level = "HIGH"
            elif risk_score >= 3:
                risk_level = "MEDIUM"
            else:
                risk_level = "LOW"
            
            risk_factors['risk_level'] = risk_level
            risk_factors['risk_score'] = risk_score
            
            return risk_factors
            
        except Exception as e:
            logger.error(f"Error assessing risk: {e}")
            return {"error": str(e)}
    
    def _calculate_trend(self, data: pd.DataFrame, column: str) -> str:
        """Calculate trend for a numeric column"""
        try:
            if len(data) < 10:
                return "insufficient_data"
            
            # Split data into two halves
            mid_point = len(data) // 2
            first_half = data.iloc[:mid_point][column]
            second_half = data.iloc[mid_point:][column]
            
            first_mean = first_half.mean()
            second_mean = second_half.mean()
            
            if second_mean > first_mean * 1.1:
                return "increasing"
            elif second_mean < first_mean * 0.9:
                return "decreasing"
            else:
                return "stable"
        except:
            return "unknown"
    
    def _calculate_frequency_trend(self, data: pd.DataFrame) -> str:
        """Calculate frequency trend over time"""
        try:
            if len(data) < 10:
                return "insufficient_data"
            
            # Group by month and count
            monthly_counts = data.groupby(data['timestamp'].dt.to_period('M')).size()
            
            if len(monthly_counts) < 6:
                return "insufficient_data"
            
            # Calculate trend using simple linear regression
            x = np.arange(len(monthly_counts))
            y = monthly_counts.values
            
            slope = np.polyfit(x, y, 1)[0]
            
            if slope > 0.1:
                return "increasing"
            elif slope < -0.1:
                return "decreasing"
            else:
                return "stable"
        except:
            return "unknown"
    
    def add_earthquake(self, earthquake: EarthquakeData) -> bool:
        """Add new earthquake data"""
        try:
            new_row = pd.DataFrame([{
                'id': earthquake.id,
                'timestamp': earthquake.timestamp,
                'latitude': earthquake.latitude,
                'longitude': earthquake.longitude,
                'depth': earthquake.depth,
                'magnitude': earthquake.magnitude,
                'region': earthquake.region.value,
                'location_description': earthquake.location_description,
                'source': earthquake.source
            }])
            
            self.earthquake_data = pd.concat([self.earthquake_data, new_row], ignore_index=True)
            self.earthquake_data.to_csv(self.data_path, index=False)
            
            logger.info(f"Added new earthquake record: {earthquake.id}")
            return True
            
        except Exception as e:
            logger.error(f"Error adding earthquake data: {e}")
            return False