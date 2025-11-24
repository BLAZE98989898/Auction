#!/usr/bin/env python3
"""
Keep Alive Script for Docker Deployment
"""

import os
import threading
import time
from flask import Flask, jsonify

app = Flask(__name__)

PORT = int(os.environ.get('PORT', 10000))

@app.route('/')
def home():
    return jsonify({"status": "active", "message": "🤖 Pokemon Auction Bot"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

def run_server():
    app.run(host='0.0.0.0', port=PORT, debug=False)

def start_keep_alive():
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    print(f"✅ Keep-alive server started on port {PORT}")

if __name__ == '__main__':
    start_keep_alive()
    while True:
        time.sleep(60)
