import { useNavigate } from "react-router-dom"

const navigate = useNavigate();

export const navigateBasedOnRole = (userRole) => {
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