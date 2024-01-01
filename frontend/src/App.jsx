import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [artists, setArtists] = useState([]);
  const fetchArtists = async () => {
    const response = await axios.get("http://localhost:8000/music/api/artists");
    setArtists(response.data);
  };

  useEffect(() => {
    fetchArtists();
  }, []);

  return (
    <>
      <h1>Artists</h1>
      <ul>
        {artists.map((artist) => (
          <li key={artist.id}>{artist.name}</li>
        ))}
      </ul>
    </>
  );
}

export default App;
