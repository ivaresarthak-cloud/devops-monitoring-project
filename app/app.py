from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUESTS = Counter('app_requests_total', 'Total Requests')

@app.route('/')
def home():
    REQUESTS.inc()
    return "Monitoring Enabled App!"

@app.route('/metrics')
def metrics():
    return generate_latest()

app.run(host='0.0.0.0', port=5000)
