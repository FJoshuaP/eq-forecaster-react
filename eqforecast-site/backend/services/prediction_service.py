import numpy as np
import pandas as pd
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
import logging
import uuid
from schemas.earthquake import PredictionRequest, PredictionResponse, ModelInfoResponse
from models.earthquake_model import EarthquakePredictor
import os

logger = logging.getLogger(__name__)

class PredictionService:
    """Service for handling earthquake predictions using ML model"""
    
    def __init__(self):
        self.model = None
        self.model_initialized = False
        self.model_path = "models/attention_lstm_model.h5"
        self.feature_columns = ['latitude', 'longitude', 'depth', 'magnitude', 'time_since_last', 'region_encoded']
        
    async def initialize_model(self):
        """Initialize the ML model"""
        try:
            logger.info("Initializing earthquake prediction model...")
            
            # Check if model file exists
            if os.path.exists(self.model_path):
                self.model = EarthquakePredictor()
                await self.model.load_model(self.model_path)
                logger.info("Loaded existing trained model")
            else:
                logger.warning("No trained model found. Creating placeholder model for development.")
                self.model = EarthquakePredictor()
                await self.model.create_placeholder_model()
                logger.info("Created placeholder model for development")
            
            self.model_initialized = True
            logger.info("Model initialization completed")
            
        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
            # Create a fallback model for development
            self.model = EarthquakePredictor()
            await self.model.create_placeholder_model()
            self.model_initialized = True
            logger.warning("Using fallback model due to initialization error")
    
    async def predict_magnitude(self, request: PredictionRequest) -> PredictionResponse:
        """Predict earthquake magnitude for given parameters"""
        try:
            if not self.model_initialized:
                raise Exception("Model not initialized")
            
            # Generate prediction ID
            prediction_id = str(uuid.uuid4())
            
            # Prepare features for prediction
            features = self._prepare_features(request)
            
            # Make prediction
            predicted_magnitude = await self.model.predict(features)
            
            # Calculate confidence intervals
            confidence_interval = self._calculate_confidence_interval(
                predicted_magnitude, 
                request.confidence_level
            )
            
            # Determine risk level
            risk_level = self._determine_risk_level(predicted_magnitude)
            
            # Generate recommendations
            recommendations = self._generate_recommendations(
                predicted_magnitude, 
                risk_level, 
                request.region
            )
            
            # Calculate model confidence (placeholder for now)
            model_confidence = self._calculate_model_confidence(features)
            
            return PredictionResponse(
                prediction_id=prediction_id,
                region=request.region,
                latitude=request.latitude,
                longitude=request.longitude,
                depth=request.depth,
                predicted_magnitude=float(predicted_magnitude),
                confidence_interval_lower=float(confidence_interval['lower']),
                confidence_interval_upper=float(confidence_interval['upper']),
                confidence_level=request.confidence_level,
                prediction_date=datetime.now(),
                time_horizon_days=request.time_horizon_days,
                model_confidence=float(model_confidence),
                risk_level=risk_level,
                recommendations=recommendations
            )
            
        except Exception as e:
            logger.error(f"Error making prediction: {e}")
            raise
    
    def _prepare_features(self, request: PredictionRequest) -> np.ndarray:
        """Prepare features for the ML model"""
        try:
            # Basic features
            features = np.array([
                request.latitude,
                request.longitude,
                request.depth,
                0.0,  # Placeholder for historical magnitude
                0.0,  # Placeholder for time since last earthquake
                0.0   # Placeholder for region encoding
            ])
            
            # Normalize features (placeholder normalization)
            # In a real implementation, you'd use the same normalization as training
            features = features.reshape(1, -1)
            
            return features
            
        except Exception as e:
            logger.error(f"Error preparing features: {e}")
            raise
    
    def _calculate_confidence_interval(
        self, 
        predicted_magnitude: float, 
        confidence_level: float
    ) -> Dict[str, float]:
        """Calculate confidence interval for prediction"""
        try:
            # Placeholder confidence interval calculation
            # In a real implementation, this would use model uncertainty estimates
            
            # Standard error (placeholder)
            std_error = 0.5
            
            # Z-score for confidence level
            if confidence_level == 0.95:
                z_score = 1.96
            elif confidence_level == 0.90:
                z_score = 1.645
            elif confidence_level == 0.99:
                z_score = 2.576
            else:
                z_score = 1.96
            
            margin_of_error = z_score * std_error
            
            return {
                'lower': max(0, predicted_magnitude - margin_of_error),
                'upper': predicted_magnitude + margin_of_error
            }
            
        except Exception as e:
            logger.error(f"Error calculating confidence interval: {e}")
            return {'lower': predicted_magnitude - 0.5, 'upper': predicted_magnitude + 0.5}
    
    def _determine_risk_level(self, predicted_magnitude: float) -> str:
        """Determine risk level based on predicted magnitude"""
        try:
            if predicted_magnitude >= 7.0:
                return "CRITICAL"
            elif predicted_magnitude >= 6.0:
                return "HIGH"
            elif predicted_magnitude >= 5.0:
                return "MEDIUM"
            elif predicted_magnitude >= 4.0:
                return "LOW"
            else:
                return "MINIMAL"
                
        except Exception as e:
            logger.error(f"Error determining risk level: {e}")
            return "UNKNOWN"
    
    def _generate_recommendations(
        self, 
        predicted_magnitude: float, 
        risk_level: str, 
        region: str
    ) -> List[str]:
        """Generate recommendations based on prediction"""
        recommendations = []
        
        try:
            # General recommendations based on magnitude
            if predicted_magnitude >= 6.0:
                recommendations.extend([
                    "Evacuate to designated safe zones immediately",
                    "Follow emergency protocols for major earthquakes",
                    "Ensure emergency supplies are readily available"
                ])
            elif predicted_magnitude >= 5.0:
                recommendations.extend([
                    "Secure heavy objects and furniture",
                    "Review emergency evacuation plans",
                    "Monitor local emergency broadcasts"
                ])
            elif predicted_magnitude >= 4.0:
                recommendations.extend([
                    "Check emergency preparedness kits",
                    "Review earthquake safety procedures",
                    "Stay informed about local seismic activity"
                ])
            
            # Region-specific recommendations
            if region in ["NCR", "Region III", "Region IV-A"]:
                recommendations.append("High population density area - ensure evacuation routes are clear")
            
            if region in ["Region V", "Region VIII"]:
                recommendations.append("Coastal region - be aware of potential tsunami risks")
            
            # Add general safety recommendations
            recommendations.extend([
                "Drop, Cover, and Hold On during earthquakes",
                "Stay away from windows and heavy objects",
                "Have a family emergency communication plan"
            ])
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            recommendations = ["Follow standard earthquake safety procedures"]
        
        return recommendations
    
    def _calculate_model_confidence(self, features: np.ndarray) -> float:
        """Calculate model confidence for the prediction"""
        try:
            # Placeholder confidence calculation
            # In a real implementation, this would use model uncertainty estimates
            
            # Simple heuristic based on feature values
            confidence = 0.8  # Base confidence
            
            # Adjust based on feature quality (placeholder logic)
            if np.any(np.isnan(features)):
                confidence *= 0.7
            
            if np.any(features == 0):
                confidence *= 0.9
            
            return min(0.95, max(0.5, confidence))
            
        except Exception as e:
            logger.error(f"Error calculating model confidence: {e}")
            return 0.7
    
    def get_model_info(self) -> ModelInfoResponse:
        """Get information about the trained ML model"""
        try:
            if not self.model_initialized:
                return ModelInfoResponse(
                    model_name="Placeholder Model",
                    model_version="0.0.1",
                    training_date=datetime.now(),
                    accuracy_metrics={"placeholder": 0.0},
                    feature_importance={"placeholder": 0.0},
                    model_architecture="Attention-LSTM (Placeholder)",
                    training_data_size=0,
                    last_updated=datetime.now()
                )
            
            # Get actual model info if available
            model_info = self.model.get_model_info()
            return model_info
            
        except Exception as e:
            logger.error(f"Error getting model info: {e}")
            # Return placeholder info
            return ModelInfoResponse(
                model_name="Earthquake Prediction Model",
                model_version="1.0.0",
                training_date=datetime.now(),
                accuracy_metrics={"mae": 0.0, "rmse": 0.0, "r2": 0.0},
                feature_importance={"latitude": 0.25, "longitude": 0.25, "depth": 0.2, "magnitude": 0.3},
                model_architecture="Attention-Enhanced LSTM",
                training_data_size=1000,
                last_updated=datetime.now()
            )
    
    async def retrain_model(self, new_data_path: str) -> bool:
        """Retrain the model with new data"""
        try:
            if not self.model_initialized:
                logger.error("Cannot retrain: model not initialized")
                return False
            
            logger.info("Starting model retraining...")
            
            # Retrain the model
            success = await self.model.retrain(new_data_path)
            
            if success:
                logger.info("Model retraining completed successfully")
                return True
            else:
                logger.error("Model retraining failed")
                return False
                
        except Exception as e:
            logger.error(f"Error during model retraining: {e}")
            return False
    
    def get_prediction_history(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get history of predictions made (placeholder)"""
        # In a real implementation, this would query a database
        return []