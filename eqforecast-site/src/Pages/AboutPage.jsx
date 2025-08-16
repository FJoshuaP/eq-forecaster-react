import React from "react";
import "../Css/AboutPage.css";

const AboutPage = ({ navigateToPage }) => {
  return (
    <div className="about-page-container">
      {/* Header */}
      <div className="header">
        <div className="header-content">
          <div className="logo">OPAL</div>
          <div className="nav-menu">
            <button onClick={() => navigateToPage(1)} className="nav-item">
              Overview
            </button>
            <button
              onClick={() => navigateToPage(3)}
              className="nav-item active"
            >
              About
            </button>
            <button onClick={() => navigateToPage(4)} className="nav-item">
              Hotlines
            </button>
            <button on onClick={() => navigateToPage(2)}className="nav-item">Awareness</button>
            <button className="forecast-btn">Forecast Now</button>
          </div>
        </div>
      </div>

      <div className="main-content">
        {/* About the model section */}
        <h1 className="page-title">About the model...</h1>

        <div className="model-section">
          <div className="model-content">
            <div className="model-text">
              <h2 className="section-title">Earthquake Forecasting</h2>
              <p className="section-paragraph">
                Body text for your whole article or post. We'll put in some
                lorem ipsum to show how a filled-out page might look.
              </p>
              <p className="section-paragraph">
                Excepteur efficient emerging, minim veniam anim aute carefully
                curated Ginza conversation exquisite perfect nostrud nisi
                intricate Content. Qui international first-class nulla ut.
                Punctual adipiscing, essential lovely queen tempor eiusmod
                irure. Exclusive izakaya charming Scandinavian impeccable aute
                quality of life soft power pariatur Melbourne consectetur
                discerning. Qui wardrobe aliquip, et Porter destination Toto
                remarkable officia Helsinki excepteur Basset hound. Zürich
                sleepy perfect consectetur.
              </p>

              <h2 className="section-title">
                Rule-Based Classification Algorithm
              </h2>
              <p className="section-paragraph">
                Body text for your whole article or post. We'll put in some
                lorem ipsum to show how a filled-out page might look.
              </p>
              <p className="section-paragraph">
                Excepteur efficient emerging, minim veniam anim aute carefully
                curated Ginza conversation exquisite perfect nostrud nisi
                intricate Content. Qui international first-class nulla ut.
                Punctual adipiscing, essential lovely queen tempor eiusmod
                irure. Exclusive izakaya charming Scandinavian impeccable aute
                quality of life soft power pariatur Melbourne consectetur
                discerning. Qui wardrobe aliquip, et Porter destination Toto
                remarkable officia Helsinki excepteur Basset hound. Zürich
                sleepy perfect consectetur.
              </p>

              <h2 className="section-title">
                Spatio-temporal Forecasting Concept
              </h2>
              <p className="section-paragraph">
                Body text for your whole article or post. We'll put in some
                lorem ipsum to show how a filled-out page might look.
              </p>
              <p className="section-paragraph">
                Excepteur efficient emerging, minim veniam anim aute carefully
                curated Ginza conversation exquisite perfect nostrud nisi
                intricate Content. Qui international first-class nulla ut.
                Punctual adipiscing, essential lovely queen tempor eiusmod
                irure. Exclusive izakaya charming Scandinavian impeccable aute
                quality of life soft power pariatur Melbourne consectetur
                discerning. Qui wardrobe aliquip, et Porter destination Toto
                remarkable officia Helsinki excepteur Basset hound. Zürich
                sleepy perfect consectetur.
              </p>
            </div>

            <div className="model-image-container">
              <img
                src="/api/placeholder/500/400"
                alt="Model diagram"
                className="model-image"
              />
            </div>
          </div>
        </div>

        {/* About the team section */}
        <div className="team-section">
          <div className="team-content">
            <h2 className="team-main-title">About the team...</h2>

            <div className="team-intro">
              <div className="team-image-container">
                <img
                  src="/api/placeholder/400/250"
                  alt="Team photo"
                  className="team-image"
                />
              </div>
              <div className="team-description">
                <h3 className="team-section-title">Earthquake Forecasting</h3>
                <p className="team-paragraph">
                  Body text for your whole article or post. We'll put in some
                  lorem ipsum to show how a filled-out page might look.
                </p>
                <p className="team-paragraph">
                  Excepteur efficient emerging, minim veniam anim aute carefully
                  curated Ginza conversation exquisite perfect nostrud nisi
                  intricate Content. Qui international first-class nulla ut.
                  Punctual adipiscing, essential lovely queen tempor eiusmod
                  irure. Exclusive izakaya charming Scandinavian impeccable aute
                  quality of life soft power pariatur Melbourne consectetur
                  discerning. Qui wardrobe aliquip, et Porter destination Toto
                  remarkable officia Helsinki excepteur Basset hound. Zürich
                  sleepy perfect consectetur.
                </p>
              </div>
            </div>

            <h3 className="team-members-title">Meet the team behind OPAL</h3>

            <div className="team-members-grid">
              <div className="team-member-card">
                <div className="member-image-container">
                  <img
                    src="/api/placeholder/80/80"
                    alt="Julia Abasolo"
                    className="member-image"
                  />
                </div>
                <div className="member-info">
                  <h4 className="member-name">Abasolo, Julia</h4>
                  <p className="member-description">
                    Body text for whatever you'd like to say. Add main takeaway
                    points, quotes, anecdotes, or even a very very short story.
                  </p>
                </div>
              </div>

              <div className="team-member-card">
                <div className="member-image-container">
                  <img
                    src="/api/placeholder/80/80"
                    alt="Kiara Laxamana"
                    className="member-image"
                  />
                </div>
                <div className="member-info">
                  <h4 className="member-name">Laxamana, Kiara</h4>
                  <p className="member-description">
                    Body text for whatever you'd like to say. Add main takeaway
                    points, quotes, anecdotes, or even a very very short story.
                  </p>
                </div>
              </div>

              <div className="team-member-card">
                <div className="member-image-container">
                  <img
                    src="/api/placeholder/80/80"
                    alt="Gabriel Ocampo"
                    className="member-image"
                  />
                </div>
                <div className="member-info">
                  <h4 className="member-name">Ocampo, Gabriel</h4>
                  <p className="member-description">
                    Body text for whatever you'd like to say. Add main takeaway
                    points, quotes, anecdotes, or even a very very short story.
                  </p>
                </div>
              </div>

              <div className="team-member-card">
                <div className="member-image-container">
                  <img
                    src="/api/placeholder/80/80"
                    alt="Joshua Perez"
                    className="member-image"
                  />
                </div>
                <div className="member-info">
                  <h4 className="member-name">Perez, Joshua</h4>
                  <p className="member-description">
                    Body text for whatever you'd like to say. Add main takeaway
                    points, quotes, anecdotes, or even a very very short story.
                  </p>
                </div>
              </div>
            </div>

            <div className="team-disclaimer">
              Disclaimer: For informational and research purposes only
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
