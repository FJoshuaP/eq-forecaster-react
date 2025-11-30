import React from "react";
import "../Css/LandingPage.css";
import map from "../Pics/map.png";
import eq_visual from "../Pics/eq_visual.png";

const LandingPage = ({ navigateToPage, isLoggedIn }) => {
  const goBack = () => {
    navigateToPage(1);
  };

  return (
    <div className="landing-page-container">
      <div className="landing-page-header">
        

        <div className="landing-page-header-content">
          <div className="landing-page-logo"></div>
          <div className="landing-page-nav-menu">
            <button
              onClick={() => navigateToPage(3)}
              className="landing-page-nav-item active"
            >
              Overview
            </button>
            <button
              onClick={() => navigateToPage(5)}
              className="landing-page-nav-item"
            >
              About
            </button>
            <button
              onClick={() => navigateToPage(6)}
              className="landing-page-nav-item"
            >
              Hotlines
            </button>
            <button
              onClick={() => navigateToPage(4)}
              className="landing-page-nav-item"
            >
              Awareness
            </button>
            <button
              onClick={() => navigateToPage(7)}
              className="landing-page-forecast-btn"
            >
              Forecast Now
            </button>
          </div>
        </div>
      </div>

      
      <div className="landing-page-hero-section">
        <h1 className="landing-page-hero-title">Earthquake Forecasting</h1>
        <p className="landing-page-hero-subtitle">
          Earthquake Forecasting in the Philippines Modelling Attention-Driven
          LSTM
        </p>
        <button
          onClick={() => navigateToPage(7)}
          className="landing-page-hero-cta-btn"
        >
          Forecast Now
        </button>
      </div>

      
      <div className="landing-page-map-section">
        <div className="landing-page-map-container">
          <img
            src={map}
            alt="Philippines Map"
            className="landing-page-map-image"
          />
        </div>
      </div>

      
      <div className="landing-page-content-section">
        <div className="landing-page-content-grid">
          <div className="landing-page-content-text">
            <h2 className="landing-page-content-title">
              Earthquake Forecasting
            </h2>
            <p className="landing-page-content-paragraph">
              Earthquake forecasting uses historical seismic data and artificial
              intelligence to identify patterns in earthquake frequency,
              magnitude, and location. While it cannot predict the exact time or
              epicenter of an event, it provides valuable insights into regional
              seismic risks.
            </p>
            <p className="landing-page-content-paragraph">
              By leveraging advanced models such as Long Short-Term Memory
              (LSTM) networks with attention mechanisms and spatial binning
              techniques, forecasting systems can detect hidden patterns in
              complex datasets. These forecasts support disaster preparedness,
              guide urban planning, and strengthen resilience by helping
              communities and policymakers anticipate potential seismic hazards.
              Ultimately, earthquake forecasting bridges science and technology
              to provide data-driven solutions for safer societies.
            </p>
          </div>
          <div className="landing-page-content-image-container">
            <img
              src={eq_visual}
              alt="Earthquake visualization"
              className="landing-page-content-image"
            />
          </div>
        </div>
      </div>

      
      <div className="landing-page-bottom-cta">
        <h2 className="landing-page-cta-title">
          Want to know more about the model?
        </h2>
        <p className="landing-page-cta-subtitle">
          Earthquake Forecasting in the Philippines Modelling Attention-Driven
          LSTM
        </p>
        <div className="landing-page-cta-buttons">
          <button
            onClick={() => navigateToPage(5)}
            className="landing-page-cta-btn-secondary"
          >
            About
          </button>
          <button
            onClick={() => navigateToPage(7)}
            className="landing-page-cta-btn-primary"
          >
            Forecast Now
          </button>
        </div>
      </div>
      <div className="landing-page-disclaimer">
        Disclaimer: For informational and research purposes only
      </div>
    </div>
  );
};

export default LandingPage;
