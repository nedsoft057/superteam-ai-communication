// Simple React UI for admins
import React from 'react';
import axios from 'axios';

export default function App() {
  const handleUpload = async (file) => {
    await axios.post('http://localhost:8000/upload-document', file);
  };

  return (
    <div>
      <h1>Superteam Admin Dashboard</h1>
      <input type="file" onChange={(e) => handleUpload(e.target.files[0])} />
    </div>
  );
}
