import { useDispatch, useSelector } from "react-redux";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { showAlert } from "../store/actions/alertsActions";
import * as usersService from "../services/usersService";

export const useUsers = () => {
  const queryClient = useQueryClient();

  const createUserMutation = useMutation({
    mutationFn: (user) => usersService.createUser(user),
    onSuccess: () => {
      queryClient.invalidateQueries("users");
      showAlert("User Created Successfully", "success");
    },
    onError: (error) => {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      showAlert(`Error Creating User: ${message}`, "danger");
    },
  });

  const updateUserMutation = useMutation({
    mutationFn: (user) => usersService.updateUser(user),
    onSuccess: () => {
      queryClient.invalidateQueries("users");
      showAlert("User Updated Successfully", "success");
    },
    onError: (error) => {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      showAlert(`Error Updating User: ${message}`, "danger");
    },
  });

  const createUser = (user) => createUserMutation.mutate(user);
  const updateUser = (user) => updateUserMutation.mutate(user);


  return {
    createUser,
    updateUser,
    createUserStatus: createUserMutation.status,
    updateUserStatus: updateUserMutation.status,
  };
};
