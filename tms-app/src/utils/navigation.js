// TODO: Make this flexible
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