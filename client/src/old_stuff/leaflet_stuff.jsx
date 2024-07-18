import React, { useState } from "react";
import get_coordinates from "./old_stuff/get_api_data";
import DraggableMarker from "./old_stuff/dragable";

import "leaflet/dist/leaflet.css";

import "leaflet/dist/images/marker-icon-2x.png";
import "leaflet/dist/images/marker-icon.png";
import "leaflet/dist/images/marker-shadow.png";

import {
  MapContainer,
  Marker,
  Polyline,
  Popup,
  TileLayer,
  useMap,
} from "react-leaflet";

function LeafletComponent() {
  console.log("inside leaflet");
  const [polyline, setPolyline] = useState(null);
  const limeOptions = { color: "lime" };

  const center = [37.79066, -122.40945];

  const [origin, setOrigin] = useState(null);
  const [destination, setDestination] = useState(null);

  const maxBounds = [
    [37.78319, -122.41879],
    [37.79696, -122.40127],
  ];

  const bounds = [
    [51.49, -0.08],
    [51.5, -0.06],
  ];

  function getStuff() {
    console.log("inside stuff");
    if (origin && destination) {
      console.log("here");
      get_coordinates(
        {
          originLat: origin.lat,
          originLng: origin.lng,
          destinationLat: destination.lat,
          destinationLng: destination.lng,
        },
        (data) => {
          console.log("recieved:", data);
          setPolyline(data);
        }
      );
    } else {
      console.log("eerrrooorr");
    }
  }

  const handleOriginDragEnd = (newPosition) => {
    setOrigin(newPosition);
  };

  const handleDestinationDragEnd = (newPosition) => {
    setDestination(newPosition);
  };

  return (
    <MapContainer center={center} zoom={16} maxBounds={maxBounds}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {polyline ? (
        <Polyline pathOptions={limeOptions} positions={polyline} />
      ) : null}
      <DraggableMarker onDragEnd={handleOriginDragEnd} text={"origin"} />
      <DraggableMarker
        onDragEnd={handleDestinationDragEnd}
        text={"destination"}
      />
      <Marker position={[37.791838, -122.4108302]}></Marker>
      <button type="button" onClick={getStuff} className="button">
        Get Route
      </button>
    </MapContainer>
  );
}

export default LeafletComponent;
