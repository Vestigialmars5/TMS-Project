import { React, useState, useRef, useCallback, useMemo } from "react";
import "leaflet/dist/leaflet.css";
import {
  MapContainer,
  Marker,
  Polyline,
  Popup,
  TileLayer,
  useMap,
} from "react-leaflet";

const center = {
  lat: 37.79066,
  lng: -122.40945,
};

function DraggableMarker({ text, onDragEnd }) {
  const [draggable, setDraggable] = useState(false);
  const [position, setPosition] = useState(center);
  const markerRef = useRef(null);
  const eventHandlers = useMemo(
    () => ({
      dragend() {
        const marker = markerRef.current;
        if (marker != null) {
          setPosition(marker.getLatLng());
          onDragEnd && onDragEnd(marker.getLatLng());
        }
      },
    }),
    [onDragEnd]
  );
  const toggleDraggable = useCallback(() => {
    setDraggable((d) => !d);
  }, []);

  return (
    <>
      <Marker
        draggable={draggable}
        eventHandlers={eventHandlers}
        position={position}
        ref={markerRef}
      >
        <Popup minWidth={90}>
          <p>
            {text}
            <br></br>
            <span onClick={toggleDraggable}>
              {draggable
                ? "Marker is draggable"
                : "Click here to make marker draggable"}
            </span>
          </p>
        </Popup>
      </Marker>
    </>
  );
}

export default DraggableMarker;
