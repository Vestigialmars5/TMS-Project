import { getToken, removeToken, storeToken, decodeToken } from "./tokenFunctions";

const SERVER_URL = "http://localhost:5000";

export const onboardUserApi = async ({userData}) => {
    const token = getToken();
    try {
        const res = await fetch(`${SERVER_URL}/api/onboarding/details`, {
            method: "POST",
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
        });

        const response = await res.json();

        if (!res.ok) {
            console.log(response.description);
            throw new Error(response.error);
        } else {
            removeToken();
            const token = response.access_token;
            storeToken(token);
            return decodeToken(token);
        }
    } catch (error) {
        throw new Error(`Onboarding Failed: ${error.message}`);
    }
};