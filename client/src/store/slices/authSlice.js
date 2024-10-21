import { createSlice } from "@reduxjs/toolkit";
import tokenService from "../../services/tokenService";
import { showAlert } from "../actions/alertsActions";
import { queryClient } from "../../main";

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

export const {
  setUser,
  clearUser,
  startAuthenticating,
  stopAuthenticating,
} = authSlice.actions;

export const forceLogout = () => (dispatch) => {
  tokenService.removeTokens();
  dispatch(clearUser());
  queryClient.clear();
  showAlert("You Have Been Logged Out", "info");
}
export default authSlice.reducer;
