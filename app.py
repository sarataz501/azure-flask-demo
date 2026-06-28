from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Azure Web App is Working!</h1>
    <p>Congratulations, your Flask app is deployed sarat.</p>
    """

@app.route("/config")
def config():
    environment = os.environ.get("ENVIRONMENT", "Not Set")

    return {
        "environment": environment
    }

@app.route("/hello")
def hello():
    return {"message": "Hello from Azure sarat"}