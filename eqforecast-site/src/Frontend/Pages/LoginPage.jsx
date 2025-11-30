import React, { useState } from "react";
import "../Css/LoginPage.css";
import { signIn } from "../services/authService";

const LoginPage = ({ navigateToPage, onLoginSuccess }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleLogin = async (e) => {
    e.preventDefault();
    
    if (!username || !password) {
      setError("Please fill in all fields");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const { user } = await signIn(username, password);
      
      onLoginSuccess(user);
      
    } catch (error) {
      setError(error.message || "Login failed. Please check your credentials.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleGuestLogin = () => {
    
    navigateToPage(3);
  };

  const goBackToLanding = () => {
    navigateToPage(3);
  };

  return (
    <div className="login-page-container">
      
      <button
        onClick={goBackToLanding}
        className="login-page-back-btn"
        title="Go back to landing page"
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

      <div className="login-page-content">
        <div className="login-page-form-container">
          <h1 className="login-page-title">Login</h1>

          {error && (
            <div className="login-page-error">
              <p>{error}</p>
              <button onClick={() => setError(null)}>Dismiss</button>
            </div>
          )}

          <form onSubmit={handleLogin} className="login-page-form">
            <div className="login-page-input-group">
              <label className="login-page-input-label">Username</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="login-page-input"
                placeholder="Enter username"
              />
            </div>

            <div className="login-page-input-group">
              <label className="login-page-input-label">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="login-page-input"
                placeholder="Enter password"
              />
            </div>

            <button 
              type="submit" 
              className="login-page-login-btn"
              disabled={isLoading}
            >
              {isLoading ? "Signing In..." : "Login"}
            </button>
          </form>

          <button onClick={handleGuestLogin} className="login-page-guest-btn">
            Use as guest
          </button>
        </div>

        <div className="login-page-disclaimer">
          Disclaimer: For informational and research purposes only
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
