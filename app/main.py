from flask import Flask, request, jsonify
import time
import json
import os

app = Flask(__name__)

START_TIME = time.time()
DATA_FILE = "data.json"

def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_records(records):
    with open(DATA_FILE, "w") as f:
        json.dump(records, f)

@app.get("/health")
def health():
    uptime_seconds = int(time.time() - START_TIME)
    return jsonify(status="ok", uptime_seconds=uptime_seconds)

@app.get("/records")
def get_records():
    return jsonify(records=load_records())

@app.post("/records")
def create_record():
    body = request.get_json(silent=True)
    if not body or "message" not in body or not isinstance(body["message"], str):
        return jsonify(error="Invalid input. Provide JSON with a string field: message"), 400

    records = load_records()
    record = {"id": len(records) + 1, "message": body["message"], "ts": int(time.time())}
    records.append(record)
    save_records(records)

    return jsonify(created=record), 201

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5050)

