import React, { useState, useEffect, useRef } from "react";
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import L from 'leaflet';
import axios from 'axios';
import "../Css/Forecasting.css";

const ForecastPage = ({ navigateToPage }) => {
  const [inputYear, setInputYear] = useState(new Date().getFullYear() + 1);
  const [forecastData, setForecastData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedBin, setSelectedBin] = useState(null);
  const [historicalData, setHistoricalData] = useState([]);
  const [mapCenter] = useState([14.5995, 120.9842]); // Manila coordinates
  const [error, setError] = useState(null);

  // API base URL
  const API_BASE_URL = 'http://localhost:8000';

  // Geographic bins with coordinates
  const geographicBins = {
    1: {
      name: "Northern Luzon",
      coordinates: [16.5, 120.5],
      description: "Baguio, La Union, Ilocos region",
      color: "#28a745" // Green
    },
    2: {
      name: "Central Luzon",
      coordinates: [15.1, 120.6],
      description: "Angeles, Pampanga, Tarlac region",
      color: "#ffc107" // Yellow
    },
    3: {
      name: "Metro Manila",
      coordinates: [14.6, 121.0],
      description: "Manila, Quezon City, surrounding areas",
      color: "#dc3545" // Red
    },
    4: {
      name: "Southern Philippines",
      coordinates: [7.1, 125.6],
      description: "Davao, Mindanao region",
      color: "#6f42c1" // Purple
    }
  };

  // Risk level colors
  const riskColors = {
    low: "#28a745",
    medium: "#ffc107", 
    high: "#fd7e14",
    critical: "#dc3545"
  };

  useEffect(() => {
    // Load initial forecast data
    generateForecast();
    loadHistoricalData();
  }, []);

  const generateForecast = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.get(`${API_BASE_URL}/api/forecast`, {
        params: { year: inputYear }
      });
      
      setForecastData(response.data.forecast_data);
      console.log('Forecast data:', response.data);
      
    } catch (err) {
      console.error('Error fetching forecast:', err);
      setError('Failed to fetch forecast data. Please try again.');
      
      // Fallback to mock data
      setForecastData([
        { bin_id: 1, max_magnitude: 4.2, num_earthquakes: 15, risk_level: "low" },
        { bin_id: 2, max_magnitude: 5.8, num_earthquakes: 8, risk_level: "medium" },
        { bin_id: 3, max_magnitude: 6.5, num_earthquakes: 3, risk_level: "high" },
        { bin_id: 4, max_magnitude: 7.2, num_earthquakes: 1, risk_level: "critical" }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const loadHistoricalData = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/historical-data`, {
        params: { limit: 100 }
      });
      
      setHistoricalData(response.data.data);
      console.log('Historical data:', response.data);
      
    } catch (err) {
      console.error('Error fetching historical data:', err);
      // Historical data is not critical, so we don't show error
    }
  };

  const getBinForecast = async (binId) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/forecast/${binId}`);
      setSelectedBin(response.data);
      console.log('Bin forecast:', response.data);
    } catch (err) {
      console.error('Error fetching bin forecast:', err);
      setError('Failed to fetch detailed forecast for this region.');
    }
  };

  const handleYearSubmit = () => {
    if (inputYear && inputYear >= 2020 && inputYear <= 2030) {
      generateForecast();
    } else {
      setError('Please enter a valid year between 2020 and 2030.');
    }
  };

  const getRiskLevelColor = (riskLevel) => {
    return riskColors[riskLevel] || "#6c757d";
  };

  const getBinColor = (binId) => {
    return geographicBins[binId]?.color || "#6c757d";
  };

  return (
    <div className="forecast-page-container">
      {/* Header */}
      <div className="header">
        <div className="header-content">
          <div className="logo">OPAL</div>
          <div className="nav-menu">
            <button onClick={() => navigateToPage(1)} className="nav-item">
              Overview
            </button>
            <button onClick={() => navigateToPage(3)} className="nav-item">
              About
            </button>
            <button onClick={() => navigateToPage(4)} className="nav-item">
              Hotlines
            </button>
            <button onClick={() => navigateToPage(2)} className="nav-item">
              Awareness
            </button>
            <button className="forecast-btn active">Forecast Now</button>
          </div>
        </div>
      </div>

      <div className="forecast-content">
        {/* Sidebar */}
        <div className="sidebar">
          <div className="input-section">
            <label className="input-label">Input Year</label>
            <input
              type="number"
              value={inputYear}
              onChange={(e) => setInputYear(parseInt(e.target.value))}
              className="year-input"
              placeholder="Enter year"
              min="2020"
              max="2030"
            />
            <button 
              onClick={handleYearSubmit}
              className="generate-btn"
              disabled={loading}
            >
              {loading ? 'Generating...' : 'Generate Forecast'}
            </button>
          </div>

          {error && (
            <div className="error-message">
              {error}
            </div>
          )}

          <div className="forecast-table-section">
            <h3 className="table-title">Annual Forecast for {inputYear}</h3>
            <table className="forecast-table">
              <thead>
                <tr>
                  <th>BINS</th>
                  <th>MAX MAG.</th>
                  <th>NO. OF EQ</th>
                  <th>RISK</th>
                </tr>
              </thead>
              <tbody>
                {forecastData.map((row) => (
                  <tr 
                    key={row.bin_id}
                    className={`bin-row ${selectedBin?.bin_id === row.bin_id ? 'selected' : ''}`}
                    onClick={() => getBinForecast(row.bin_id)}
                    style={{ cursor: 'pointer' }}
                  >
                    <td>BIN {row.bin_id}</td>
                    <td>{row.max_magnitude}</td>
                    <td>{row.num_earthquakes}</td>
                    <td>
                      <span 
                        className="risk-badge"
                        style={{ backgroundColor: getRiskLevelColor(row.risk_level) }}
                      >
                        {row.risk_level.toUpperCase()}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {selectedBin && (
            <div className="bin-details">
              <h3>Region Details</h3>
              <div className="detail-item">
                <strong>Location:</strong> {selectedBin.location}
              </div>
              <div className="detail-item">
                <strong>Confidence:</strong> {(selectedBin.confidence_level * 100).toFixed(1)}%
              </div>
              <div className="detail-item">
                <strong>Pattern:</strong> {selectedBin.historical_pattern}
              </div>
              {selectedBin.recommendations && (
                <div className="recommendations">
                  <strong>Recommendations:</strong>
                  <ul>
                    {selectedBin.recommendations.map((rec, index) => (
                      <li key={index}>{rec}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Main Map Area */}
        <div className="map-area">
          <div className="map-container">
            <MapContainer 
              center={mapCenter} 
              zoom={6} 
              style={{ height: '100%', width: '100%' }}
            >
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              />
              
              {/* Draw geographic bins */}
              {Object.entries(geographicBins).map(([binId, binInfo]) => {
                const forecast = forecastData.find(f => f.bin_id === parseInt(binId));
                const riskColor = forecast ? getRiskLevelColor(forecast.risk_level) : binInfo.color;
                
                return (
                  <Circle
                    key={binId}
                    center={binInfo.coordinates}
                    radius={50000} // 50km radius
                    pathOptions={{
                      color: riskColor,
                      fillColor: riskColor,
                      fillOpacity: 0.3,
                      weight: 2
                    }}
                  />
                );
              })}
              
              {/* Add markers for each bin */}
              {Object.entries(geographicBins).map(([binId, binInfo]) => {
                const forecast = forecastData.find(f => f.bin_id === parseInt(binId));
                
                return (
                  <Marker key={binId} position={binInfo.coordinates}>
                    <Popup>
                      <div className="map-popup">
                        <h4>{binInfo.name}</h4>
                        <p>{binInfo.description}</p>
                        {forecast && (
                          <div className="forecast-info">
                            <p><strong>Max Magnitude:</strong> {forecast.max_magnitude}</p>
                            <p><strong>Earthquakes Expected:</strong> {forecast.num_earthquakes}</p>
                            <p><strong>Risk Level:</strong> 
                              <span 
                                className="risk-badge-small"
                                style={{ backgroundColor: getRiskLevelColor(forecast.risk_level) }}
                              >
                                {forecast.risk_level.toUpperCase()}
                              </span>
                            </p>
                          </div>
                        )}
                      </div>
                    </Popup>
                  </Marker>
                );
              })}
              
              {/* Historical earthquake markers */}
              {historicalData.slice(0, 20).map((eq) => (
                <Marker 
                  key={eq.id} 
                  position={[eq.latitude, eq.longitude]}
                  icon={L.divIcon({
                    className: 'historical-marker',
                    html: `<div style="
                      background-color: ${eq.magnitude >= 6 ? '#dc3545' : eq.magnitude >= 5 ? '#fd7e14' : '#28a745'};
                      width: 8px;
                      height: 8px;
                      border-radius: 50%;
                      border: 2px solid white;
                    "></div>`,
                    iconSize: [12, 12]
                  })}
                >
                  <Popup>
                    <div className="earthquake-popup">
                      <h4>Magnitude {eq.magnitude}</h4>
                      <p><strong>Date:</strong> {new Date(eq.date).toLocaleDateString()}</p>
                      <p><strong>Depth:</strong> {eq.depth} km</p>
                      <p><strong>Location:</strong> {eq.location}</p>
                    </div>
                  </Popup>
                </Marker>
              ))}
            </MapContainer>
          </div>
          
          <div className="forecasting-disclaimer">
            Disclaimer: For informational and research purposes only. 
            This system uses machine learning models and should not be used as the sole basis for emergency decisions.
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForecastPage;