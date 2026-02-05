# api-sim-data

This project simulates an API environment to capture and analyze network traffic data from both automated bots and human interactions. Note that this project captures data for educational/ML purposes.

## Project Structure

- **`api.py`**: A Flask-based web server that exposes `/login` and `/search` endpoints. It logs details of every incoming request (Timestamp, IP, Endpoint, Method, etc.) to a CSV file.
- **`botsimulator.py`**: A python script that simulates bot behavior by sending automated, periodic requests to the API.

## Prerequisites

- Python 3.x
- `pip` package manager

Install the required Python libraries:

```bash
pip install flask requests
```

## How to Run

### 1. Start the API Server
Open a terminal in the project directory and run:

```bash
python api.py
```
*This will start the server at `http://127.0.0.1:5000` and create/reset the `api_logs.txt` file.*

### 2. Capture Bot Data
While the API server is running, open a **second terminal** and run the bot simulator:

```bash
python botsimulator.py
```
*This acts as a bot, sending requests with fixed time intervals to `/login` and `/search`.*

### 3. Capture Human Data
To generate "Human" data, manually interact with the API while the server is running:
- Open your web browser and navigate to: `http://127.0.0.1:5000/search`
- Refresh the page at random intervals.
- You can also use tools like **Postman** or **curl** to send POST requests to `http://127.0.0.1:5000/login`.

## Data Output
All traffic is logged to `api_logs.txt` in the root directory. The log includes:
- Timestamp
- IP Address
- Endpoint
- HTTP Method
- Response Code
- Request Time Gap (Placeholder)
- Label (Default: Unknown)
