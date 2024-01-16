from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/first-test")
def first_test():
    return {"test": ["first", "second"]}

if __name__ == "__main__":
    app.run(debug=True)