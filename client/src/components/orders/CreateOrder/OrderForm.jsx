import { useState } from "react";
import Form from "react-bootstrap/Form";
import Spinner from "react-bootstrap/Spinner";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const OrderForm = () => {
  const { products, loading } = {
    products: [
      { id: 1, name: "potatoes" },
      { id: 2, name: "tomatoes" },
      { id: 3, name: "carrots" },
    ],
    loading: false,
  }; // Placeholder until hook is added
  const [selectedProducts, setSelectedProducts] = useState({});

  const handleProductSelect = (productId) => {
    setSelectedProducts((prev) => ({
      ...prev,
      [productId]: prev[productId] ? undefined : { quantity: 1 },
    }));
  };

  const handleQuantityChange = (productId, quantity) => {
    setSelectedProducts((prev) => ({
      ...prev,
      [productId]: { ...prev[productId], quantity: parseInt(quantity) },
    }));
  };

  const handleSubmit = () => {};

  return (
    <Form onSubmit={handleSubmit}>
      <section>
        <h4>Available Products</h4>
        {loading ? (
          <Spinner animation="border" />
        ) : (
          products.map((product) => (
            <Form.Check
              key={product.id}
              type="checkbox"
              label={product.name}
              checked={!!selectedProducts[product.id]}
              onChange={() => handleProductSelect(product.id)}
            />
          ))
        )}
      </section>

      <section>
        <h4>Selected Products</h4>
        {products
          .filter((product) => selectedProducts[product.id])
          .map((product) => (
            <Row key={product.id}>
              <Col>{product.name}</Col>
              <Col xs={4}>
                <Form.Control
                  type="number"
                  min="1"
                  value={selectedProducts[product.id].quantity}
                  onChange={(e) =>
                    handleQuantityChange(product.id, e.target.value)
                  }
                />
              </Col>
            </Row>
          ))}
      </section>

      <Button type="submit">
        Create Order
      </Button>
    </Form>
  );
};

export default OrderForm;
