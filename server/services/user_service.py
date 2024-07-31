import logging
from server.extensions import db
from server.models.tms_models import User, Role
from werkzeug.security import generate_password_hash
from flask import abort


class UserService:
    @staticmethod
    def get_users(search, sort_by, sort_order, page, limit):
        """
        Get all users.

        @param search (str): The search query.
        @param sortBy (str): The sort by field.
        @param sortOrder (str): The sort order.
        @param page (int): The page number.
        @param limit (int): The number of items per page.
        @return (dict, int): The response and status code.
        """
        try:
            users = UserService._construct_query(
                search, sort_by, sort_order, page, limit)

        except Exception as e:
            abort(500, description=str(e))

        return {"success": True, "users": users}, 200

    @staticmethod
    def create_user(email, password, role_id):
        """
        Create a user.

        @param email (str): The email of the user.
        @param password (str): The password of the user.
        @param role_id (int): The role_id of the user.
        @return (dict, int): The response and status code.
        """

        # TODO: Make this different for uniqueness
        username = email.split("@")[0]

        # TODO: Validations for registering

        try:
            password_hash = generate_password_hash(password)
            user = User(username=username, email=email,
                        password=password_hash, role_id=role_id)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            abort(500, description=str(e))

        return {"success": True}, 200

    @staticmethod
    def delete_user(user_id):
        """
        Delete a user.

        @param user_id (int): The id of the user.
        @return (dict, int): The response and status code.
        """
        # TODO: Validations for deleting

        try:
            db.session.query(User).filter(User.user_id == user_id).delete()
            db.session.commit()
        except Exception as e:
            abort(500, description=str(e))
        return {"success": True}, 200

    @staticmethod
    def update_user(user_id, username, email, role_id):
        """
        Update a user.

        @param user_id (int): The id of the user.
        @param username (str): The username of the user.
        @param email (str): The email of the user.
        @param role_id (int): The role_id of the user.
        @return (dict, int): The response and status code.
        """

        # TODO: Validations for updating
        try:
            db = get_db()
            db.execute(
                "UPDATE users SET username = ?, email = ?, role_id = ? WHERE user_id = ?",
                (
                    username,
                    email,
                    role_id,
                    user_id,
                ),
            )
            db.commit()
        except:
            abort(500, description="Error handling db")
        return {"success": True}, 200

    @staticmethod
    def _construct_query(search, sort_by, sort_order, page, limit):
        """
        Construct the query for getting users.

        @param search (str): The search query.
        @param sort (str): The sort order.
        @param page (int): The page number.
        @param limit (int): The number of items per page.
        @return (str, list): The query and params.
        """

        query = db.session.query(User).join(Role)
        print(f"Query: {query}")


        print(f"Search: {search}")
        if search:
            search_filter = f"%{search}%"
            query = query.filter(
                (User.username.like(search_filter)) |
                (User.email.like(search_filter)) |
                (Role.role_name.like(search_filter))
            )

        print(f"Sort By: {sort_by}, Sort Order: {sort_order}")
        if sort_by and sort_order:
            if sort_order == "asc":
                query.order_by(db.asc(sort_by))
            else:
                query.order_by(db.desc(sort_by))

        offset = (page - 1) * limit
        query = query.offset(offset).limit(limit)

        users = query.all()

        user_list = [user.to_dict_js() for user in users]
        print(f"User List: {user_list}")

        return user_list
