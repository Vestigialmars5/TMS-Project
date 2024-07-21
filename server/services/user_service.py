import logging
import sqlite3
from server.db import get_db
from werkzeug.security import generate_password_hash
from flask import abort


class UserService:
    @staticmethod
    def get_users(search, sort, page, limit):
        """
        Get all users.

        @param search (str): The search query.
        @param sort (str): The sort order.
        @param page (int): The page number.
        @param limit (int): The number of items per page.
        @return (dict, int): The response and status code.
        """
        try:
            db = get_db()
            query, params = UserService._construct_query(search, sort, page, limit)

            res = db.execute(query, tuple(params))        
            rows = res.fetchall()
            users = []

            for row in rows:
                users.append(
                    {
                        "userId": row["user_id"],
                        "username": row["username"],
                        "email": row["email"],
                        "roleId": row["role_id"],
                        "roleName": row["role_name"],
                    }
                )
            return {"success": True, "users": users}, 200

        except sqlite3.OperationalError as e:
            return {"success": False, "users": [], "error": "Error handling db", "description": str(e)}, 500
        except Exception as e:
            return {"success": False, "users": [], "error": "Exception", "description": str(e)}, 500

    @staticmethod
    def create_user(email, password, role_id):
        """
        Create a user.

        @param email (str): The email of the user.
        @param password (str): The password of the user.
        @param role_id (int): The role_id of the user.
        @return (dict, int): The response and status code.
        """

        username = email.split("@")[0]  # TODO: Make this different for uniqueness

        # TODO: Validations for registering

        try:
            db = get_db()
            db.execute(
                "INSERT INTO users (username, email, password, role_id) VALUES (?, ?, ?, ?)",
                (username, email, generate_password_hash(password), role_id),
            )
            db.commit()
        except:
            abort(500, description="Error handling db")

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
            db = get_db()
            db.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            db.commit()
        except:
            abort(500, description="Error handling db")
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
    def _construct_query(search, sort, page, limit):
        """
        Construct the query for getting users.

        @param search (str): The search query.
        @param sort (str): The sort order.
        @param page (int): The page number.
        @param limit (int): The number of items per page.
        @return (str, list): The query and params.
        """

        base_query = """
            SELECT users.user_id,
                users.username,
                users.email,
                users.role_id,
                roles.role_name
            FROM users
            JOIN roles ON users.role_id = roles.role_id
        """
        params = []

        if search:
            base_query += " WHERE username LIKE ?"
            params.append("%" + search + "%")

        if sort == "asc":
            base_query += " ORDER BY users.username ASC"
        else:
            base_query += " ORDER BY users.username DESC"

        offset = (page - 1) * limit
        base_query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        return base_query, params
