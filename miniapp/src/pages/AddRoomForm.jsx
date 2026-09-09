import { useState } from "react";
import { apiPost } from "../../api/api";

export default function AddRoomForm() {
  const [number, setNumber] = useState("");
  const [building, setBuilding] = useState("");

  const submit = async () => {
    await apiPost("/rooms", { number, building });
    alert("Аудитория добавлена");
  };

  return (
    <div>
      <h2>Добавить аудиторию</h2>
      <input
        placeholder="Номер"
        value={number}
        onChange={(e) => setNumber(e.target.value)}
      />
      <input
        placeholder="Корпус"
        value={building}
        onChange={(e) => setBuilding(e.target.value)}
      />
      <button onClick={submit}>Добавить</button>
    </div>
  );
}
