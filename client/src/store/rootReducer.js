import { combineReducers } from "@reduxjs/toolkit";
import authReducer from "./slices/authSlice";
import alertsReducer from "./slices/alertsSlice";
import ordersReducer from "./slices/ordersSlice";


export const rootReducer = combineReducers({
    auth: authReducer,
    alerts: alertsReducer,
    orders: ordersReducer,
});


export default rootReducer;