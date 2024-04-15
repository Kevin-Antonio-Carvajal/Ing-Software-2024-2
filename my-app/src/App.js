import React, { useState, useContext } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CRUDClientes from './components/Clientes/CRUDClientes';
import CRUDPeliculas from './components/Peliculas/CRUDPeliculas';
import CRURentas from './components/Rentar/CRURentas';

import './App.css';

const ThemeContext = React.createContext();

function App() {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={theme}>
      <Router>
        <div className={`App ${theme}`}>
          <nav className="side-navigation">
            <button onClick={toggleTheme}>Toggle Theme</button>
            <ul>
              <li>
                <Link to="/usuarios">Usuarios</Link>
              </li>
              <li>
                <Link to="/peliculas">Películas</Link>
              </li>
              <li>
                <Link to="/rentas">Rentas</Link>
              </li>
            </ul>
          </nav>
          <main>
            <Routes>
              <Route path="/usuarios" element={<CRUDClientes />} />
              <Route path="/peliculas" element={<CRUDPeliculas />} />
              <Route path="/rentas" element={<CRURentas />} />
            </Routes>
          </main>
        </div>
      </Router>
    </ThemeContext.Provider>
  );
}

export default App;
