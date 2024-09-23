import { useDispatch, useSelector } from "react-redux";
import { setUser, clearUser } from "../store/slices/authSlice";
import { useRoleBasedNavigation } from "../hooks/useRoleBasedNavigation";
import { useNavigate } from "react-router-dom";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import * as authService from "../services/authService";
import tokenService from "../services/tokenService";
import { showAlert } from "../store/actions/alertsActions";

export const useAuth = () => {
  const dispatch = useDispatch();
  const queryClient = useQueryClient();
  const user = useSelector((state) => state.auth.user);
  const navigate = useNavigate();
  const { goToDashboard } = useRoleBasedNavigation();

  const loginMutation = useMutation({
    mutationFn: (credentials) => authService.login(credentials),
    onSuccess: (data) => {
      tokenService.setTokens(data.accessToken, data.refreshToken);
      dispatch(setUser(data.user));
      queryClient.setQueryData("user", data.user);
      showAlert("Login Successful", "success");
      goToDashboard(data.user.roleId);
    },
    onError: (error) => {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      showAlert(message, "danger");
    },
  });

  const logoutMutation = useMutation({
    mutationFn: () => authService.logout(),
    onSuccess: () => {
      tokenService.removeTokens();
      dispatch(clearUser());
      queryClient.setQueryData("user", null);
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
    isAuthenticated: !!user,
    login,
    logout,
    loginStatus: loginMutation.status,
    logoutStatus: logoutMutation.status,
  };
};
