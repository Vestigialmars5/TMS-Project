import React from "react";
import UserDetailsForm from "../../components/onboarding/UserDetailsForm";
import CustomerDetailsForm from "../../components/onboarding/CustomerDetailsForm";
import { useQuery } from "@tanstack/react-query";
import Spinner from "react-bootstrap/Spinner";
import { useAuth } from "../../hooks/useAuth";
import { getCurrentStep } from "../../services/onboardingService";
import { showAlert } from "../../store/actions/alertsActions";
import { useOnboarding } from "../../hooks/useOnboarding";
import Button from "react-bootstrap/Button";

const Onboarding = () => {
  const { user } = useAuth();
  const {submitRoleDetails} = useOnboarding();
  const {data: currentStep, status: currentStepStatus, error} = useQuery({
    queryKey: ["currentStep"],
    queryFn: () => getCurrentStep(),
  });

  if (currentStepStatus === "pending" || !user) {
    return <Spinner animation="border" role="status"/>;
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

  const PlaceholderStep = () => {
    const roleId = user.roleId
    const details = {roleId, roleId}
    submitRoleDetails({ roleId, details});
  }

  const STEP_COMPONENTS = {
    1: UserDetailsForm,
    2: roleForms[user.roleId] || (() => <p>Role-specific form not found</p>),
  };

  return (
    <div>
      <h1>Onboarding</h1>
      {STEP_COMPONENTS[currentStep] &&
        React.createElement(STEP_COMPONENTS[currentStep])}
      {roleForms[user.roleId] ? (
        <></>
      ) : (
        <Button type="submit" onClick={PlaceholderStep}>
          Skip
        </Button>
      )}
    </div>
  );

};

export default Onboarding;
