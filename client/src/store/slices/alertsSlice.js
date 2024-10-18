import { createSlice } from "@reduxjs/toolkit";

const alertsSlice = createSlice({
    name: "ALERTS",
    initialState: {
        alerts: [],
    },
    reducers: {
        addAlert: (state, action) => {
            state.alerts.push(action.payload);
        },
        removeAlert: (state, action) => {
            state.alerts = state.alerts.filter(alert => alert.id !== action.payload);
        },
        clearAlerts: (state) => {
            state.alerts = [];
        },
    },
});

export const { addAlert, removeAlert, clearAlerts } = alertsSlice.actions;
export default alertsSlice.reducer;