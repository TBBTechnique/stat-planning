
import { useEffect, useState } from "react";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer,
  PieChart, Pie, Cell, LineChart, Line
} from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#A28EF0", "#F56565"];

export default function Stats() {
  const [stats, setStats] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/stats")
      .then(res => res.json())
      .then(setStats);
  }, []);

  // Regrouper les heures par employé pour le PieChart
  const totalParEmploye = stats.reduce((acc, s) => {
    if (!acc[s.employe_id]) acc[s.employe_id] = 0;
    acc[s.employe_id] += s.heures_planifiees;
    return acc;
  }, {});
  const pieData = Object.entries(totalParEmploye).map(([key, value]) => ({ name: key, value }));

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Statistiques</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <div className="bg-white p-4 rounded shadow">
          <h3 className="font-semibold mb-2">Évolution mensuelle</h3>
          <ResponsiveContainer width="100%" height={250}>
            <LineChart data={stats}>
              <XAxis dataKey="mois" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="heures_planifiees" stroke="#8884d8" name="Planifiées" />
              <Line type="monotone" dataKey="heures_effectuees" stroke="#82ca9d" name="Effectuées" />
            </LineChart>
          </ResponsiveContainer>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h3 className="font-semibold mb-2">Répartition par employé</h3>
          <ResponsiveContainer width="100%" height={250}>
            <PieChart>
              <Pie data={pieData} dataKey="value" nameKey="name" outerRadius={90} label>
                {pieData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      <table className="table-auto w-full text-sm bg-white rounded shadow">
        <thead>
          <tr>
            <th className="text-left p-2">Employé</th>
            <th>Mois</th>
            <th>Planifiées</th>
            <th>Effectuées</th>
            <th>Dépassement</th>
          </tr>
        </thead>
        <tbody>
          {stats.map((s, i) => (
            <tr key={i} className={s.depassement_quota === "Oui" ? "bg-red-100" : ""}>
              <td className="p-2">{s.employe_id}</td>
              <td>{s.mois}</td>
              <td>{s.heures_planifiees}</td>
              <td>{s.heures_effectuees}</td>
              <td>{s.depassement_quota}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
