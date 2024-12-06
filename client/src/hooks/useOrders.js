import { useMutation, useQueryClient } from "@tanstack/react-query";
import * as orderService from "../services/orderService";
import { showAlert } from "../store/actions/alertsActions";

export const useOrders = () => {
  const queryClient = useQueryClient();

  const createOrderMutation = useMutation({
    mutationFn: (order) => orderService.createOrder(order),
    onSuccess: () => {
      queryClient.invalidateQueries("orders");
      showAlert("Order Created Successfully", "success");
    },
    onError: (error) => {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      showAlert(`Error Creating Order: ${message}`, "danger");
    },
  });

  const createOrder = (order) => createOrderMutation.mutate(order);

  return {
    createOrder,
    createOrderStatus: createOrderMutation.status,
  };
};
