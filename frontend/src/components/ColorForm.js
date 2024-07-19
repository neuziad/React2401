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
    <div className="m-plus-1p-regular" style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', justifyContent: 'center'}}>
      <form onSubmit={handleSubmit}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', justifyContent: 'left', margin: '4rem' }}>
          {Object.keys(hexColors).map((part, index) => (
            <div key={part} style={{ display: 'grid', justifyContent: 'left', marginBottom: index < 3 ? '1.5rem' : '0' }}>
              <label style={{ display: 'grid', justifyContent: 'left' }}>
                {part.charAt(0).toUpperCase() + part.slice(1)}:
                <HexColorPicker
                  color={hexColors[part]}
                  onChange={(color) => handleColorChange(color, part)}
                  style={{ margin: '1rem' }}
                />
                <input
                  type="text"
                  name={part}
                  value={hexColors[part]}
                  onChange={handleChange}
                  style={{ margin: 'auto' }}
                />
              </label>
            </div>
          ))}
        </div>
        <button type="submit" style={{ fontSize: '1.5rem' }}>Generate Code</button>
      </form>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(1, 1fr)' }}>
        <h2 className="m-plus-1p-regular" style={{ textAlign: 'center' }}>Generated Code</h2>
        <div style={{ gridColumn: '1' }}>
          <textarea
            style={{ width: '80%', height: '550px', resize: 'none' }}
            value={generatedCode}
            readOnly
          />
        </div>
      </div>
    </div>
  );
};

export default ColorForm;
