import { jwtDecode } from "jwt-decode";

export const tokenService = {
  setTokens: (accessToken, refreshToken) => {
    localStorage.setItem(
      "authTokens",
      JSON.stringify({ accessToken, refreshToken })
    );
  },
  setAccessToken: (accessToken) => {
    const tokens = tokenService.getTokens();
    if (tokens) {
      tokens.accessToken = accessToken;
      tokenService.setTokens(tokens.accessToken, tokens.refreshToken);
    }
  },
  setRefreshToken: (refreshToken) => {
    const tokens = tokenService.getTokens();
    if (tokens) {
      tokens.refreshToken = refreshToken;
      tokenService.setTokens(tokens.accessToken, tokens.refreshToken);
    }
  },
  getTokens: () => {
    const tokens = localStorage.getItem("authTokens");
    return tokens ? JSON.parse(tokens) : null;
  },
  removeTokens: () => {
    localStorage.removeItem("authTokens");
  },
  getAccessToken: () => {
    const tokens = tokenService.getTokens();
    return tokens ? tokens.accessToken : null;
  },
  getRefreshToken: () => {
    const tokens = tokenService.getTokens();
    return tokens ? tokens.refreshToken : null;
  },
  decodeToken: (token) => {
    try {
      return jwtDecode(token);
    } catch (error) {
      return null;
    }
  },
};

export default tokenService;
