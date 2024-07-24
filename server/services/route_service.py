from server.db import get_db
class RouteService:
    
    @staticmethod
    def get_routes():
        try:
            db = get_db()
            routes = db.execute("SELECT * FROM routes").fetchall()
        except:
            abort(500, description="Error handling db")