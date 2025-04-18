import { useDispatch } from "react-redux";
import { setOrders, addOrder, removeOrder } from "../store/slices/ordersSlice";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import * as orderService from "../services/orderService";
import { showAlert } from "../store/actions/alertsActions";

export const useOrders = () => {
  const queryClient = useQueryClient();
  const dispatch = useDispatch();

  const createOrderMutation = useMutation({
    mutationFn: (order) => orderService.createOrder(order),
    onSuccess: (responseData, variables) => {
      showAlert("Order Created Successfully", "success");
      queryClient.invalidateQueries("orders");
      dispatch(addOrder(variables));
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
