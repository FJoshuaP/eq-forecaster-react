import React, { useState } from "react";
import "../Css/Forecasting.css";

const ForecastPage = ({ navigateToPage }) => {
  const [inputYear, setInputYear] = useState("");
  const [forecastData, setForecastData] = useState([
    { bin: 1, maxMag: "-", noOfEq: "-" },
    { bin: 2, maxMag: "-", noOfEq: "-" },
    { bin: 3, maxMag: "-", noOfEq: "-" },
    { bin: 4, maxMag: "-", noOfEq: "-" },
  ]);

  const handleYearSubmit = () => {
    // Handle forecast generation logic here
    console.log("Generating forecast for year:", inputYear);
  };

  return (
    <div className="forecast-page-container">
      {/* Header */}
      <div className="header">
        <div className="header-content">
          <div className="logo">OPAL</div>
          <div className="nav-menu">
            <button
              onClick={() => navigateToPage(1)}
              className="nav-item"
            >
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
              onChange={(e) => setInputYear(e.target.value)}
              className="year-input"
              placeholder="Enter year"
            />
          </div>

          <div className="forecast-table-section">
            <h3 className="table-title">Annual Forecast for the Year ----</h3>
            <table className="forecast-table">
              <thead>
                <tr>
                  <th>BINS</th>
                  <th>MAX MAG.</th>
                  <th>NO. OF EQ</th>
                </tr>
              </thead>
              <tbody>
                {forecastData.map((row, index) => (
                  <tr key={index}>
                    <td>BIN {row.bin}</td>
                    <td>{row.maxMag}</td>
                    <td>{row.noOfEq}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="bin-selection-section">
            <h3 className="selection-title">Select a BIN</h3>
            <div className="bin-id-label">BIN ID NO.</div>
          </div>
        </div>

        {/* Main Map Area */}
        <div className="map-area">
          <div className="map-container">
            {/* Philippines Map with colored regions */}
            <div className="philippines-map">
              {/* Map regions - simplified representation */}
              <div className="map-grid">
                {/* Top row */}
                <div className="map-cell green"></div>
                <div className="map-cell green"></div>
                <div className="map-cell red"></div>
                <div className="map-cell brown"></div>
                
                {/* Second row */}
                <div className="map-cell green"></div>
                <div className="map-cell green"></div>
                <div className="map-cell red"></div>
                <div className="map-cell brown"></div>
                
                {/* Third row */}
                <div className="map-cell green"></div>
                <div className="map-cell green"></div>
                <div className="map-cell red"></div>
                <div className="map-cell brown"></div>
                
                {/* Fourth row */}
                <div className="map-cell green"></div>
                <div className="map-cell brown"></div>
                <div className="map-cell purple"></div>
                <div className="map-cell brown"></div>
              </div>
              
              {/* Location markers */}
              <div className="location-markers">
                <div className="marker" style={{top: '15%', left: '25%'}}>
                  <span className="marker-icon">📍</span>
                  <span className="marker-label">Baguio</span>
                </div>
                <div className="marker" style={{top: '30%', left: '45%'}}>
                  <span className="marker-icon">📍</span>
                  <span className="marker-label">Angeles</span>
                </div>
                <div className="marker" style={{top: '45%', left: '35%'}}>
                  <span className="marker-icon">📍</span>
                  <span className="marker-label">Manila</span>
                </div>
                <div className="marker attention-marker" style={{top: '65%', left: '55%'}}>
                  <span className="attention-icon">⚠️</span>
                  <span className="attention-label">ATTENTION DEFICIT</span>
                </div>
                <div className="marker" style={{bottom: '15%', right: '25%'}}>
                  <span className="marker-icon">📍</span>
                  <span className="marker-label">Davao</span>
                </div>
              </div>
            </div>
          </div>
          
          <div className="forecasting-disclaimer">
            Disclaimer: For informational and research purposes only
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForecastPage;