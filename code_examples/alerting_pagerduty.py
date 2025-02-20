import requests

def send_alert(error_message):
    requests.post("https://events.pagerduty.com/v2/enqueue", json={
        "routing_key": "YOUR_API_KEY",
        "event_action": "trigger",
        "payload": {"summary": error_message, "severity": "critical"}
    })
