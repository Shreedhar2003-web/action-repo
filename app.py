from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Connect to MongoDB (use your Atlas URL here if you're using MongoDB Atlas)
client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB
db = client["webhookDB"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    action = data.get("action")
    author = data.get("sender", {}).get("login", "Unknown")
    timestamp = datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")

    # Message based on action
    if action == "push":
        msg = f'{author} pushed to a branch on {timestamp}'
    elif action == "opened":  # pull request
        msg = f'{author} submitted a pull request on {timestamp}'
    else:
        msg = f'{author} did {action} on {timestamp}'

    # Save to MongoDB
    collection.insert_one({"message": msg})
    return jsonify({"status": "stored"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0}))  # Remove MongoDB's internal _id field
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
