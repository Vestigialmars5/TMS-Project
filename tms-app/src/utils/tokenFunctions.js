import { jwtDecode } from "jwt-decode";

// Function to store JWT token in local storage
export const storeToken = (token) => {
  localStorage.setItem("token", token);
};

// Function to get JWT token from local storage
export const getToken = () => {
  return localStorage.getItem("token"); // Null if no token
};

// Function to remove JWT token from local storage
export const removeToken = () => {
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
