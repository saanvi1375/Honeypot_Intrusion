from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB connection setup
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["honeypot"]
logs_collection = db["logs"]

# Basic home route
@app.route("/")
def home():
    return "Honeypot backend is running!"

# Log incoming connection attempts
from bson import ObjectId

import ipapi
from ipwhois import IPWhois

@app.route("/log", methods=["POST"])
def log_connection():
    data = request.json
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    print(f"Received connection from: {ip}")

    # Geolocation info
    geo_info = ipapi.location(ip, output='json') if ip != "127.0.0.1" else {}

    # WHOIS info
    try:
        whois_info = IPWhois(ip).lookup_rdap() if ip != "127.0.0.1" else {}
    except Exception as e:
        whois_info = {"error": str(e)}

    log_entry = {
        "ip": ip,
        "port": data.get("port"),
        "timestamp": datetime.utcnow(),
        "description": data.get("description", "Attempted connection"),
        "severity": data.get("severity", "info"),
        "geo": {
            "city": geo_info.get("city"),
            "region": geo_info.get("region"),
            "country": geo_info.get("country_name"),
            "org": geo_info.get("org"),
            "asn": geo_info.get("asn")
        },
        "whois": {
            "asn_description": whois_info.get("asn_description"),
            "network_name": whois_info.get("network", {}).get("name"),
            "org": whois_info.get("network", {}).get("org"),
        }
    }

    logs_collection.insert_one(log_entry)
    return jsonify({"status": "logged", "entry": log_entry})


# Get all logs
@app.route("/logs", methods=["GET"])
def get_logs():
    logs = list(logs_collection.find({}, {"_id": 0}))
    return jsonify(logs)

# Run the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)