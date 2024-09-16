import { useDispatch, useSelector } from "react-redux";
import { loginUser, logoutUser } from "../store/slices/authSlice";
import { useRoleBasedNavigation } from "../hooks/useRoleBasedNavigation";
import { useNavigate } from "react-router-dom";

export const useAuth = () => {
  const dispatch = useDispatch();
  const authState = useSelector((state) => state.auth);
  const navigate = useNavigate();
  const { goToDashboard } = useRoleBasedNavigation();

  const login = async (credentials) => {
    try {
      const user = await dispatch(loginUser(credentials)).unwrap();
      goToDashboard(user.roleId);
    } catch (error) {
      // Do nothing
      console.log();
    }
  };

  const logout = () => {
    dispatch(logoutUser());
    navigate("/login");
  };

  return {
    ...authState,
    login,
    logout,
  };
};
