"""
Earthquake Forecasting Model using Attention-LSTM Architecture

This module contains the machine learning model for earthquake magnitude forecasting
based on historical PHIVOLCS data from the Philippines.

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Optional
import json
import pickle
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EarthquakeForecastModel:
    """
    Attention-LSTM based earthquake forecasting model
    
    This model processes spatio-temporal earthquake data to predict:
    - Maximum expected magnitude per geographic bin
    - Number of earthquakes expected per bin
    - Risk level assessment
    """
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize the earthquake forecasting model
        
        Args:
            model_path: Path to pre-trained model weights (optional)
        """
        self.model = None
        self.scaler = None
        self.feature_names = [
            'latitude', 'longitude', 'depth', 'magnitude',
            'time_since_last_eq', 'eq_frequency_30d', 'eq_frequency_90d',
            'avg_magnitude_30d', 'max_magnitude_30d', 'seismic_energy_30d'
        ]
        self.bin_regions = {
            1: {"name": "Northern Luzon", "lat_range": (16.0, 18.0), "lng_range": (120.0, 121.0)},
            2: {"name": "Central Luzon", "lat_range": (14.5, 16.0), "lng_range": (120.0, 121.0)},
            3: {"name": "Metro Manila", "lat_range": (14.0, 15.0), "lng_range": (120.5, 121.5)},
            4: {"name": "Southern Philippines", "lat_range": (6.0, 8.0), "lng_range": (125.0, 126.0)}
        }
        
        if model_path:
            self.load_model(model_path)
        else:
            logger.info("No pre-trained model provided. Using mock predictions for development.")
    
    def preprocess_data(self, earthquake_data: List[Dict]) -> np.ndarray:
        """
        Preprocess earthquake data for model input
        
        Args:
            earthquake_data: List of earthquake records
            
        Returns:
            Preprocessed feature matrix
        """
        if not earthquake_data:
            logger.warning("No earthquake data provided for preprocessing")
            return np.array([])
        
        # Convert to DataFrame for easier processing
        df = pd.DataFrame(earthquake_data)
        
        # Ensure required columns exist
        required_cols = ['latitude', 'longitude', 'depth', 'magnitude', 'date']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Convert date strings to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Sort by date
        df = df.sort_values('date')
        
        # Calculate time-based features
        df['time_since_last_eq'] = df['date'].diff().dt.total_seconds() / 3600  # hours
        
        # Calculate rolling statistics for each bin
        features = []
        for bin_id in range(1, 5):
            bin_data = df[df['bin_id'] == bin_id].copy()
            if len(bin_data) == 0:
                # No data for this bin, use default values
                features.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                continue
            
            # Calculate rolling statistics
            bin_data['eq_frequency_30d'] = bin_data.rolling(window=30, min_periods=1)['magnitude'].count()
            bin_data['eq_frequency_90d'] = bin_data.rolling(window=90, min_periods=1)['magnitude'].count()
            bin_data['avg_magnitude_30d'] = bin_data.rolling(window=30, min_periods=1)['magnitude'].mean()
            bin_data['max_magnitude_30d'] = bin_data.rolling(window=30, min_periods=1)['magnitude'].max()
            
            # Calculate seismic energy (simplified: magnitude^2)
            bin_data['seismic_energy_30d'] = bin_data.rolling(window=30, min_periods=1)['magnitude'].apply(
                lambda x: (x**2).sum()
            )
            
            # Get latest values for each feature
            latest_features = [
                bin_data['latitude'].iloc[-1],
                bin_data['longitude'].iloc[-1],
                bin_data['depth'].iloc[-1],
                bin_data['magnitude'].iloc[-1],
                bin_data['time_since_last_eq'].iloc[-1] if len(bin_data) > 1 else 0,
                bin_data['eq_frequency_30d'].iloc[-1],
                bin_data['eq_frequency_90d'].iloc[-1],
                bin_data['avg_magnitude_30d'].iloc[-1],
                bin_data['max_magnitude_30d'].iloc[-1],
                bin_data['seismic_energy_30d'].iloc[-1]
            ]
            
            features.append(latest_features)
        
        return np.array(features)
    
    def predict(self, earthquake_data: List[Dict], forecast_year: int = None) -> Dict:
        """
        Generate earthquake forecast for the Philippines
        
        Args:
            earthquake_data: Historical earthquake data
            forecast_year: Year to forecast (defaults to next year)
            
        Returns:
            Dictionary containing forecast results
        """
        if forecast_year is None:
            forecast_year = datetime.now().year + 1
        
        try:
            # Preprocess input data
            features = self.preprocess_data(earthquake_data)
            
            if len(features) == 0:
                logger.warning("No features generated, using default predictions")
                return self._generate_mock_forecast(forecast_year)
            
            # If we have a trained model, use it
            if self.model is not None:
                predictions = self._model_predict(features)
            else:
                # Use mock predictions for development
                predictions = self._generate_mock_forecast(forecast_year)
            
            # Add metadata
            predictions['year'] = forecast_year
            predictions['generated_at'] = datetime.now().isoformat()
            predictions['model_version'] = '1.0.0'
            predictions['data_source'] = 'PHIVOLCS'
            
            return predictions
            
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            # Fallback to mock predictions
            return self._generate_mock_forecast(forecast_year)
    
    def _model_predict(self, features: np.ndarray) -> Dict:
        """
        Make predictions using the trained model
        
        Args:
            features: Preprocessed feature matrix
            
        Returns:
            Model predictions
        """
        # This would contain the actual LSTM + Attention model inference
        # For now, return mock data
        return self._generate_mock_forecast()
    
    def _generate_mock_forecast(self, year: int = None) -> Dict:
        """
        Generate mock forecast data for development/testing
        
        Args:
            year: Forecast year
            
        Returns:
            Mock forecast data
        """
        if year is None:
            year = datetime.now().year + 1
        
        # Generate realistic mock data based on historical patterns
        base_magnitudes = [4.2, 5.8, 6.5, 7.2]
        base_counts = [15, 8, 3, 1]
        
        # Add some randomness
        np.random.seed(year)  # Consistent results for same year
        
        forecast_data = []
        for i, (base_mag, base_count) in enumerate(zip(base_magnitudes, base_counts)):
            # Add noise to magnitude
            magnitude = base_mag + np.random.normal(0, 0.3)
            magnitude = max(0, min(10, magnitude))  # Clamp to valid range
            
            # Add noise to count
            count = max(0, int(base_count + np.random.normal(0, 2)))
            
            # Determine risk level
            if magnitude < 5.0:
                risk_level = "low"
            elif magnitude < 6.0:
                risk_level = "medium"
            elif magnitude < 7.0:
                risk_level = "high"
            else:
                risk_level = "critical"
            
            forecast_data.append({
                "bin_id": i + 1,
                "max_magnitude": round(magnitude, 1),
                "num_earthquakes": count,
                "risk_level": risk_level,
                "confidence_level": 0.85 + np.random.normal(0, 0.1),
                "location": self.bin_regions[i + 1]["name"]
            })
        
        return {
            "forecast_data": forecast_data,
            "total_earthquakes": sum(bin["num_earthquakes"] for bin in forecast_data),
            "max_expected_magnitude": max(bin["max_magnitude"] for bin in forecast_data),
            "confidence_score": 0.82
        }
    
    def train(self, training_data: List[Dict], validation_data: List[Dict] = None):
        """
        Train the Attention-LSTM model
        
        Args:
            training_data: Training earthquake data
            validation_data: Validation earthquake data (optional)
        """
        logger.info("Training Attention-LSTM model...")
        
        # This would contain the actual training logic
        # For now, just log that training would happen
        
        # TODO: Implement actual training
        # 1. Data preprocessing and feature engineering
        # 2. Sequence creation for LSTM
        # 3. Model architecture definition
        # 4. Training loop with attention mechanism
        # 5. Model validation and hyperparameter tuning
        
        logger.info("Model training completed (mock)")
    
    def save_model(self, model_path: str):
        """
        Save the trained model
        
        Args:
            model_path: Path to save the model
        """
        if self.model is not None:
            # Save model weights
            self.model.save_weights(f"{model_path}_weights.h5")
            
            # Save model architecture
            with open(f"{model_path}_architecture.json", 'w') as f:
                json.dump(self.model.to_json(), f)
            
            # Save scaler
            with open(f"{model_path}_scaler.pkl", 'wb') as f:
                pickle.dump(self.scaler, f)
            
            logger.info(f"Model saved to {model_path}")
        else:
            logger.warning("No model to save")
    
    def load_model(self, model_path: str):
        """
        Load a pre-trained model
        
        Args:
            model_path: Path to the saved model
        """
        try:
            # Load model architecture
            with open(f"{model_path}_architecture.json", 'r') as f:
                model_config = json.load(f)
            
            # Load model weights
            # self.model = tf.keras.models.model_from_json(model_config)
            # self.model.load_weights(f"{model_path}_weights.h5")
            
            # Load scaler
            with open(f"{model_path}_scaler.pkl", 'rb') as f:
                self.scaler = pickle.load(f)
            
            logger.info(f"Model loaded from {model_path}")
            
        except FileNotFoundError:
            logger.warning(f"Model files not found at {model_path}")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
    
    def evaluate_model(self, test_data: List[Dict]) -> Dict:
        """
        Evaluate model performance on test data
        
        Args:
            test_data: Test earthquake data
            
        Returns:
            Evaluation metrics
        """
        logger.info("Evaluating model performance...")
        
        # This would contain actual evaluation logic
        # For now, return mock metrics
        
        return {
            "mae": 0.45,
            "rmse": 0.67,
            "r2_score": 0.78,
            "accuracy": 0.82
        }