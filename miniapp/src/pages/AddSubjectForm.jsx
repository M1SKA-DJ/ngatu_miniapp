import { useState } from "react";
import { apiPost } from "../../api/api";

export default function AddSubjectForm() {
  const [name, setName] = useState("");
  const [type, setType] = useState("lecture");

  const submit = async () => {
    await apiPost("/subjects", { name, type });
    alert("Предмет добавлен");
  };

  return (
    <div>
      <h2>Добавить предмет</h2>
      <input
        placeholder="Название"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option value="lecture">Лекция</option>
        <option value="practice">Практика</option>
        <option value="lab">Лабораторная</option>
      </select>

      <button onClick={submit}>Добавить</button>
    </div>
  );
}
