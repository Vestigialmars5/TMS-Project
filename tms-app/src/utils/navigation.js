// TODO: Make this flexible and probably incluede based on roleid
export const navigateBasedOnRole = (userRole, navigate) => {
    switch (userRole) {
        case "Admin":
            navigate("/admin");
            break;
        default:
            console.error("Invalid user role:", userRole);
            navigate("/");
            break;
    }
};