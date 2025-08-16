import React from "react";
import "../Css/LandingPage.css";

const LandingPage = ({ navigateToPage }) => {
  return (
    <div className="landing-page-container">
      {/* Header */}
      <div className="header">
        <div className="header-content">
          <div className="logo">OPAL</div>
          <div className="nav-menu">
            <button
              onClick={() => navigateToPage(1)}
              className="nav-item active"
            >
              Overview
            </button>

            <button onClick={() => navigateToPage(3)} className="nav-item">
              About
            </button>
            <button onClick={() => navigateToPage(4)} className="nav-item">
              Hotlines
            </button>
            <button onClick={() => navigateToPage(2)} className="nav-item">Awareness</button>
            <button onClick={() => navigateToPage(5)}  className="forecast-btn">Forecast Now</button>
          </div>
        </div>
      </div>

      {/* Main Hero Section */}
      <div className="hero-section">
        <h1 className="hero-title">OPAL Earthquake Forecasting</h1>
        <p className="hero-subtitle">
          Regional Earthquake Forecasting in the PH Modelling Attention-Driven
          LSTM
        </p>
        <button onClick={() => navigateToPage(5)} className="hero-cta-btn">
          Forecast Now
        </button>
      </div>

      {/* Map Section */}
      <div className="map-section">
        <div className="map-container">
          <img
            src="/api/placeholder/1200/400"
            alt="Philippines Map"
            className="map-image"
          />
        </div>
      </div>

      {/* Content Section */}
      <div className="content-section">
        <div className="content-grid">
          <div className="content-text">
            <h2 className="content-title">Earthquake Forecasting</h2>
            <p className="content-paragraph">
              Body text for your whole article or post. We'll put in some lorem
              ipsum to show how a filled-out page might look.
            </p>
            <p className="content-paragraph">
              Excepteur efficient emerging, minim veniam anim aute carefully
              curated Ginza conversation exquisite perfect nostrud nisi
              intricate Content. Qui international first-class nulla ut.
              Punctual adipiscing, essential lovely queen tempor eiusmod irure.
              Exclusive izakaya charming Scandinavian impeccable aute quality of
              life soft power pariatur Melbourne consectetur discerning. Qui
              wardrobe aliquip, et Porter destination Toto remarkable officia
              Helsinki excepteur Basset hound. Zürich sleepy perfect
              consectetur.
            </p>
          </div>
          <div className="content-image-container">
            <img
              src="/api/placeholder/400/250"
              alt="Earthquake visualization"
              className="content-image"
            />
          </div>
        </div>
      </div>

      {/* Bottom CTA Section */}
      <div className="bottom-cta">
        <h2 className="cta-title">Want to know more about the model?</h2>
        <p className="cta-subtitle">
          Regional Earthquake Forecasting in the PH Modelling Attention-Driven
          LSTM
        </p>
        <div className="cta-buttons">
          <button
            onClick={() => navigateToPage(3)}
            className="cta-btn-secondary"
          >
            About
          </button>
          <button onClick={() => navigateToPage(5)} className="cta-btn-primary">
            Forecast Now
            </button>
        </div>
        <div className="disclaimer">
          Disclaimer: For informational and research purposes only
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
