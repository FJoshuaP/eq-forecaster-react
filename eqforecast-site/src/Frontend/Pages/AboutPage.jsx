import React from "react";
import "../Css/AboutPage.css";
import model from "../Pics/model.png";
import gab from "../Pics/gab.jpg";
import ju from "../Pics/ju.jpg";
import jp from "../Pics/jp.jpg";
import kia from "../Pics/kia.jpg";
import group from "../Pics/group.jpg";

const AboutPage = ({ navigateToPage, isLoggedIn }) => {
  const goBack = () => {
    // Navigate to the previous page or landing page
    navigateToPage(3);
  };

  return (
    <div className="about-page-container">
      {/* Header */}
      <div className="about-page-header">
        <button
          onClick={goBack}
          className="about-page-back-btn"
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

        <div className="about-page-header-content">
          <div className="about-page-logo"></div>
          <div className="about-page-nav-menu">
            <button
              onClick={() => navigateToPage(3)}
              className="about-page-nav-item"
            >
              Overview
            </button>
            <button
              onClick={() => navigateToPage(5)}
              className="about-page-nav-item active"
            >
              About
            </button>
            <button
              onClick={() => navigateToPage(6)}
              className="about-page-nav-item"
            >
              Hotlines
            </button>
            <button
              onClick={() => navigateToPage(4)}
              className="about-page-nav-item"
            >
              Awareness
            </button>
            <button
              onClick={() => navigateToPage(7)}
              className="about-page-forecast-btn"
            >
              Forecast Now
            </button>
            <button
              onClick={() => navigateToPage(1)}
              className="about-page-admin-btn"
            >
              Admin
            </button>
          </div>
        </div>
      </div>

      <div className="about-page-main-content">
        {/* About the model section */}
        <h1 className="about-page-title">About the Model</h1>

        <div className="about-page-model-section">
          <div className="about-page-model-content">
            <div className="about-page-model-text">
              <h2 className="about-page-section-title">
                Long Short-Term Memory (LSTM) Networks
              </h2>
              <p className="about-page-section-paragraph">
                Long Short-Term Memory (LSTM) networks are a type of recurrent
                neural network (RNN) built to model sequential data. Since
                earthquakes follow complex time-based patterns, LSTM is
                well-suited for analyzing how past seismic events shape future
                ones.
              </p>
              <p className="about-page-section-paragraph">
                In our system, we use a pure LSTM model to forecast the maximum
                annual earthquake magnitude per region. This focuses on
                identifying the strongest possible seismic events, helping
                provide a clearer picture of potential hazards each year.
              </p>

              <h2 className="about-page-section-title">Attention - LSTM</h2>
              <p className="about-page-section-paragraph">
                While LSTM captures time-based dependencies, it does not always
                distinguish which past events matter most. To address this, we
                integrate an Attention Mechanism—a technique that allows the
                model to prioritize significant seismic signals while minimizing
                less relevant ones.
              </p>
              <p className="about-page-section-paragraph">
                This enhanced Attention-LSTM model is applied to forecast annual
                earthquake frequency. By highlighting critical patterns in
                earthquake history, the attention mechanism strengthens the
                model’s ability to recognize recurring seismic activity and
                improves forecasting accuracy compared to standard LSTM
              </p>

              <h2 className="about-page-section-title">
                Spatio-temporal Forecasting Concept
              </h2>
              <p className="about-page-section-paragraph">
                Spatio-temporal forecasting means looking at earthquakes in both
                time (when they happen) and space (where they happen). By
                combining these two factors, we can see trends in how
                earthquakes affect different regions over the years.
              </p>
              <p className="about-page-section-paragraph">
                This approach uses modern tools to give a clearer picture of
                which areas are at higher risk in the future. The goal is to
                provide easy-to-understand forecasts that help people,
                communities, and decision-makers stay safer and more prepared.
              </p>

              <h2 className="about-page-section-title">
                Quadtree Spatial Binning
              </h2>
              <p className="about-page-section-paragraph">
                Earthquake activity in the Philippines is uneven—some regions
                experience frequent seismic events, while others remain
                relatively quiet. To capture this, we applied Quadtree-based
                Spatial Binning, an adaptive method that divides the country
                into smaller regions or “bins” depending on earthquake density.
              </p>
              <p className="about-page-section-paragraph">
                Active zones are represented with finer bins, while low-activity
                areas are grouped into larger bins. After merging, these bins
                form static spatial zones used by the models. In simple terms,
                bins act as statistical containers that balance earthquake
                distribution across regions, making forecasts more reliable and
                region-specific.
              </p>
            </div>

            <div className="about-page-model-image-container">
              <img
                src={model}
                alt="Model diagram"
                className="about-page-model-image"
              />
            </div>
          </div>
        </div>

        {/* About the team section */}
        <div className="about-page-team-section">
          <div className="about-page-team-content">
            <h2 className="about-page-team-main-title">About the team</h2>

            <div className="about-page-team-intro">
              <div className="about-page-team-image-container">
                <img
                  src={group}
                  alt="Team photo"
                  className="about-page-team-image"
                />
              </div>
              <div className="about-page-team-description">
                <h3 className="about-page-team-section-title">OPAL</h3>

                <p className="about-page-team-paragraph">
                  We are 4th-year Computer Science students from Holy Angel
                  University conducting a research study entitled
                  “Spatiotemporal Earthquake Forecasting in the Philippines
                  Modelling Attention LSTM ” Our study aims to develop a
                  forecasting system that analyzes historical earthquake data
                  from PHIVOLCS to generate annual predictions of earthquake
                  frequency and maximum magnitude per region. The system
                  integrates an Attention-Driven Long Short-Term Memory (LSTM)
                  model with a Quadtree-based spatial binning algorithm and
                  provides results through an interactive visualization
                  platform.
                </p>
              </div>
            </div>

            <h3 className="about-page-team-members-title">
              Meet the team behind OPAL
            </h3>

            <div className="about-page-team-members-grid">
              <div className="about-page-team-member-card">
                <div className="about-page-member-image-container">
                  <img
                    src={ju}
                    alt="Julia Abasolo"
                    className="about-page-member-image"
                  />
                </div>
                <div className="about-page-member-info">
                  <h4 className="about-page-member-name">Abasolo, Julia</h4>
                  <p className="about-page-member-description">
                    Frontend, Documentation
                  </p>
                </div>
              </div>

              <div className="about-page-team-member-card">
                <div className="about-page-member-image-container">
                  <img
                    src={kia}
                    alt="Kiara Laxamana"
                    className="about-page-member-image"
                  />
                </div>
                <div className="about-page-member-info">
                  <h4 className="about-page-member-name">Laxamana, Kiara</h4>
                  <p className="about-page-member-description">
                    Machine Learning, Documentation
                  </p>
                </div>
              </div>

              <div className="about-page-team-member-card">
                <div className="about-page-member-image-container">
                  <img
                    src={gab}
                    alt="Gabriel Ocampo"
                    className="about-page-member-image"
                  />
                </div>
                <div className="about-page-member-info">
                  <h4 className="about-page-member-name">Ocampo, Gabriel</h4>
                  <p className="about-page-member-description">
                    Documentation, UI/UX Designer
                  </p>
                </div>
              </div>

              <div className="about-page-team-member-card">
                <div className="about-page-member-image-container">
                  <img
                    src={jp}
                    alt="Joshua Perez"
                    className="about-page-member-image"
                  />
                </div>
                <div className="about-page-member-info">
                  <h4 className="about-page-member-name">Perez, Joshua</h4>
                  <p className="about-page-member-description">
                    Backend, Documentation
                  </p>
                </div>
              </div>
            </div>

            <div className="about-page-team-disclaimer">
              Disclaimer: For informational and research purposes only
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
