import React from "react";
import UserDetailsForm from "../../components/onboarding/UserDetailsForm";
import CustomerDetailsForm from "../../components/onboarding/CustomerDetailsForm";
import { useQuery } from "@tanstack/react-query";
import Spinner from "react-bootstrap/Spinner";
import { useAuth } from "../../hooks/useAuth";
import { getCurrentStep } from "../../services/onboardingService";

const Onboarding = () => {
  const { user } = useAuth();
  const {data: currentStep, isLoading, error} = useQuery({
    queryKey: ["currentStep"],
    queryFn: () => getCurrentStep(),
  });

  if (isLoading || !user) {
    return <Spinner />;
  }

  if (error) {
    const message =
      error.response?.data?.description ||
      error.response?.data?.error ||
      "An Unknown Error Occurred";
    console.error(error);
    showAlert(`Error Retrieving Current Step: ${message}`, "danger");
    // TODO: logout
    return <p>Error</p>
  }

  const roleForms = {
    4: CustomerDetailsForm,
  };

  const STEP_COMPONENTS = {
    1: UserDetailsForm,
    2: roleForms[user.roleId] || (() => <p>Role-specific form not found</p>),
  };

  return (
    <div>
      <h1>Onboarding</h1>
      {STEP_COMPONENTS[currentStep] &&
        React.createElement(STEP_COMPONENTS[currentStep])}
    </div>
  );

};

export default Onboarding;
