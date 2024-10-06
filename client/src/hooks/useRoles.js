import { useQuery } from "@tanstack/react-query";
import { getRoles } from "../services/usersService";


export const useRoles = () => {
  return useQuery({ queryKey: ["roles"], queryFn: getRoles });
};
