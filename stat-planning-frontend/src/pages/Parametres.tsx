import { useEffect, useState } from "react";

export default function Parametres() {
  const [param, setParam] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/parametres")
      .then(res => res.json())
      .then(setParam);
  }, []);

  const handleToggle = (key: string) => {
    if (param) {
      setParam({ ...param, [key]: !param[key] });
    }
  };

  const save = () => {
    fetch("http://localhost:8000/parametres", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(param),
    });
  };

  if (!param) return <p>Chargement...</p>;

  return (
    <div>
      <h2 className="text-xl font-bold mb-2">Paramètres de Majoration</h2>
      <div className="grid grid-cols-2 gap-2">
        {["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"].map(jour => (
          <label key={jour}>
            <input
              type="checkbox"
              checked={param[`${jour}_active`]}
              onChange={() => handleToggle(`${jour}_active`)}
            />{" "}
            Majoration {jour}
          </label>
        ))}
      </div>
      <div className="mt-4 space-y-2">
        <label>
          Début nuit :{" "}
          <input
            type="number"
            value={param.nuit_debut}
            onChange={e => setParam({ ...param, nuit_debut: parseInt(e.target.value) })}
          />
        </label>
        <label>
          Fin nuit :{" "}
          <input
            type="number"
            value={param.nuit_fin}
            onChange={e => setParam({ ...param, nuit_fin: parseInt(e.target.value) })}
          />
        </label>
      </div>
      <button onClick={save} className="mt-4 px-4 py-2 bg-blue-600 text-white rounded">
        Enregistrer
      </button>
    </div>
  );
}