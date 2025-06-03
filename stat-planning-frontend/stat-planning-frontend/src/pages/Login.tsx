
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [pwd, setPwd] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    if (pwd === "admin123") {
      localStorage.setItem("auth", "true");
      navigate("/");
    } else {
      alert("Mot de passe incorrect.");
    }
  };

  return (
    <div className="max-w-sm mx-auto mt-20 bg-white p-6 rounded shadow">
      <h2 className="text-xl mb-4">Connexion</h2>
      <input
        type="password"
        value={pwd}
        onChange={(e) => setPwd(e.target.value)}
        placeholder="Mot de passe"
        className="border p-2 w-full mb-4"
      />
      <button onClick={handleLogin} className="bg-blue-600 text-white px-4 py-2 rounded w-full">
        Se connecter
      </button>
    </div>
  );
}
