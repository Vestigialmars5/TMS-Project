import { combineReducers } from "@reduxjs/toolkit";
import authReducer from "./slices/authSlice";
import alertsReducer from "./slices/alertsSlice";


export const rootReducer = combineReducers({
    auth: authReducer,
    alerts: alertsReducer,
});


export default rootReducer;