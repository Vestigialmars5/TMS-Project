export const navigateBasedOnRole = (userRole, navigate) => {
    switch (userRole) {
        case "admin":
            navigate("/admin");
            break;
        default:
            console.error("Invalid user role:", userRole);
            navigate("/");
            break;
    }
};