import { React, useState, useEffect } from "react";

function get_coordinates() {
  const [coordinates, setCoordinates] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api-test")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("hi");
      })
      .then((data) => {
        setCoordinates(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return coordinates;
}

export default get_coordinates;
