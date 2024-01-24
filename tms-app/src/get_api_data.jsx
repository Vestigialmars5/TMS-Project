async function getCoordinates(props, callback) {
  console.log(props)
  try {
    const response = await fetch("http://127.0.0.1:5000/api-test", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(props),
    });

    if (!response.ok) {
      throw new Error("Error Getting Coordinates");
    }

    const data = await response.json();
    callback(data);
    console.log("datata", data)
  } catch (error) {
    console.error(error);
  }
}

export default getCoordinates;
