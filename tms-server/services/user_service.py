import logging
from db import get_db


class UserService:
    @staticmethod
    def get_users(search, sort, page, limit):
        try:
            db = get_db()
            query, params = UserService._construct_query(search, sort, page, limit)

            try:
                res = db.execute(query, tuple(params))
            except:
                logging.exception("")
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
