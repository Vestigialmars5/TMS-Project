import { createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
  name: "AUTH",
  initialState: {
    user: null,
    isAuthenticated: false,
    isAuthenticating: false,
  },
  reducers: {
    setUser: (state, action) => {
      state.user = action.payload;
      state.isAuthenticated = true;
      state.isAuthenticating = false;
    },
    clearUser: (state) => {
      state.user = null;
      state.isAuthenticated = false;
      state.isAuthenticating = false;
    },
    startAuthenticating: (state) => {
      state.isAuthenticating = true;
    },
    stopAuthenticating: (state) => {
      state.isAuthenticating = false;
    },
  },
});


export const { setUser, clearUser, startAuthenticating, stopAuthenticating } = authSlice.actions;
export default authSlice.reducer;