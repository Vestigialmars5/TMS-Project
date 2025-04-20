import pytest


class TestConfig:
    """Test cases for application configuration settings."""

    def test_testing_config(self, app):
        """Verify the testing configuration is correctly loaded with appropriate settings."""
        assert app.config["TESTING"], "TESTING flag should be True"
        assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:", "Wrong database URI"
        assert app.config["SQLALCHEMY_BINDS"]["wms"] == "sqlite:///:memory:", "Wrong WMS database bind"

    def test_important_security_settings(self, app):
        """Verify security-related settings are properly configured."""
        assert app.config["JWT_SECRET_KEY"], "JWT_SECRET_KEY should be set"
        assert app.config["SECRET_KEY"], "SECRET_KEY should be set"
