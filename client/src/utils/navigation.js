// TODO: Make this flexible and probably incluede based on roleid
export const navigateBasedOnRole = (userRoleId, navigate) => {
    switch (userRoleId) {
        case 1:
            navigate("/admin");
            break;
        default:
            console.error("Invalid user role:", userRoleId);
            navigate("/");
            break;
    }
};