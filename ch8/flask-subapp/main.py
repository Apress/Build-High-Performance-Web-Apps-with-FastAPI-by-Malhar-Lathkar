from flask import Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def index_flask():
    return "Hello World from Flask!"

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World from FastAPI!"}

from fastapi.middleware.wsgi import WSGIMiddleware
app.mount("/flask", WSGIMiddleware(flask_app))
