import requests
import json

API_KEY = 'a1b97a25d071239a52f4547ef2a506a0e7b0b33b701a3437208bf4eadd33551674e887a7b6bd34b8'

def ip_reputation_check(ip):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    print(f"IP Address: {ip}")
    print(f"Abuse Confidence Score: {data['data']['abuseConfidenceScore']}")
    print(f"ISP: {data['data']['isp']}")
    print(f"Usage Type: {data['data']['usageType']}\n")

ip_list = ['95.163.255.16', '45.146.164.110', '95.163.255.12']

for ip in ip_list:
    ip_reputation_check(ip)