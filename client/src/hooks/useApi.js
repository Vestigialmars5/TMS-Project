/* import { useState, useCallback } from "react";

export const useApi = (apiFunc) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const execute = useCallback(
    async (...args) => {
      try {
        setLoading(true);
        setError(null);
        const result = await apiFunc(...args);
        setData(result.data);
        console.log("useApi.js");
        return result.data;
      } catch (err) {
        setError(err.response?.data?.message || "An unexpected error occurred");
        throw err;
      } finally {
        setLoading(false);
      }
    },
    [apiFunc]
  );

  return { data, error, loading, execute };
};


 */