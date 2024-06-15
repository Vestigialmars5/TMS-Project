import logging
from db import get_db
from werkzeug.security import generate_password_hash


class UserService:
    @staticmethod
    def get_users(search, sort, page, limit):
        try:
            db = get_db()
            query, params = UserService._construct_query(search, sort, page, limit)

            res = db.execute(query, tuple(params))
            rows = res.fetchall()
            users = []
            for row in rows:
                users.append(
                    {
                        "id": row["id"],
                        "username": row["username"],
                        "email": row["email"],
                        "role": row["role"],
                    }
                )

            return {"success": True, "users": users}, 200
        except:
            print("Error handling db")
            return {"success": False, "users": [], "error": "Error handling db"}, 400

    @staticmethod
    def create_user(email, password, role):

        username = email.split("@")[0]  # TODO: Make this different for uniqueness

        # TODO: Validations for registering

        try:
            db = get_db()
            db.execute(
                "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
                (username, email, generate_password_hash(password), role),
            )
            db.commit()
        except:
            print("Error handling db")
            return {"success": False, "error": "Error handling db"}, 400

        return {"success": True}, 200

    @staticmethod
    def _construct_query(search, sort, page, limit):
        if search:
            query = "SELECT * FROM users WHERE username LIKE ? "
            params = ["%" + search + "%"]
        else:
            query = "SELECT * FROM users "
            params = []

        if sort == "asc":
            query += "ORDER BY username ASC "
        else:
            query += "ORDER BY username DESC "

        offset = (page - 1) * limit
        query += "LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        return query, params
