
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
import Stats from "./pages/Stats";
import Alertes from "./pages/Alertes";
import Parametres from "./pages/Parametres";
import Login from "./pages/Login";

const ProtectedRoute = ({ children }) => {
  const isAuth = localStorage.getItem("auth") === "true";
  return isAuth ? children : <Navigate to="/login" />;
};

export default function App() {
  return (
    <Router>
      <div className="p-4">
        <nav className="mb-4 space-x-4">
          <Link to="/">Stats</Link>
          <Link to="/alertes">Alertes</Link>
          <Link to="/parametres">Paramètres</Link>
          <Link to="/login">Déconnexion</Link>
        </nav>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<ProtectedRoute><Stats /></ProtectedRoute>} />
          <Route path="/alertes" element={<ProtectedRoute><Alertes /></ProtectedRoute>} />
          <Route path="/parametres" element={<ProtectedRoute><Parametres /></ProtectedRoute>} />
        </Routes>
      </div>
    </Router>
  );
}
