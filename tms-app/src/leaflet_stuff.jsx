import React, { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";

import "leaflet/dist/images/marker-icon-2x.png";
import "leaflet/dist/images/marker-shadow.png";

import { MapContainer, Marker, Popup, TileLayer, useMap } from "react-leaflet";

function LeafletComponent() {
  return (
    <MapContainer center={[38.0406, -84.5037]} zoom={12}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[37.986918, -84.499435]}>
        <Popup>
            Here's hom
        </Popup>
      </Marker>
    </MapContainer>
  );
}

export default LeafletComponent;
