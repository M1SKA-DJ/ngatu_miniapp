import { useEffect, useState } from "react";
import { apiGet } from "../api/api.js";
import Loader from "../components/Loader.jsx";
import ErrorBlock from "../components/ErrorBlock.jsx";

export default function Teachers() {
  const [teachers, setTeachers] = useState(null);

  useEffect(() => {
    async function load() {
      const data = await apiGet("/api/teachers/");
      setTeachers(data);
    }
    load();
  }, []);

  if (!teachers) return <Loader />;
  if (teachers.error) return <ErrorBlock />;

  return (
    <div>
      <h2>Преподаватели</h2>
      <ul>
        {teachers.map((t) => (
          <li key={t.id}>{t.full_name}</li>
        ))}
      </ul>
    </div>
  );
}
