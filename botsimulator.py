import requests
import time

# Bot hammers /login for credential stuffing
for i in range(20):  # 20 requests
    response = requests.post('http://127.0.0.1:5000/login')
    print(f"Bot request {i+1}: {response.status_code}")
    time.sleep(2)  # Fixed 2-sec gap, mechanical

# Bot scrapes /search
for i in range(20):
    response = requests.get('http://127.0.0.1:5000/search')
    print(f"Bot scrape {i+1}: {response.status_code}")
    time.sleep(1)  # Even faster 1-sec