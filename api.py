from flask import Flask, request
import datetime
import os

app = Flask(__name__)

# Log file
LOG_FILE = 'api_logs.txt'

# Function to log requests
def log_request():
    timestamp = datetime.datetime.now().isoformat()
    ip = request.remote_addr  # Will be 127.0.0.1 for local
    endpoint = request.path
    method = request.method
    response_code = 200  # Fake success for now; we'll simulate failures manually/automatically
    time_gap = '0'  # We'll calculate this later if needed; for now, skip
    label = 'Unknown'  # We'll assign Normal/Bot later

    log_entry = f"{timestamp},{ip},{endpoint},{method},{response_code},{time_gap},{label}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

@app.route('/login', methods=['POST'])
def login():
    log_request()
    return 'Login response', 200  # Or 401 for failure, but keep simple

@app.route('/search', methods=['GET'])
def search():
    log_request()
    return 'Search results', 200

if __name__ == '__main__':
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)  # Clear old logs
    with open(LOG_FILE, 'w') as f:
        f.write('Timestamp,IP Address,Endpoint,HTTP Method,Response Code,Request Time Gap,Label\n')  # Header
    app.run(debug=True)