import { useEffect, useState } from "react";
import { apiGet } from "./api/api";

function App() {
  const [groups, setGroups] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiGet("/groups")
      .then((data) => setGroups(data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Загрузка...</div>;

  return (
    <div>
      <h1>Группы</h1>
      <ul>
        {groups.map((g) => (
          <li key={g.id}>{g.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
