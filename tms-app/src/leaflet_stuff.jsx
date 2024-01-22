import React, { useEffect, useState } from "react";
import get_coordinates from "./get_api_data";

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
  const polyline = get_coordinates();
  const limeOptions = { color: "lime" };

  const center = [37.7928594, -122.4027912];
  const destination = [37.7870311, -122.403019];

  const maxBounds = [
    [37.976523, -84.570034],
    [38.076587, -84.449871],
  ];

  if (!polyline) {
    return <div>Loading...</div>;
  }

  return (
    <MapContainer center={center} zoom={15} minZoom={13}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={center}>
        <Popup>Here's start</Popup>
      </Marker>
      <Marker position={destination}>
        <Popup>Here's destination</Popup>
      </Marker>
      <Polyline pathOptions={limeOptions} positions={polyline} />
    </MapContainer>
  );
}

export default LeafletComponent;
