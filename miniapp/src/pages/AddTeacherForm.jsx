import { useState } from "react";
import { apiPost } from "../../api/api";

export default function AddTeacherForm() {
  const [name, setName] = useState("");
  const [department, setDepartment] = useState("");

  const submit = async () => {
    await apiPost("/teachers", { full_name: name, department });
    alert("Преподаватель добавлен");
  };

  return (
    <div>
      <h2>Добавить преподавателя</h2>
      <input
        placeholder="ФИО"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder="Кафедра"
        value={department}
        onChange={(e) => setDepartment(e.target.value)}
      />
      <button onClick={submit}>Добавить</button>
    </div>
  );
}
