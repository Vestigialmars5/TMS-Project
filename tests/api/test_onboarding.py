from server.models.tms_models import Role, User, UserDetails
from server.extensions import db


def test_onboard_user(client, auth_token, user_not_onboarded):
    response = client.post("/api/onboarding/onboard", headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }, json={
        "email": "admin@admin.com",
        "password": "asdfasdf",
        "confirmation": "asdfasdf",
        "firstName": "Admin",
        "lastName": "Admin",
        "phoneNumber": "1234567890",
        "address": "123 Admin St.",
        "role_id": 1,
        "role_name": "admin"
    })



    assert response.status_code == 200
    assert response.json["success"] == True
    assert db.session.query(User).filter_by(email="admin@admin.com").first() is not None

    user = db.session.query(User).filter_by(email="admin@admin.com").first()
    
    assert user.user_details.first_name == "Admin"
    assert user.user_details.last_name == "Admin"
    assert user.user_details.phone_number == "1234567890"
    assert user.user_details.address == "123 Admin St."
    assert user.role_id == 1