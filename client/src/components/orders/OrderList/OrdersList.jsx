import React, { useCallback, useState } from "react";
import SearchBox from "../../common/SearchBox";
import Tab from "react-bootstrap/Tab";
import ListGroup from "react-bootstrap/ListGroup";
import { useQuery } from "@tanstack/react-query";
import { debounce } from "../../../utils/utils";
import { showAlert } from "../../../store/actions/alertsActions";
import { getOrders } from "../../../services/orderService";
import OrderCard from "./OrderCard";
import Spinner from "react-bootstrap/Spinner"

const OrdersList = () => {
  const [searchField, setSearchField] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");
  const [sortBy, setSortBy] = useState("referenceId");
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(10);
  const [total, setTotal] = useState(0);

  const {
      data: orders,
      isLoading,
      error,
    } = useQuery({
      queryKey: ["orders", searchField, sortBy, sortOrder, page, limit],
      queryFn: () => getOrders({ searchField, sortBy, sortOrder, page, limit }),
      config: {
        keepPreviousData: true,
      },
    });

  const handleSearchChange = useCallback(
    debounce((e) => {
      setSearchField(e.target.value);
      setPage(1);
    }, 300),
    []
  );

  if (error) {
      const message =
        error.response?.data?.description ||
        error.response?.data?.error ||
        "An Unknown Error Occurred";
      console.error(error);
      showAlert(`Error Retrieving Orders: ${message}`, "danger");
    }

  return (
    <div>
      <SearchBox searchChange={handleSearchChange} />
      <Tab.Container id="orders-list" defaultActiveKey="#Id">
        <ListGroup horizontal>
          <ListGroup.Item action href="#Id">
            Id/Reference Number
          </ListGroup.Item>
          <ListGroup.Item action href="#CustomerId">
            Customer Id
          </ListGroup.Item>
          <ListGroup.Item action href="#Total">
            Total
          </ListGroup.Item>
          <ListGroup.Item action href="#Status">
            Status
          </ListGroup.Item>
          <ListGroup.Item action href="#Actions">
            Actions
          </ListGroup.Item>
        </ListGroup>
        <Tab.Content>
          <Tab.Pane eventKey="#Id"></Tab.Pane>
          <Tab.Pane eventKey="#Customer"></Tab.Pane>
          <Tab.Pane eventKey="#Total"></Tab.Pane>
          <Tab.Pane eventKey="#Status"></Tab.Pane>
          <Tab.Pane eventKey="#Actions"></Tab.Pane>
        </Tab.Content>
      </Tab.Container>
      {isLoading ? (
        <Spinner animation="border" />
      ) : error ? (
        <p>Try Again...</p>
      ) : orders && orders.length > 0 ? (
        orders.map((user, index) => <OrderCard key={index} order={order} />)
      ) : (
        <p>No Orders Found</p>
      )}
    </div>
  );
};

export default OrdersList;
