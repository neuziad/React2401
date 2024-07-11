import React, { useState } from 'react';
import axios from 'axios';
import { HexColorPicker } from 'react-colorful';

const ColorForm = () => {
  const [hexColors, setHexColors] = useState({
    // Default Mario colors
    hat: '#7F0000',
    overalls: '#00007F',
    gloves: '#7F7F7F',
    shoes: '#390E07',
    face: '#7F603C',
    hair: '#390300'
  });
  const [generatedCode, setGeneratedCode] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setHexColors({
      ...hexColors,
      [name]: value
    });
  };

  const handleColorChange = (color, part) => {
    setHexColors({
      ...hexColors,
      [part]: color.toUpperCase()
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Submitting:', hexColors);
    try {
      const response = await axios.post('http://localhost:5000/generate', { hexColors });
      setGeneratedCode(response.data.code);
    } catch (error) {
      console.error('Error generating code:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        {Object.keys(hexColors).map((part) => (
          <div key={part}>
            <label>
              {part.charAt(0).toUpperCase() + part.slice(1)}:
              <HexColorPicker color={hexColors[part]} onChange={(color) => handleColorChange(color, part)} />
              <input
                type="text"
                name={part}
                value={hexColors[part]}
                onChange={handleChange}
              />
            </label>
          </div>
        ))}
        <button type="submit">Generate Code</button>
      </form>
      {generatedCode && (
        <div>
          <h2>Generated Code</h2>
          <pre>{generatedCode}</pre>
        </div>
      )}
    </div>
  );
};

export default ColorForm;
