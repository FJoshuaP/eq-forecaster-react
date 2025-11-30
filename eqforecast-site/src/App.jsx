import React, { useState } from "react";
import LoginPage from "./Frontend/Pages/LoginPage";
import LandingPage from "./Frontend/Pages/LandingPage";
import AwarenessPage from "./Frontend/Pages/AwarenessPage";
import AboutPage from "./Frontend/Pages/AboutPage";
import HotlinePage from "./Frontend/Pages/HotlinePage";
import ForecastPage from "./Frontend/Pages/ForecastingPage";
import BinPage from "./Frontend/Pages/BinPage";

const App = () => {
  const [currentPage, setCurrentPage] = useState(3); 
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);

  const navigateToPage = (page) => {
    setCurrentPage(page);
  };

  

 

  return (
    <div>
      {currentPage === 1 && (
        <LoginPage
          navigateToPage={navigateToPage}
          onLoginSuccess={handleLoginSuccess}
        />
      )}
      {currentPage === 3 && (
        <LandingPage navigateToPage={navigateToPage} isLoggedIn={isLoggedIn} />
      )}
      {currentPage === 4 && (
        <AwarenessPage
          navigateToPage={navigateToPage}
          isLoggedIn={isLoggedIn}
        />
      )}
      {currentPage === 5 && (
        <AboutPage navigateToPage={navigateToPage} isLoggedIn={isLoggedIn} />
      )}
      {currentPage === 6 && (
        <HotlinePage navigateToPage={navigateToPage} isLoggedIn={isLoggedIn} />
      )}
      {currentPage === 7 && (
        <ForecastPage navigateToPage={navigateToPage} isLoggedIn={isLoggedIn} />
      )}
      {currentPage === 8 && (
        <BinPage navigateToPage={navigateToPage} isLoggedIn={isLoggedIn} />
      )}
    </div>
  );
};

export default App;
