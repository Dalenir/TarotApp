import {useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";

console.log(import.meta.env);
console.log(import.meta.env.PROD)

function App() {
  const [count, setCount] = useState(0)
  const [apiresp, setApiresp] = useState("")

  function handleApiCall() {
          axios.get(`${import.meta.env.VITE_API_ROOT}/`)
              .then(response => {
                  setApiresp(response.data.message + '!')
              })
              .catch(error => {
                  setApiresp('ERROR: ' + error.message)
              })
          }


  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      {apiresp && <h3>{apiresp}</h3>}
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={handleApiCall}>Ping API</button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App
