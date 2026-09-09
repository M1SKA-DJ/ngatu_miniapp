import { useEffect, useState } from "react";
import { apiGet, apiPost } from "../api/api";
import AddTeacherForm from "../components/admin/AddTeacherForm";
import AddRoomForm from "../components/admin/AddRoomForm";
import AddSubjectForm from "../components/admin/AddSubjectForm";
import AddGroupForm from "../components/admin/AddGroupForm";
import AddLessonForm from "../components/admin/AddLessonForm";

function Admin() {
  const [admin, setAdmin] = useState(false);
  const [section, setSection] = useState("teachers");

  useEffect(() => {
    apiGet("/admin/check")
      .then((res) => setAdmin(res.allowed))
      .catch(() => setAdmin(false));
  }, []);

  if (!admin) return <div>Нет доступа</div>;

  return (
    <div style={{ padding: 20 }}>
      <h1>Админ‑панель</h1>

      <nav style={{ marginBottom: 20 }}>
        <button onClick={() => setSection("teachers")}>Преподаватели</button>
        <button onClick={() => setSection("rooms")}>Аудитории</button>
        <button onClick={() => setSection("subjects")}>Предметы</button>
        <button onClick={() => setSection("groups")}>Группы</button>
        <button onClick={() => setSection("lessons")}>Пары</button>
      </nav>

      {section === "teachers" && <AddTeacherForm />}
      {section === "rooms" && <AddRoomForm />}
      {section === "subjects" && <AddSubjectForm />}
      {section === "groups" && <AddGroupForm />}
      {section === "lessons" && <AddLessonForm />}
    </div>
  );
}

export default Admin;
