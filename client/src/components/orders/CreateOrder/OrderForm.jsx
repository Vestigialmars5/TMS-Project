import { useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import Form from "react-bootstrap/Form";
import Spinner from "react-bootstrap/Spinner";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const OrderForm = () => {
  const customerId = "123"; // Replace with actual customer ID from auth context
  const [deliveryAddress, setDeliveryAddress] = useState("");
  const [totalPrice, setTotalPrice] = useState(0);
  const [deliveryAddressError, setDeliveryAddressError] = useState("");

  const { products, loading } = {
    products: [
      { id: 1, name: "potatoes", basePrice: 10.99 },
      { id: 2, name: "tomatoes", basePrice: 8.99 },
      { id: 3, name: "carrots", basePrice: 5.99 },
    ],
    loading: false,
  }; // Placeholder until hook is added
  const [selectedProducts, setSelectedProducts] = useState({});

  useEffect(() => {
    const newTotal = products
      .filter((product) => selectedProducts[product.id])
      .reduce(
        (total, product) =>
          total + selectedProducts[product.id].quantity * product.basePrice,
        0
      );
    setTotalPrice(newTotal);
  }, [selectedProducts, products]);

  const handleProductSelect = (productId) => {
    const product = products.find((p) => p.id === productId);
    setSelectedProducts((prev) => ({
      ...prev,
      [productId]: prev[productId]
        ? undefined
        : {
            quantity: 1,
            basePrice: product.basePrice,
          },
    }));
  };

  const handleQuantityChange = (productId, quantity) => {
    setSelectedProducts((prev) => ({
      ...prev,
      [productId]: { ...prev[productId], quantity: parseInt(quantity) },
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const deliveryAddressErr = validateAddress(deliveryAddress);

    if (deliveryAddressErr) {
      setDeliveryAddressError(deliveryAddressErr);
      return;
    } else {
      createOrder({
        referenceId: uuidv4(),
        customerId,
        deliveryAddress,
        products: Object.keys(selectedProducts).map((key) => ({
          productId: key,
          productName: products.find((p) => p.id === key).name,
          quantity: selectedProducts[key].quantity,
          price:
            selectedProducts[key].quantity *
            products.find((p) => p.id === key).basePrice,
        })),
      });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <section className="mb-4">
        <h4>Order Details</h4>
        <Form.Group className="mb-3">
          <Form.Label>Customer ID</Form.Label>
          <Form.Control type="text" value={customerId} disabled />
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Delivery Address</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            value={deliveryAddress}
            onChange={(e) => setDeliveryAddress(e.target.value)}
            required
            isInvalid={!!deliveryAddressError}
          />
          <Form.Control.Feedback type="invalid">
            {deliveryAddressError}
          </Form.Control.Feedback>
        </Form.Group>
      </section>

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
              <Col>Base Price: ${product.basePrice}</Col>
              <Col>
                Subtotal: $
                {(
                  selectedProducts[product.id].quantity * product.basePrice
                ).toFixed(2)}
              </Col>
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

      <section>
        <h4>Total Price</h4>
        <p>${totalPrice.toFixed(2)}</p>
      </section>

      <Button type="submit">Create Order</Button>
    </Form>
  );
};

export default OrderForm;
