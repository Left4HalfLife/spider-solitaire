from pathlib import Path

from flask import Flask, send_from_directory


app = Flask(__name__, static_folder=None)


@app.get("/")
def index():
    return send_from_directory(Path(__file__).resolve().parent, "index.html")
