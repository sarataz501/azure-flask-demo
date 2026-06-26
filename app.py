from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Azure Web App is Working!</h1>
    <p>Congratulations, your Flask app is deployed.</p>
    """

@app.route("/hello")
def hello():
    return {"message": "Hello from Azure"}