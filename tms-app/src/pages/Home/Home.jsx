import React from "react";
import { useAuth } from "../../context/AuthProvider";

const Home = () => {
  const { isLoggedIn, user } = useAuth();

  return (
    // TODO: Make a component for this
    <div className="mainContainer">
      <div className={"titleContainer"}>
        <div>Welcome!</div>
      </div>
      <div>This is the home page.</div>
      <div className={"buttonContainer"}>
        {isLoggedIn ? <div>Your email address is {user.email}</div> : <div />}
        {isLoggedIn ? <div>Your role is {user.role}</div> : <div />}
      </div>
    </div>
  );
};

export default Home;
