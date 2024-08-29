import server.utils.validations as validations
from server.extensions import db
from server.models.tms_models import User, Role
from server.utils.exceptions import DatabaseQueryError, DataValidationError
import random
import string
from server.utils.validations import user_exists
from server.utils.cleaners import clean_username
from server.utils.consts import MAX_USERNAME


# Usernames are in this format:
# username from domain + role id + (suffix)
def create_unique_username(username, role_id):
    # username must be able to spare 5 characters for: "#" or "-", role_id, and the suffix (max 2 digits). Or the random string (3 chars)
    # plus one extra
    n = len(username)
    if n >= MAX_USERNAME - 5:
        username = username[:MAX_USERNAME - 5]

    new_username = f"{username}{role_id}"

    # Base case, most cases will hit this only
    if not user_exists(username=new_username):
        return new_username

    # Else add the suffix
    try:
        similar_usernames = db.session.query(User).filter(
            User.username.like(f"{new_username}%")).all()
    except:
        raise DatabaseQueryError("Error Getting Similar Usernames")

    similar_usernames_set = {user.username for user in similar_usernames}

    count = len(similar_usernames_set)
    username_with_count = f"{new_username}#{count+1}"

    while count < 50:
        if username_with_count not in similar_usernames_set:
            return username_with_count
        count += 1
        username_with_count = f"{new_username}#{count}"

    # As a fallback append a random string
    return f"{username}{role_id}-{generate_random_string(2)}"


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.punctuation, k=length))
