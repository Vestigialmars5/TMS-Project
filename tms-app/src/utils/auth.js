import { jwtDecode } from "jwt-decode";

// Function to store JWT token in local storage
export const storeToken = (token) => {
    localStorage.setItem("token", token);
};

// Function to get JWT token from local storage
export const getToken = () => {
    return localStorage.getItem("token");
};

// Function to remove JWT token from local storage
export const removeToken = (token) => {
    localStorage.removeItem("token");
};

// Function to decode JWT token and get user info
export const decodeToken = (token) => {
    try {
        const decoded = jwtDecode(token);
        return decoded;
    } catch (error) {
        return null;
    }
};

// Function to check if user is authenticated
export const isAuthenticated = () => {
    const token = getToken();
    return token !== null && token != undefined;
};

// Function to authenticate user
export const authenticateUser = (token) => {
    if (token) {
        storeToken(token);
    }
};

export const isAuthorized = (requiredRole) => {
    const token = getToken();
    const role = token.role;
    return role === requiredRole;
};