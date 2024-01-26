async function getCoordinates(props, callback) {
  fetch("http://127.0.0.1:5000/api-test", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(props),
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      throw new Error("Error Getting Data From API");
    })
    .then((data) => {
      callback(data);
    })
    .catch((error) => {
      console.log(error);
    });
}

export default getCoordinates;
