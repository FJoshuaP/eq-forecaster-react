import React, { useState, useEffect } from "react";
import {
  MapContainer,
  TileLayer,
  Polygon,
  Tooltip,
  Popup,
} from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "../Css/Forecasting.css";
import { supabase } from "../supabase";

const ForecastPage = ({ navigateToPage, isLoggedIn }) => {
  const [spatialBins, setSpatialBins] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [availableYears, setAvailableYears] = useState([]);
  const [selectedYear, setSelectedYear] = useState(2025);
  const [forecastData, setForecastData] = useState({});
  const [forecastLoading, setForecastLoading] = useState(false);

  
  const hardcodedBins = [
    {
      id: 0,
      bounds: [119.475, 122.65, 7.0, 12.0],
      earthquake_count: 69,
      max_magnitude: 0,
      width: 3.175,
      height: 5.0,
    },
    {
      id: 1,
      bounds: [125.825, 127.4125, 2.0, 4.5],
      earthquake_count: 182,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 2,
      bounds: [127.4125, 129.0, 2.0, 4.5],
      earthquake_count: 70,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 3,
      bounds: [125.825, 127.4125, 4.5, 7.0],
      earthquake_count: 227,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 4,
      bounds: [124.2375, 125.825, 7.0, 9.5],
      earthquake_count: 61,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 5,
      bounds: [124.2375, 125.825, 9.5, 12.0],
      earthquake_count: 114,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 6,
      bounds: [125.825, 127.4125, 7.0, 9.5],
      earthquake_count: 283,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 7,
      bounds: [119.475, 121.0625, 12.0, 14.5],
      earthquake_count: 108,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 8,
      bounds: [119.475, 121.0625, 14.5, 17.0],
      earthquake_count: 98,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 9,
      bounds: [121.0625, 122.65, 14.5, 17.0],
      earthquake_count: 100,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 10,
      bounds: [119.475, 121.0625, 17.0, 19.5],
      earthquake_count: 105,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 11,
      bounds: [121.0625, 122.65, 17.0, 19.5],
      earthquake_count: 79,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 12,
      bounds: [119.475, 121.0625, 19.5, 22.0],
      earthquake_count: 46,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 13,
      bounds: [121.0625, 122.65, 19.5, 22.0],
      earthquake_count: 96,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 14,
      bounds: [124.2375, 125.825, 12.0, 14.5],
      earthquake_count: 131,
      max_magnitude: 0,
      width: 1.5875,
      height: 2.5,
    },
    {
      id: 15,
      bounds: [127.4125, 129.0, 4.5, 9.5],
      earthquake_count: 63,
      max_magnitude: 0,
      width: 1.5875,
      height: 5.0,
    },
    {
      id: 16,
      bounds: [122.65, 124.2375, 7.0, 12.0],
      earthquake_count: 67,
      max_magnitude: 0,
      width: 1.5875,
      height: 5.0,
    },
    {
      id: 17,
      bounds: [121.0625, 124.2375, 12.0, 14.5],
      earthquake_count: 75,
      max_magnitude: 0,
      width: 3.175,
      height: 2.5,
    },
    {
      id: 18,
      bounds: [125.825, 129.0, 12.0, 22.0],
      earthquake_count: 38,
      max_magnitude: 0,
      width: 3.175,
      height: 10.0,
    },
    {
      id: 19,
      bounds: [124.2375, 125.825, 2.0, 7.0],
      earthquake_count: 115,
      max_magnitude: 0,
      width: 1.5875,
      height: 5.0,
    },
    {
      id: 20,
      bounds: [125.825, 129.0, 9.5, 12.0],
      earthquake_count: 237,
      max_magnitude: 0,
      width: 3.175,
      height: 2.5,
    },
    {
      id: 21,
      bounds: [122.65, 125.825, 14.5, 22.0],
      earthquake_count: 22,
      max_magnitude: 0,
      width: 3.175,
      height: 7.5,
    },
    {
      id: 22,
      bounds: [116.3, 119.475, 7.0, 22.0],
      earthquake_count: 37,
      max_magnitude: 0,
      width: 3.175,
      height: 15.0,
    },
    {
      id: 23,
      bounds: [116.3, 124.2375, 2.0, 7.0],
      earthquake_count: 75,
      max_magnitude: 0,
      width: 7.9375,
      height: 5.0,
    },
  ];

  
  useEffect(() => {
    setSpatialBins(hardcodedBins);
  }, []);

  
  useEffect(() => {
    const fetchAvailableYears = async () => {
      try {
        const { data, error } = await supabase.from("forecasts").select("year");

        if (error) {
          return;
        }

        
        const uniqueYears = [
          ...new Set(data.map((record) => record.year)),
        ].sort();
        setAvailableYears(uniqueYears);

     
        if (uniqueYears.includes(2025)) {
          setSelectedYear(2025);
        } else if (uniqueYears.length > 0) {
          setSelectedYear(uniqueYears[uniqueYears.length - 1]);
        }
      } catch (error) {
       
      }
    };

    fetchAvailableYears();
  }, []);

 
  useEffect(() => {
    const fetchForecastData = async () => {
      if (!selectedYear) return;

      try {
        setForecastLoading(true);

        const { data, error } = await supabase
          .from("forecasts")
          .select("bin_id, year, forecast_frequency, forecast_max_mag")
          .eq("year", selectedYear)
          .order("bin_id");

        if (error) {
          setError("Failed to fetch forecast data");
          return;
        }

        
        const forecastMap = {};
        data.forEach((forecast) => {
          
          const numericId = parseInt(forecast.bin_id);
          forecastMap[numericId] = forecast;
        });

        setForecastData(forecastMap);
        setError(null);
      } catch (error) {
        setError("Failed to fetch forecast data");
      } finally {
        setForecastLoading(false);
      }
    };

    fetchForecastData();
  }, [selectedYear]);

  
  const regions = hardcodedBins.map((bin) => {
    const forecast = forecastData[bin.id];
    return {
      id: bin.id,
      name: `Bin ${bin.id}`,
      bin: bin.id,
      positions: [
        [bin.bounds[2], bin.bounds[0]], 
        [bin.bounds[2], bin.bounds[1]], 
        [bin.bounds[3], bin.bounds[1]], 
        [bin.bounds[3], bin.bounds[0]], 
      ],
      earthquake_count: bin.earthquake_count || 0,
      max_magnitude: bin.max_magnitude || 0,
      forecast: forecast
        ? {
            forecast_frequency: forecast.forecast_frequency,
            forecast_max_mag: forecast.forecast_max_mag,
          }
        : null,
    };
  });

  const goBack = () => {
    navigateToPage(3);
  };

  const handleYearSubmit = () => {
    
  };

  


  return (
    <div className="forecast-page-container">
      
      <div className="forecast-page-header">
        <button
          onClick={goBack}
          className="forecast-page-back-btn"
          title="Go back"
        >
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>

        <div className="forecast-page-header-content">
          <div className="forecast-page-logo"></div>
          <div className="forecast-page-nav-menu">
            <button
              onClick={() => navigateToPage(3)}
              className="forecast-page-nav-item"
            >
              Overview
            </button>
            <button
              onClick={() => navigateToPage(5)}
              className="forecast-page-nav-item"
            >
              About
            </button>
            <button
              onClick={() => navigateToPage(6)}
              className="forecast-page-nav-item"
            >
              Hotlines
            </button>
            <button
              onClick={() => navigateToPage(4)}
              className="forecast-page-nav-item"
            >
              Awareness
            </button>
            <button
              onClick={() => navigateToPage(7)}
              className="forecast-page-forecast-btn active"
            >
              Forecast Now
            </button>
            <button
              onClick={() => navigateToPage(8)}
              className="forecast-page-bins-btn"
            >
              Bins
            </button>
            {isLoggedIn && (
              <button
                onClick={() => navigateToPage(2)}
                className="forecast-page-admin-btn"
              >
                Admin
              </button>
            )}
          </div>
        </div>
      </div>

      <div className="forecast-page-content">
        
        <div className="forecast-page-sidebar">
          <div className="forecast-page-input-section">
            <label className="forecast-page-input-label">
              Select Historical Year (1960-{Math.max(...availableYears)})
            </label>
            <select
              value={selectedYear}
              onChange={(e) => setSelectedYear(parseInt(e.target.value))}
              className="forecast-page-year-input"
            >
              {availableYears.map((year) => (
                <option key={year} value={year}>
                  {year}
                </option>
              ))}
            </select>
            <div style={{ fontSize: "12px", color: "#666", marginTop: "5px" }}>
              {availableYears.length} years available:{" "}
              {Math.min(...availableYears)} - {Math.max(...availableYears)}
            </div>
          </div>

          <div className="forecast-page-table-section">
            <h3 className="forecast-page-table-title">
              Earthquake Forecast for {selectedYear} ({hardcodedBins.length}{" "}
              bins)
            </h3>

            {loading && (
              <div style={{ textAlign: "center", padding: "20px" }}>
                Loading earthquake data for {selectedYear}...
              </div>
            )}

            {error && (
              <div
                style={{ textAlign: "center", padding: "20px", color: "red" }}
              >
                {error}
              </div>
            )}

            {!loading && !error && (
              <div className="forecast-page-table-container">
                <table className="forecast-page-table">
                  <thead>
                    <tr>
                      <th>BIN ID</th>
                      <th>FORECAST FREQUENCY</th>
                      <th>FORECAST MAX MAGNITUDE</th>
                      <th>RISK LEVEL</th>
                    </tr>
                  </thead>
                  <tbody>
                    {hardcodedBins.map((bin, index) => {
                      const forecast = forecastData[bin.id];
                      return (
                        <tr key={index}>
                          <td>BIN {bin.id}</td>
                          <td>
                            {forecast ? (
                              <span
                                style={{ color: "black", fontWeight: "bold" }}
                              >
                                {Math.round(forecast.forecast_frequency) ||
                                  "N/A"}
                              </span>
                            ) : (
                              <span
                                style={{ color: "#666", fontStyle: "italic" }}
                              >
                                No forecast data
                              </span>
                            )}
                          </td>
                          <td>
                            {forecast ? (
                              <span
                                style={{ color: "black", fontWeight: "bold" }}
                              >
                                {forecast.forecast_max_mag?.toFixed(1) || "N/A"}
                              </span>
                            ) : (
                              <span
                                style={{ color: "#666", fontStyle: "italic" }}
                              >
                                No forecast data
                              </span>
                            )}
                          </td>
                          <td>
                            {forecast ? (
                              (() => {
                                const maxMag = forecast.forecast_max_mag;
                                if (maxMag >= 7.0) {
                                  return (
                                    <span
                                      style={{
                                        color: "#dc2626",
                                        fontWeight: "bold",
                                      }}
                                    >
                                      HIGH
                                    </span>
                                  );
                                } else if (maxMag >= 6.1) {
                                  return (
                                    <span
                                      style={{
                                        color: "#f59e0b",
                                        fontWeight: "bold",
                                      }}
                                    >
                                      MEDIUM
                                    </span>
                                  );
                                } else if (maxMag >= 5.0) {
                                  return (
                                    <span
                                      style={{
                                        color: "#10b981",
                                        fontWeight: "bold",
                                      }}
                                    >
                                      LOW
                                    </span>
                                  );
                                } else {
                                  return (
                                    <span
                                      style={{
                                        color: "#6b7280",
                                        fontWeight: "bold",
                                      }}
                                    >
                                      MINIMAL
                                    </span>
                                  );
                                }
                              })()
                            ) : (
                              <span
                                style={{ color: "#666", fontStyle: "italic" }}
                              >
                                No forecast data
                              </span>
                            )}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
            <div className="forecast-page-note">
              The predictions shown only cover stronger earthquakes (
              <b>magnitude 5.0 and above</b>) that happen close to the surface (
              <b>within 70 km deep</b>). Smaller or deeper earthquakes are not
              included in these forecasts.
            </div>
          </div>
        </div>

        
        <div className="forecast-page-map-area">
          <div className="forecast-page-map-container">
            <MapContainer
              center={[12.8797, 121.774]}
              zoom={6}
              style={{ height: "100%", width: "100%" }}
            >
              <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />

              
              {regions.map((region, index) => (
                <Polygon
                  key={index}
                  positions={region.positions}
                  pathOptions={{
                    fillColor: (() => {
                      if (region.forecast) {
                        const maxMag = region.forecast.forecast_max_mag;
                        if (maxMag >= 7.0) return "#dc2626"; // Red for HIGH
                        if (maxMag >= 6.1) return "#f59e0b"; // Orange for MEDIUM
                        if (maxMag >= 5.0) return "#86efac"; // Light green for LOW
                        return "#6b7280"; // Gray for MINIMAL
                      }
                      return "transparent";
                    })(),
                    fillOpacity: 0.3,
                    color: "black",
                    weight: 1.5,
                    opacity: 1.0,
                  }}
                >
                  <Tooltip
                    permanent={false}
                    direction="top"
                    offset={[0, -10]}
                    opacity={0.9}
                    className="bin-tooltip"
                  >
                    <div
                      style={{
                        minWidth: "180px",
                        fontSize: "12px",
                        lineHeight: "1.4",
                        textAlign: "center",
                      }}
                    >
                      <div
                        style={{
                          fontWeight: "bold",
                          marginBottom: "8px",
                          fontSize: "14px",
                        }}
                      >
                        Bin {region.bin}
                      </div>
                      {region.forecast ? (
                        <>
                          <div
                            style={{
                              marginBottom: "4px",
                              color: "white",
                              fontWeight: "bold",
                            }}
                          >
                            <strong>{selectedYear} FORECAST:</strong>
                          </div>
                          <div style={{ marginBottom: "4px", color: "white" }}>
                            <strong>Frequency:</strong>{" "}
                            {Math.round(region.forecast.forecast_frequency) ||
                              "N/A"}
                          </div>
                          <div style={{ marginBottom: "4px", color: "white" }}>
                            <strong>Max Magnitude:</strong>{" "}
                            {region.forecast.forecast_max_mag?.toFixed(1) ||
                              "N/A"}
                          </div>
                        </>
                      ) : (
                        <div
                          style={{
                            marginBottom: "4px",
                            color: "#666",
                            fontStyle: "italic",
                          }}
                        >
                          No forecast data available
                        </div>
                      )}
                    </div>
                  </Tooltip>
                </Polygon>
              ))}
            </MapContainer>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForecastPage;
