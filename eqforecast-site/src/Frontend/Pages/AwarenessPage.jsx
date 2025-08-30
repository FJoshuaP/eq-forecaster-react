import React from "react";
import "../Css/AwarenessPage.css";
import dch from "../Pics/dch.png";

const AwarenessPage = ({ navigateToPage, isLoggedIn }) => {
  const goBack = () => {
    navigateToPage(3);
  };

  return (
    <div className="awareness-page-container">
      {/* Header */}
      <div className="awareness-page-header">
        <button
          onClick={goBack}
          className="awareness-page-back-btn"
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

        <div className="awareness-page-header-content">
          <div className="awareness-page-logo"></div>
          <div className="awareness-page-nav-menu">
            <button
              onClick={() => navigateToPage(3)}
              className="awareness-page-nav-item"
            >
              Overview
            </button>
            <button
              onClick={() => navigateToPage(5)}
              className="awareness-page-nav-item"
            >
              About
            </button>
            <button
              onClick={() => navigateToPage(6)}
              className="awareness-page-nav-item"
            >
              Hotlines
            </button>
            <button
              onClick={() => navigateToPage(4)}
              className="awareness-page-nav-item active"
            >
              Awareness
            </button>
            <button
              onClick={() => navigateToPage(7)}
              className="awareness-page-forecast-btn"
            >
              Forecast Now
            </button>
            <button
              onClick={() => navigateToPage(1)}
              className="awareness-page-admin-btn"
            >
              Admin
            </button>
          </div>
        </div>
      </div>

      {/* Main Hero Section */}
      <div className="awareness-page-hero-section">
        <h1 className="awareness-page-hero-title">
          What to do BEFORE, DURING, and AFTER an earthquake?
        </h1>
      </div>

      {/* Before Section */}
      <div className="awareness-page-before-section">
        <h2 className="awareness-page-section-title">
          BEFORE an earthquake, you should...
        </h2>

        <div className="awareness-page-before-grid">
          <div className="awareness-page-before-column">
            <h3 className="awareness-page-subsection-title">
              Create an emergency plan
            </h3>
            <ul className="awareness-page-info-list">
              <li>
                Identify safe spots in each room (e.g., under sturdy tables,
                away from windows).
              </li>
              <li>Designate meeting points outside your home.</li>
              <li>Know evacuation routes and emergency contacts.</li>
            </ul>

            <h3 className="awareness-page-subsection-title">
              Build an emergency kit
            </h3>
            <ul className="awareness-page-info-list">
              <li>
                Include water, food, flashlight, batteries, first aid supplies,
                medications, important documents, and cash.
              </li>
            </ul>
          </div>

          <div className="awareness-page-before-column">
            <h3 className="awareness-page-subsection-title">
              Secure your environment
            </h3>
            <ul className="awareness-page-info-list">
              <li>Anchor heavy furniture and appliances to walls.</li>
              <li>Store breakable items on low shelves.</li>
              <li>Repair structural weaknesses in your home if possible.</li>
            </ul>

            <h3 className="awareness-page-subsection-title">Stay informed</h3>
            <ul className="awareness-page-info-list">
              <li>Know your area's risk level.</li>
              <li>
                Install apps or follow official government agencies (like
                PHIVOLCS in the Philippines) for alerts.
              </li>
            </ul>
          </div>
        </div>
      </div>

      {/* During Section */}
      <div className="awareness-page-during-section">
        <h2 className="awareness-page-section-title">
          DURING an earthquake, you should...
        </h2>

        <div className="awareness-page-during-content">
          <div className="awareness-page-during-main">
            <div className="awareness-page-drop-cover-hold">
              <h3 className="awareness-page-subsection-title">
                DROP, COVER, and HOLD ON
              </h3>
              <ol className="awareness-page-numbered-list">
                <li>Drop to the ground.</li>
                <li>Take cover under a sturdy piece of furniture.</li>
                <li>Hold on until the shaking stops.</li>
              </ol>

              <ul className="awareness-page-info-list">
                <li>
                  Stay away from windows, mirrors, glass, and heavy objects.
                </li>
                <li>Do not use elevators.</li>
                <li>
                  If you're in bed, stay there and protect your head with a
                  pillow.
                </li>
              </ul>
            </div>

            <div className="awareness-page-during-scenarios">
              <div className="awareness-page-scenario">
                <h4 className="awareness-page-scenario-title">
                  If OUTDOORS....
                </h4>
                <ul className="awareness-page-info-list">
                  <li>
                    Move to an open area away from buildings, trees,
                    streetlights, and utility wires.
                  </li>
                  <li>
                    Drop to the ground and stay there until the shaking stops.
                  </li>
                </ul>
              </div>

              <div className="awareness-page-scenario">
                <h4 className="awareness-page-scenario-title">
                  If in a VEHICLE...
                </h4>
                <ul className="awareness-page-info-list">
                  <li>Pull over to a safe area and stop.</li>
                  <li>Avoid overpasses, bridges, and power lines.</li>
                  <li>Stay inside the vehicle until the shaking stops.</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="awareness-page-during-image">
            <img
              src={dch}
              alt="Drop, Cover, and Hold On demonstration"
              className="awareness-page-demo-image"
            />
          </div>
        </div>
      </div>

      {/* After Section */}
      <div className="awareness-page-after-section">
        <h2 className="awareness-page-section-title">
          AFTER an earthquake, you should...
        </h2>

        <div className="awareness-page-after-grid">
          <div className="awareness-page-after-item">
            <h3 className="awareness-page-after-number">
              1. Check yourself and others for injuries
            </h3>
            <ul className="awareness-page-info-list">
              <li>Provide first aid if trained and necessary.</li>
            </ul>
          </div>

          <div className="awareness-page-after-item">
            <h3 className="awareness-page-after-number">
              2. Inspect your surroundings.
            </h3>
            <ul className="awareness-page-info-list">
              <li>Be alert for gas leaks, fire, or structural damage.</li>
              <li>
                Don't use electrical switches or open flames if a gas leak is
                suspected.
              </li>
            </ul>
          </div>

          <div className="awareness-page-after-item">
            <h3 className="awareness-page-after-number">
              3. Be prepared for aftershocks.
            </h3>
            <ul className="awareness-page-info-list">
              <li>These can be strong and cause additional damage.</li>
            </ul>
          </div>

          <div className="awareness-page-after-item">
            <h3 className="awareness-page-after-number">
              4. Listen to official sources
            </h3>
            <ul className="awareness-page-info-list">
              <li>
                Use a battery-powered radio or mobile phone to get updates from
                local authorities.
              </li>
            </ul>
          </div>

          <div className="awareness-page-after-item">
            <h3 className="awareness-page-after-number">
              5. Avoid unnecessary travel
            </h3>
            <ul className="awareness-page-info-list">
              <li>Keep roads clear for emergency vehicles.</li>
            </ul>
          </div>

          <div className="awareness-page-after-item">
            <h3 className="awareness-page-after-number">
              6. If you're in a tsunami-prone area:
            </h3>
            <ul className="awareness-page-info-list">
              <li>
                Move to higher ground immediately after the shaking stops.
              </li>
              <li>
                Do not wait for an official warning if you're near the coast and
                the shaking is strong or prolonged.
              </li>
            </ul>
          </div>
        </div>
      </div>

      {/* Bottom CTA Section */}
      <div className="awareness-page-bottom-cta">
        <h2 className="awareness-page-cta-title">
          Want to know more about the model?
        </h2>
        <p className="awareness-page-cta-subtitle">
          Regional Earthquake Forecasting in the PH Modelling Attention-Driven
          LSTM
        </p>
        <div className="awareness-page-cta-buttons">
          <button
            onClick={() => navigateToPage(5)}
            className="awareness-page-cta-btn-secondary"
          >
            About
          </button>
          <button
            onClick={() => navigateToPage(7)}
            className="awareness-page-cta-btn-primary"
          >
            Forecast Now
          </button>
        </div>
        <div className="awareness-page-disclaimer">
          Disclaimer: For informational and research purposes only
        </div>
      </div>
    </div>
  );
};

export default AwarenessPage;
