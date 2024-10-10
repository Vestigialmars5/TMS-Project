import React from "react";
import { useSelector } from "react-redux";
import LogoutButton from "../../components/auth/LogoutButton";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const authState = useSelector((state) => state.auth);
  const navigate = useNavigate();

  const handleLoginRedirect = () => {
    navigate("/login");
  };


  return (
    // TODO: Make a component for this
    <div className="mainContainer">
      <div className={"titleContainer"}>
        <div>Welcome!</div>
      </div>
      <div>This is the home page.</div>


      {authState.isAuthenticated ? (
        <div className={"buttonContainer"}>
          <div>Your email address is {authState.user.email}</div>
          <div>Your role is {authState.user.roleName}</div>
          <LogoutButton />
        </div>
      ) : (
        <button onClick={handleLoginRedirect}>Go To Login</button>
      )}
    </div>
  );
};

export default Home;
