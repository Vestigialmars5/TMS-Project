def test_testing_config(app):
    assert app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
    assert app.config["SQLALCHEMY_BINDS"]["wms"] == "sqlite:///:memory:"