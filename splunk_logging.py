import requests
import json

splunkURL = 'https://splunk-server:8088/services/collector'
splunkToken = 'splunk-token'

def logToSplunk(alertMessage):
    headers = {
        'Authorization': 'Splunk ' + splunkToken,
    }
    data = {
        "event": alertMessage
    }

    response = requests.post(splunkURL, headers=headers, json=data)
    
    if (response.status_code != 200):
        print(f"Failed to log to Splunk: {response.text}")