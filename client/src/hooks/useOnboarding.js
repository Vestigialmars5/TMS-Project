import { useMutation, useQueryClient } from "@tanstack/react-query";
import tokenService from "../services/tokenService";
import {
  setUser,
  startAuthenticating,
  stopAuthenticating,
} from "../store/slices/authSlice";
import { useDispatch } from "react-redux";
import { showAlert } from "../store/actions/alertsActions";
import * as onboardingService from "../services/onboardingService";

export const useOnboarding = () => {
  const dispatch = useDispatch();
  const queryClient = useQueryClient();

  const submitUserDetailsMutation = useMutation({
    mutationFn: (details) => {
      dispatch(startAuthenticating()); // Set user stops authenticating automatically
      return onboardingService.submitUserDetails(details);
    },
    onSuccess: (data) => {
      queryClient.setQueryData("user", data.user);
      dispatch(setUser(data.user));
      showAlert("User Details Submitted", "success");
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

  const submitRoleDetailsMutation = useMutation({
    mutationFn: (details) => {
      dispatch(startAuthenticating()); // Set user stops authenticating automatically
      return onboardingService.submitRoleDetails(details);
    },
    onSuccess: (data) => {
      queryClient.setQueryData("user", data.user);
      dispatch(setUser(data.user));
      showAlert("Role Details Submitted", "success");
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

  const submitUserDetails = (details) =>
    submitUserDetailsMutation.mutate(details);

  const submitRoleDetails = (details) =>
    submitRoleDetailsMutation.mutate(details);

  return {
    submitUserDetails,
    submitRoleDetails,
    submitUserDetailsStatus: submitUserDetailsMutation.status,
    submitRoleDetailsStatus: submitRoleDetailsMutation.status,
  };
};
