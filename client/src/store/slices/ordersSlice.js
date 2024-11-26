import { createSlice } from "@reduxjs/toolkit";

const ordersSlice = createSlice({
  name: "ORDERS",
  initialState: {
    orders: [],
  },
  reducers: {
    setOrders: (state, action) => {
      state.orders = action.payload;
    },
    addOrder: (state, action) => {
      state.orders.push(action.payload);
    },
    removeOrder: (state, action) => {
      state.orders = state.orders.filter(
        (order) => order._id !== action.payload
      );
    },
  },
});

export const { setOrders, addOrder, removeOrder } = ordersSlice.actions;

export default ordersSlice.reducer;
