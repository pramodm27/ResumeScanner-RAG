import React, { useState } from 'react';
import axios from 'axios';

function UploadResume() {
  const [file, setFile] = useState(null);

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await axios.post(
      'http://localhost:8000/upload-resume',
      formData
    );

    console.log(response.data);
  };

  return (
    <div>
      <input type='file' onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadFile}>Upload</button>
    </div>
  );
}

export default UploadResume;