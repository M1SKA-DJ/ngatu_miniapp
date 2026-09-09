import { useState } from "react";
import { apiPost } from "../../api/api";

export default function AddGroupForm() {
  const [name, setName] = useState("");

  const submit = async () => {
    await apiPost("/groups", { name });
    alert("Группа добавлена");
  };

  return (
    <div>
      <h2>Добавить группу</h2>
      <input
        placeholder="Название группы"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={submit}>Добавить</button>
    </div>
  );
}
