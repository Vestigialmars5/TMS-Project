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
      tokenService.setAccessToken(data.accessToken);
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

  const submitUserDetails = (details) =>
    submitUserDetailsMutation.mutate(details);

  return {
    submitUserDetails,
    submitUserDetailsStatus: submitUserDetailsMutation.status,
  };
};
