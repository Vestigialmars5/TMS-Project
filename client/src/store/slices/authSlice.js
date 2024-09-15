import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import * as authService from "../../services/authService";
import { decodeToken, storeToken } from "../../utils/tokenFunctions";

export const loginUser = createAsyncThunk(
  "auth/login",
  async (credentials, { rejectWithValue }) => {
    try {
      const response = await authService.login(credentials);
      console.log("action", response);
      storeToken(response.accessToken); // Store the token after successful login
      // Add alert here
      return decodeToken(response.accessToken);

    } catch (error) {
      console.error("Login error", error);
      return rejectWithValue({
        error: error.response?.data?.error,
        message: error.response?.data?.description,
        status: error.response?.status,
      });
    }
  }
);

export const logoutUser = createAsyncThunk("auth/logout", async () => {
  await authService.logout();
});

const authSlice = createSlice({
  name: "AUTH",
  initialState: {
    user: null,
    isAuthenticated: false,
    status: "idle",
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isAuthenticated = true;
        state.status = "success";
      })
      .addCase(loginUser.rejected, (state, action) => {
        console.log("rejected", action);
        state.error = {
          error: action.payload.error,
          message: action.payload.message,
          status: action.payload.status,
        };
        state.status = "failed";
      })
      .addCase(loginUser.pending, (state) => {
        console.log("pending");
        state.status = "loading";
      })
      .addCase(logoutUser.fulfilled, (state) => {
        state.user = null;
        state.token = null;
        state.isAuthenticated = false;
        state.status = "idle";
      });
  },
});

export default authSlice.reducer;
