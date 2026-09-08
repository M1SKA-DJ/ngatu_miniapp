// TODO: вставь URL своего backend API
const API_URL = import.meta.env.VITE_API_URL;

export async function apiGet(path) {
  try {
    const res = await fetch(`${API_URL}${path}`);
    return await res.json();
  } catch (e) {
    return { error: true, message: "Failed to fetch" };
  }
}
