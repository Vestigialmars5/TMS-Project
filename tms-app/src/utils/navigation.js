import { useNavigate } from "react-router-dom"


export const navigateBasedOnRole = (userRole) => {
    const navigate = useNavigate();
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