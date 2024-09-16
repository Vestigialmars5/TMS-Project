import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import * as authService from "../../services/authService";
import tokenService from "../../services/tokenService";

export const loginUser = createAsyncThunk(
  "auth/login",
  async (credentials, { rejectWithValue }) => {
    try {
      const response = await authService.login(credentials);
      tokenService.setTokens(response.accessToken, response.refreshToken); // Store tokens -> TODO: response.refreshToken
      // Add alert here
      return response.user;
    } catch (error) {
      return rejectWithValue({
        error: error.response?.data?.error,
        message: error.response?.data?.description,
        status: error.response?.status,
      });
    }
  }
);

export const logoutUser = createAsyncThunk(
  "auth/logout",
  async (_, { rejectWithValue }) => {
    try {
      await authService.logout();
      tokenService.removeTokens();
      return ;
    } catch {
      return rejectWithValue({
        error: error.response?.data?.error,
        message: error.response?.data?.description,
        status: error.response?.status,
      });
    }
  }
);

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
        state.isAuthenticated = false;
        state.status = "idle";
      })
      .addCase(logoutUser.pending, (state) => {
        state.status = "loading";
      })
      .addCase(logoutUser.rejected, (state, action) => {
        state.error = {
          error: action.payload.error,
          message: action.payload.message,
          status: action.payload.status,
        };
        state.status = "failed";
      });
  },
});

export default authSlice.reducer;
