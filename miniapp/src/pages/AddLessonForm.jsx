import { useState } from "react";
import { apiPost } from "../../api/api";

export default function AddLessonForm() {
  const [subjectId, setSubjectId] = useState("");
  const [teacherId, setTeacherId] = useState("");
  const [roomId, setRoomId] = useState("");
  const [groupId, setGroupId] = useState("");
  const [day, setDay] = useState("Понедельник");
  const [lessonNumber, setLessonNumber] = useState(1);

  const submit = async () => {
    await apiPost("/lessons", {
      subject_id: subjectId,
      teacher_id: teacherId,
      room_id: roomId,
      group_id: groupId,
      day_of_week: day,
      lesson_number: lessonNumber,
    });

    alert("Пара добавлена");
  };

  return (
    <div>
      <h2>Добавить пару</h2>

      <input placeholder="ID предмета" value={subjectId} onChange={(e) => setSubjectId(e.target.value)} />
      <input placeholder="ID преподавателя" value={teacherId} onChange={(e) => setTeacherId(e.target.value)} />
      <input placeholder="ID аудитории" value={roomId} onChange={(e) => setRoomId(e.target.value)} />
      <input placeholder="ID группы" value={groupId} onChange={(e) => setGroupId(e.target.value)} />

      <select value={day} onChange={(e) => setDay(e.target.value)}>
        <option>Понедельник</option>
        <option>Вторник</option>
        <option>Среда</option>
        <option>Четверг</option>
        <option>Пятница</option>
        <option>Суббота</option>
      </select>

      <input
        type="number"
        value={lessonNumber}
        onChange={(e) => setLessonNumber(Number(e.target.value))}
      />

      <button onClick={submit}>Добавить</button>
    </div>
  );
}
