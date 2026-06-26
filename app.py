from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Azure Web App is Working but from git sarat!</h1>
    <p>Congratulations, your Flask app is deployed from git.</p>
    """

@app.route("/hello")
def hello():
    return {"message": "This is via github actions deployment!"}