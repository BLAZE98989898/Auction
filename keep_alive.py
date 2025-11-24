#!/usr/bin/env python3
"""
Keep Alive Script for Telegram Bot Deployment on Render
Simple and compatible version
"""

import os
import threading
import time
from flask import Flask, jsonify

app = Flask(__name__)

# Get the port from environment variable or default to 10000
PORT = int(os.environ.get('PORT', 10000))

@app.route('/')
def home():
    """Root endpoint showing bot status"""
    return jsonify({
        "message": "🤖 Pokemon Auction Bot is running!",
        "status": "active",
        "service": "telegram-bot"
    })

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({"status": "healthy"})

def run_flask_app():
    """Run the Flask app"""
    try:
        print(f"🌐 Starting keep-alive server on port {PORT}")
        app.run(host='0.0.0.0', port=PORT, debug=False, threaded=True)
    except Exception as e:
        print(f"❌ Flask app error: {e}")

def start_keep_alive():
    """Start the keep-alive server in a separate thread"""
    try:
        flask_thread = threading.Thread(target=run_flask_app, daemon=True)
        flask_thread.start()
        print("✅ Keep-alive server started successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to start keep-alive server: {e}")
        return False

if __name__ == '__main__':
    print("🚀 Starting keep-alive server...")
    start_keep_alive()
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 Keep-alive server stopped")
