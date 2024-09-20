import { useRoleBasedNavigation } from "./useRoleBasedNavigation";
import { useState } from "react";
import * as onboardingService from "../services/onboardingService";

export const useOnboarding = () => {
  const [status, setStatus] = useState("idle");
  const { goToDashboard } = useRoleBasedNavigation();

  const submitDetails = async (details) => {
    setStatus("loading");
    try {
      const response = await onboardingService.submitUserDetails(details);
      goToDashboard(response.roleId);
    } catch (error) {
      // pass
    } finally {
      setStatus("idle");
    }
  };

  return {
    submitDetails,
    status,
  };
};
