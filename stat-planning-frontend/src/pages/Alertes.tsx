import { useEffect, useState } from "react";

export default function Alertes() {
  const [alertes, setAlertes] = useState([]);

  useEffect(() => {
    fetch("https://stat-planning.onrender.com/alertes")
      .then(res => res.json())
      .then(setAlertes);
  }, []);

  return (
    <div>
      <h2 className="text-xl font-bold mb-2">Alertes</h2>
      {alertes.length === 0 ? <p>Aucune alerte.</p> : (
        <ul className="list-disc pl-5">
          {alertes.map((a, i) => (
            <li key={i}>
              Employé {a.employe_id} a dépassé son quota en {a.mois}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}