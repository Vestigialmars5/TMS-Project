from server.models.tms_models import Role, User, UserDetails
from server.extensions import db
from tests.utilstest import incomplete_user_token


def test_onboard_user(client, incomplete_user_token):
    response = client.post("/api/onboarding/onboard", headers={
        "Authorization": f"Bearer {incomplete_user_token}",
        "Content-Type": "application/json"
    }, json={
        "email": "test_user_not_onboarded@email.com",
        "password": "notOnboarded",
        "confirmation": "notOnboarded",
        "firstName": "Admin",
        "lastName": "Admin",
        "phoneNumber": "1234567890",
        "address": "123 Admin St.",
        "role_id": 1,
        "role_name": "admin"
    })



    assert response.status_code == 200
    assert response.json["success"] == True
    assert db.session.query(User).filter_by(email="test_user_not_onboarded@email.com").first() is not None

    user = db.session.query(User).filter_by(email="test_user_not_onboarded@email.com").first()
    
    assert user.user_details.first_name == "Admin"
    assert user.user_details.last_name == "Admin"
    assert user.user_details.phone_number == "1234567890"
    assert user.user_details.address == "123 Admin St."
    assert user.role_id == 1