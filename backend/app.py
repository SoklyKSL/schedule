from flask import Flask, request, jsonify, send_from_directory
from db import add_or_update_user
import os

app = Flask(__name__, static_folder="static")

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    added = add_or_update_user(
        telegram_id=str(data['telegram_id']),
        name=data['name'],
        phone_number=data.get('phone_number'),
        role='user'
    )
    return jsonify({"status": "new" if added else "existing"})
