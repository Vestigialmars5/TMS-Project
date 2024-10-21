import { useDispatch, useSelector } from "react-redux";
import {
  setUser,
  clearUser,
  startAuthenticating,
  stopAuthenticating,
} from "../store/slices/authSlice";
import { useNavigate } from "react-router-dom";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import * as authService from "../services/authService";
import tokenService from "../services/tokenService";
import { showAlert } from "../store/actions/alertsActions";

export const useAuth = () => {
  const dispatch = useDispatch();
  const queryClient = useQueryClient();
  const { user, isAuthenticated } = useSelector((state) => state.auth);
  const navigate = useNavigate();

  const loginMutation = useMutation({
    mutationFn: (credentials) => {
      dispatch(startAuthenticating()); // Set user stops authenticating automatically
      return authService.login(credentials);
    },
    onSuccess: (data) => {
      tokenService.setTokens(data.accessToken, data.refreshToken);
      queryClient.setQueryData("user", data.user);
      dispatch(setUser(data.user));
      showAlert("Login Successful", "success");
    },
    onError: (error) => {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      showAlert(message, "danger");
      dispatch(stopAuthenticating());
    },
  });

  const logoutMutation = useMutation({
    mutationFn: () => authService.logout(),
    onSuccess: () => {
      tokenService.removeTokens();
      dispatch(clearUser());
      queryClient.clear();
      showAlert("Logout Successful", "success");
      navigate("/login");
    },
    onError: (error) => {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      showAlert(message, "danger");
    },
  });

  const login = (credentials) => loginMutation.mutate(credentials);
  const logout = () => logoutMutation.mutate();

  return {
    user,
    isAuthenticated: isAuthenticated,
    login,
    logout,
    loginStatus: loginMutation.status,
    logoutStatus: logoutMutation.status,
  };
};
