import { useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";


export const useRoleBasedNavigation = () => {
  const navigate = useNavigate();
  // Get roleId from redux state considering user might be null
  const roleId = useSelector((state) => state.auth.user?.roleId);

  const goToDashboard = () => {
    switch (roleId) {
      case 1:
        navigate("/admin");
        break;
      case 4:
        navigate("/customer");
        break;
      case 8:
        navigate("/dispatcher");
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
