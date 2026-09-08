import { useState } from "react";
import Schedule from "./pages/Schedule.jsx";
import Teachers from "./pages/Teachers.jsx";
import Settings from "./pages/Settings.jsx";
import AdminPanel from "./pages/AdminPanel.jsx";

export default function App() {
  const [page, setPage] = useState("schedule");

  const tg = window.Telegram.WebApp;
  tg.expand();

  return (
    <div className="app">
      <nav className="nav">
        <button onClick={() => setPage("schedule")}>Расписание</button>
        <button onClick={() => setPage("teachers")}>Преподаватели</button>
        <button onClick={() => setPage("settings")}>Настройки</button>

        {tg.initDataUnsafe?.user?.id === Number(import.meta.env.VITE_ADMIN_ID) && (
          <button onClick={() => setPage("admin")}>Админ</button>
        )}
      </nav>

      {page === "schedule" && <Schedule />}
      {page === "teachers" && <Teachers />}
      {page === "settings" && <Settings />}
      {page === "admin" && <AdminPanel />}
    </div>
  );
}
