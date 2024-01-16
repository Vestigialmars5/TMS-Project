import React, {useState, useEffect} from "react";


function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:5000/first-test").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>
      {(typeof	data.test === "undefined") ? (
        <p>loading...</p>
      ) : (
        data.test.map((test, i) => (
          <p key={i}>{test}</p>
        ))
      )}
    </div>
  )
}

export default App