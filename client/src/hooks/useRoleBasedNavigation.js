import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

export const useRoleBasedNavigation = () => {
  const navigate = useNavigate();

  const goToDashboard = (roleId) => {
    switch (roleId) {
      case 1:
        navigate("/admin");
        break;
      default:
        console.error("Invalid user role:", roleId);
        navigate("/");
        break;
    }
  };

  return {
    goToDashboard,
  };
};
