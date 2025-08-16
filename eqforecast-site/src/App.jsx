import React, { useState } from "react";
import LandingPage from "./Pages/LandingPage";
import AboutPage from "./Pages/AboutPage";
import HotlinePage from "./Pages/HotlinePage";
import AwarenessPage from "./Pages/AwarenessPage";
import ForecastPage from "./Pages/Forecasting";

const App = () => {
  const [currentPage, setCurrentPage] = useState(1);

  const navigateToPage = (page) => {
    setCurrentPage(page);
  };

  return (
    <div>
      {currentPage === 1 && <LandingPage navigateToPage={navigateToPage} />}
      {currentPage === 2 && <AwarenessPage navigateToPage={navigateToPage} />}
      {currentPage === 3 && <AboutPage navigateToPage={navigateToPage} />}
      {currentPage === 4 && <HotlinePage navigateToPage={navigateToPage} />}
      {currentPage === 5 && <ForecastPage navigateToPage={navigateToPage} />}

    </div>
  );
};

export default App;
