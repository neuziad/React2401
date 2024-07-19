import React from 'react';
import './App.css';
import ColorForm from './components/ColorForm';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="m-plus-1p-regular" style={{ margin: "-1%" }}><b>React2401</b></h1>
        <ColorForm/>
      </header>
    </div>
  );
}

export default App;
