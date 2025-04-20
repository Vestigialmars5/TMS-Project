# Test Guidelines

This document outlines the structure and best practices for writing tests in this project.

## Test File Structure

Each test file should follow this general structure:

```python
import pytest
from tests.utilstest import TestUtils, token_fixture
# Other imports

class TestFeatureName:
    """Brief description of what this test class covers"""

    @pytest.mark.parametrize(
        "param1, param2, ..., expected_status_code, expected_success",
        [
            # Test case 1 with descriptive comment
            (value1, value2, ..., status_code, success),
            # Test case 2 with descriptive comment
            (value1, value2, ..., status_code, success),
        ],
        ids=["case_1_description", "case_2_description"]
    )
    def test_endpoint_name(self, client, param1, param2, ..., expected_status_code, expected_success):
        """Docstring describing what this test verifies"""
        # Test implementation
        assert response.status_code == expected_status_code
        assert response.json["success"] == expected_success
```

## Best Practices

1. **Use Classes**: Organize related tests in classes named `Test[FeatureName]`
2. **Descriptive Names**: Use clear test method names starting with `test_`
3. **Parametrize Tests**: Use pytest's parametrize to test multiple scenarios
4. **Descriptive IDs**: Add ids to parametrized tests for better reporting
5. **Use Fixtures**: Create fixtures for common setup/teardown operations
6. **Use Helpers**: Use helper methods from `TestUtils` to reduce repetition
7. **Document Tests**: Add docstrings to test methods and classes
8. **Isolate Tests**: Each test should be independent and not rely on other tests

## Common Fixtures

- `client`: Flask test client
- `app`: Flask application object
- `token_fixture`: Parameterized fixture to get authentication tokens
- `auth_headers`: Factory to create authorization headers
- `get_user_id`: Factory to get user IDs by email

## Assertion Helpers

Use `TestUtils.assert_response_structure()` to check common response properties:

```python
TestUtils.assert_response_structure(
    response,
    expected_status_code,
    expected_success,
    expected_fields=["field1", "field2"] if expected_success else None
)
```

## Testing API Endpoints

Each endpoint should have tests for:

1. **Happy Path**: Valid inputs producing the expected result
2. **Validation**: Invalid inputs that should be rejected
3. **Authorization**: Ensuring only authorized users can access
4. **Error Handling**: Proper handling of errors and edge cases

## Example Test File

```python
# filepath: tests/api/test_example.py
import pytest
from tests.utilstest import token_fixture, TestUtils
import tests.consts as consts

class TestExample:
    """Tests for the example feature"""

    @pytest.mark.parametrize(
        "token_fixture, param, expected_status_code, expected_success",
        [
            # Valid case
            ("admin_token", "valid_value", 200, True),
            # Invalid case
            ("admin_token", "invalid_value", 400, False),
            # Unauthorized case
            ("", "valid_value", 401, False),
        ],
        ids=["valid", "invalid", "unauthorized"],
        indirect=["token_fixture"]
    )
    def test_example_endpoint(self, client, token_fixture, param,
                              expected_status_code, expected_success):
        """Test the example endpoint with various inputs"""
        response = client.post("/api/example", headers={
            "Authorization": f"Bearer {token_fixture}",
            "Content-Type": "application/json"
        }, json={
            "param": param
        })

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success
        )
```
