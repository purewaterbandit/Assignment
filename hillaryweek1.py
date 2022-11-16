# app.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

word = ["TALENT PLUS"]

@app.get("/word")
def get_word():
    return (word)

@app.post("/word")
def add_word():
    if request.is_json:
        word = request.get_json()
        response=word
        print(response.status_code)
        return word, 201
    return {"error": "Request must be JSON"}, 415
