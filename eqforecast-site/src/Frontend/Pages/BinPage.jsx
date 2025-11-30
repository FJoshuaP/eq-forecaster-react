import React, { useState, useEffect } from "react";
import "../Css/BinPage.css";

const BinPage = ({ navigateToPage, isLoggedIn }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [sortConfig, setSortConfig] = useState({ key: "id", direction: "asc" });


  const binsData = [
    {
      id: 0,
      bounds: [119.475, 122.65, 7.0, 12.0],
      width: 3.175,
      height: 5.0,
      area: 15.875,
      center_lat: 9.5,
      center_lon: 121.0625,
      locations: [
        "Southern Mindoro",
        "Panay (Aklan, Antique, Iloilo)",
        "Western Negros (Occidental/Oriental)",
      ],
    },
    {
      id: 1,
      bounds: [125.825, 127.4125, 2.0, 4.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 3.25,
      center_lon: 126.61875,
      locations: [
        "Celebes Sea",
        "Southern Mindanao offshore (Sarangani Bay, Davao Occidental)",
        "Border near Indonesia",
      ],
    },
    {
      id: 2,
      bounds: [127.4125, 129.0, 2.0, 4.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 3.25,
      center_lon: 128.20625,
      locations: [
        "Celebes Sea–Pacific transition (offshore southeast of Mindanao)",
      ],
    },
    {
      id: 3,
      bounds: [125.825, 127.4125, 4.5, 7.0],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 5.75,
      center_lon: 126.61875,
      locations: [
        "Davao Region (Davao Oriental, Occidental, City)",
        "Compostela Valley",
        "Parts of Sarangani",
      ],
    },
    {
      id: 4,
      bounds: [124.2375, 125.825, 7.0, 9.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 8.25,
      center_lon: 125.03125,
      locations: [
        "Bukidnon",
        "Misamis Oriental",
        "Agusan del Sur",
        "Northern Davao del Norte",
        "Northern Cotabato",
      ],
    },
    {
      id: 5,
      bounds: [124.2375, 125.825, 9.5, 12.0],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 10.75,
      center_lon: 125.03125,
      locations: [
        "Northern Agusan del Norte",
        "Northern Surigao del Sur",
        "Northern Mindanao uplands",
        "Southern Leyte",
        "Eastern Samar",
        "Dinagat Islands",
        "Samar",
      ],
    },
    {
      id: 6,
      bounds: [125.825, 127.4125, 7.0, 9.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 8.25,
      center_lon: 126.61875,
      locations: [
        "Surigao del Sur",
        "Davao Oriental",
        "Agusan del Sur",
        "Eastern Mindanao offshore (Philippine Trench)",
      ],
    },
    {
      id: 7,
      bounds: [119.475, 121.0625, 12.0, 14.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 13.25,
      center_lon: 120.26875,
      locations: [
        "Southern Luzon (Mindoro, Marinduque, Batangas, Quezon)",
        "Northern Palawan",
        "Dasmarinas",
        "Muntilupa",
      ],
    },
    {
      id: 8,
      bounds: [119.475, 121.0625, 14.5, 17.0],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 15.75,
      center_lon: 120.26875,
      locations: [
        "Central Luzon (Zambales, Bataan, Pampanga, Nueva Ecija, Pangasinan, Tarlac, Baguio, Cabanatuan)",
        "Metro Manila edge",
        "Olangapo",
        "Bataan",
        "Mariveles",
        "Benguet",
        "La Union",
      ],
    },
    {
      id: 9,
      bounds: [121.0625, 122.65, 14.5, 17.0],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 15.75,
      center_lon: 121.85625,
      locations: [
        "Quezon Province",
        "Pasig",
        "Taguig",
        "Rizal",
        "Tanay",
        "Antipolo",
        "Dona Remedios Trinidad",
        "Montalbon",
        "Quirino",
        "Aurora",
        "Camarines Norte",
        "Polillo Islands",
      ],
    },
    {
      id: 10,
      bounds: [119.475, 121.0625, 17.0, 19.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 18.25,
      center_lon: 120.26875,
      locations: [
        "Ilocos Region (Ilocos Norte, Ilocos Sur, La Union, Pangasinan)",
        "Abra",
        "Vigan",
      ],
    },
    {
      id: 11,
      bounds: [121.0625, 122.65, 17.0, 19.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 18.25,
      center_lon: 121.85625,
      locations: [
        "Nueva Vizcaya",
        "Quirino",
        "Southern Isabela",
        "Tuguegarao",
        "Ilagan",
        "Apayao",
        "Kalinga",
      ],
    },
    {
      id: 12,
      bounds: [119.475, 121.0625, 19.5, 22.0],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 20.75,
      center_lon: 120.26875,
      locations: [
        "Northern Luzon (Cagayan, Apayao, Mountain Province, Kalinga)",
        "Batanes offshore",
      ],
    },
    {
      id: 13,
      bounds: [121.0625, 122.65, 19.5, 22.0],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 20.75,
      center_lon: 121.85625,
      locations: [
        "Eastern Cagayan Valley",
        "Batanes",
        "Northern Isabela",
        "Cagayan up to Babuyan Islands",
      ],
    },
    {
      id: 14,
      bounds: [124.2375, 125.825, 12.0, 14.5],
      width: 1.5875,
      height: 2.5,
      area: 3.97,
      center_lat: 13.25,
      center_lon: 125.03125,
      locations: [
        "Samar",
        "Northern Samar",
        "Masbate",
        "Sorsogon",
        "Albay",
        "Catanduanes",
      ],
    },
    {
      id: 15,
      bounds: [127.4125, 129.0, 4.5, 9.5],
      width: 1.5875,
      height: 5.0,
      area: 7.94,
      center_lat: 7.0,
      center_lon: 128.20625,
      locations: [
        "Philippine Trench (east of Mindanao)",
        "Offshore Davao–Caraga",
      ],
    },
    {
      id: 16,
      bounds: [122.65, 124.2375, 7.0, 12.0],
      width: 1.5875,
      height: 5.0,
      area: 7.94,
      center_lat: 9.5,
      center_lon: 123.44375,
      locations: [
        "Central–Eastern Visayas (Leyte, Samar, Biliran, Cebu, Bohol, Zambonga del Sur, Lanao del Norte, Misamis Occidental, Parts of Zambonga del Norte)",
        "Northern Mindanao coast",
      ],
    },
    {
      id: 17,
      bounds: [121.0625, 124.2375, 12.0, 14.5],
      width: 3.175,
      height: 2.5,
      area: 7.94,
      center_lat: 13.25,
      center_lon: 122.65,
      locations: [
        "Bicol Region (Camarines Norte, Camarines Sur, Albay)",
        "Sibuyan Island",
        "Parts of Masbate",
        "Romblon",
        " Sorosogon",
        "Oriental Mindoro",
        "Marinduque",
        "Catanduanes",
        "Parts of Batangas",
        "Calamba Laguna",
        "Quezon",
      ],
    },
    {
      id: 18,
      bounds: [125.825, 129.0, 12.0, 22.0],
      width: 3.175,
      height: 10.0,
      area: 31.75,
      center_lat: 17.0,
      center_lon: 127.4125,
      locations: [
        "Philippine Trench (east of Luzon & Samar)",
        "Deep Pacific offshore area",
      ],
    },
    {
      id: 19,
      bounds: [124.2375, 125.825, 2.0, 7.0],
      width: 1.5875,
      height: 5.0,
      area: 7.94,
      center_lat: 4.5,
      center_lon: 125.03125,
      locations: [
        "Southern Mindanao (General Santos, South Cotabato, Sarangani, Sultan Kudarat, Davao Occidental, Davao del Sur, Maguindanao del Sur)",
      ],
    },
    {
      id: 20,
      bounds: [125.825, 129.0, 9.5, 12.0],
      width: 3.175,
      height: 2.5,
      area: 7.94,
      center_lat: 10.75,
      center_lon: 127.4125,
      locations: [
        "Eastern Visayas offshore (Samar, Leyte east coast)",
        "Siargao",
        "Socorro",
        "Philippine Trench (Tacloban–Borongan area)",
      ],
    },
    {
      id: 21,
      bounds: [122.65, 125.825, 14.5, 22.0],
      width: 3.175,
      height: 7.5,
      area: 23.81,
      center_lat: 18.25,
      center_lon: 124.2375,
      locations: [
        "Bicol Region (Camarines Sur, Albay, Catanduanes)",
        "Eastern Luzon (Quezon, Aurora, Isabela coastal areas)",
      ],
    },
    {
      id: 22,
      bounds: [116.3, 119.475, 7.0, 22.0],
      width: 3.175,
      height: 15.0,
      area: 47.625,
      center_lat: 14.5,
      center_lon: 117.8875,
      locations: [
        "Palawan",
        "Mindoro",
        "Calamian Islands",
        "Balabac",
        "Spratly Islands vicinity (West Philippine Sea)",
      ],
    },
    {
      id: 23,
      bounds: [116.3, 124.2375, 2.0, 7.0],
      width: 7.9375,
      height: 5.0,
      area: 39.6875,
      center_lat: 4.5,
      center_lon: 120.26875,
      locations: [
        "Sulu Archipelago (Tawi-Tawi, Basilan, Jolo)",
        "Zamboanga City ",
        "Celebes Sea",
      ],
    },
  ];

  const handleSort = (key) => {
    let direction = "asc";
    if (sortConfig.key === key && sortConfig.direction === "asc") {
      direction = "desc";
    }
    setSortConfig({ key, direction });
  };

  const sortedData = [...binsData].sort((a, b) => {
    if (sortConfig.key === "id") {
      return sortConfig.direction === "asc" ? a.id - b.id : b.id - a.id;
    }
    if (sortConfig.key === "area") {
      return sortConfig.direction === "asc" ? a.area - b.area : b.area - a.area;
    }
    if (sortConfig.key === "center_lat") {
      return sortConfig.direction === "asc"
        ? a.center_lat - b.center_lat
        : b.center_lat - a.center_lat;
    }
    if (sortConfig.key === "center_lon") {
      return sortConfig.direction === "asc"
        ? a.center_lon - b.center_lon
        : b.center_lon - a.center_lon;
    }
    return 0;
  });

  const filteredData = sortedData.filter((bin) => {
    const searchLower = searchTerm.toLowerCase();
    return (
      bin.id.toString().includes(searchLower) ||
      bin.locations.some((location) =>
        location.toLowerCase().includes(searchLower)
      ) ||
      bin.center_lat.toString().includes(searchLower) ||
      bin.center_lon.toString().includes(searchLower)
    );
  });

  const goBack = () => {
    navigateToPage(7); 
  };

  return (
    <div className="bin-page-container">
     
      <div className="bin-page-header">
        <button
          onClick={goBack}
          className="bin-page-back-btn"
          title="Go back to forecast"
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

        <div className="bin-page-header-content">
          <div className="bin-page-logo"></div>
          <div className="bin-page-nav-menu">
            <button
              onClick={() => navigateToPage(3)}
              className="bin-page-nav-item"
            >
              Overview
            </button>
            <button
              onClick={() => navigateToPage(5)}
              className="bin-page-nav-item"
            >
              About
            </button>
            <button
              onClick={() => navigateToPage(6)}
              className="bin-page-nav-item"
            >
              Hotlines
            </button>
            <button
              onClick={() => navigateToPage(4)}
              className="bin-page-nav-item"
            >
              Awareness
            </button>
            <button
              onClick={() => navigateToPage(7)}
              className="bin-page-nav-item"
            >
              Forecast Now
            </button>
            <button
              onClick={() => navigateToPage(8)}
              className="bin-page-bins-btn active"
            >
              Bins
            </button>
            {isLoggedIn && (
              <button
                onClick={() => navigateToPage(2)}
                className="bin-page-admin-btn"
              >
                Admin
              </button>
            )}
          </div>
        </div>
      </div>

      <div className="bin-page-content">
      
        <div className="bin-page-title-section">
          <h1 className="bin-page-title">Spatial Bins Overview</h1>
          <p className="bin-page-subtitle">
            Geographic regions used for earthquake forecasting in the
            Philippines
          </p>
        </div>

        
        <div className="bin-page-controls">
          <div className="bin-page-search-container">
            <input
              type="text"
              placeholder="Search bins by ID, location, or coordinates..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="bin-page-search-input"
            />
            <svg
              className="bin-page-search-icon"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </div>

          <div className="bin-page-stats">
            <div className="bin-page-stat-item">
              <span className="bin-page-stat-number">
                {filteredData.length}
              </span>
              <span className="bin-page-stat-label">Total Bins</span>
            </div>
            <div className="bin-page-stat-item">
              <span className="bin-page-stat-number">
                {filteredData
                  .reduce((sum, bin) => sum + bin.area, 0)
                  .toFixed(1)}
                °²
              </span>
              <span className="bin-page-stat-label">Total Area</span>
            </div>
          </div>
        </div>

        
        <div className="bin-page-table-container">
          <table className="bin-page-table">
            <thead>
              <tr>
                <th
                  onClick={() => handleSort("id")}
                  className={`bin-page-sortable ${
                    sortConfig.key === "id"
                      ? "sorted-" + sortConfig.direction
                      : ""
                  }`}
                >
                  BIN ID
                  <span className="bin-page-sort-icon">
                    {sortConfig.key === "id" && sortConfig.direction === "asc"
                      ? "↑"
                      : "↓"}
                  </span>
                </th>
                <th>BOUNDS (LON, LAT)</th>
                <th
                  onClick={() => handleSort("center_lat")}
                  className={`bin-page-sortable ${
                    sortConfig.key === "center_lat"
                      ? "sorted-" + sortConfig.direction
                      : ""
                  }`}
                >
                  CENTER LAT
                  <span className="bin-page-sort-icon">
                    {sortConfig.key === "center_lat" &&
                    sortConfig.direction === "asc"
                      ? "↑"
                      : "↓"}
                  </span>
                </th>
                <th
                  onClick={() => handleSort("center_lon")}
                  className={`bin-page-sortable ${
                    sortConfig.key === "center_lon"
                      ? "sorted-" + sortConfig.direction
                      : ""
                  }`}
                >
                  CENTER LON
                  <span className="bin-page-sort-icon">
                    {sortConfig.key === "center_lon" &&
                    sortConfig.direction === "asc"
                      ? "↑"
                      : "↓"}
                  </span>
                </th>
                <th>DIMENSIONS</th>
                <th
                  onClick={() => handleSort("area")}
                  className={`bin-page-sortable ${
                    sortConfig.key === "area"
                      ? "sorted-" + sortConfig.direction
                      : ""
                  }`}
                >
                  AREA (°²)
                  <span className="bin-page-sort-icon">
                    {sortConfig.key === "area" && sortConfig.direction === "asc"
                      ? "↑"
                      : "↓"}
                  </span>
                </th>
                <th>MAJOR LOCATIONS</th>
              </tr>
            </thead>
            <tbody>
              {filteredData.map((bin) => (
                <tr key={bin.id}>
                  <td>
                    <span className="bin-page-bin-id">BIN {bin.id}</span>
                  </td>
                  <td className="bin-page-bounds-cell">
                    <div className="bin-page-bounds-grid">
                      <div>
                        SW: ({bin.bounds[0]}°, {bin.bounds[2]}°)
                      </div>
                      <div>
                        NE: ({bin.bounds[1]}°, {bin.bounds[3]}°)
                      </div>
                    </div>
                  </td>
                  <td>
                    <span className="bin-page-coord">{bin.center_lat}°</span>
                  </td>
                  <td>
                    <span className="bin-page-coord">{bin.center_lon}°</span>
                  </td>
                  <td className="bin-page-dimensions-cell">
                    <div className="bin-page-dimensions">
                      <span>
                        {bin.width}° × {bin.height}°
                      </span>
                    </div>
                  </td>
                  <td>
                    <span className="bin-page-area-value">{bin.area}</span>
                  </td>
                  <td className="bin-page-locations-cell">
                    <div className="bin-page-locations">
                      {bin.locations.map((location, index) => (
                        <span key={index} className="bin-page-location-tag">
                          {location}
                        </span>
                      ))}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {filteredData.length === 0 && (
          <div className="bin-page-no-results">
            <p>No bins found matching your search criteria.</p>
          </div>
        )}

       
        <div className="bin-page-info-note">
          <div className="bin-page-note-icon">ℹ️</div>
          <div>
            <strong>About Spatial Bins:</strong> These geographic regions are
            used to divide the Philippines into manageable areas for earthquake
            forecasting. Each bin represents a specific coordinate range where
            seismic activity is monitored and analyzed. The forecasting model
            uses historical earthquake data within these bins to predict future
            seismic events.
          </div>
        </div>
      </div>
    </div>
  );
};

export default BinPage;
