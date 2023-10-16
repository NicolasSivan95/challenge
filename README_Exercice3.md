# IP Reputation Check Script

## Description

This script uses the API of AbuseIPDB to check the reputation of given IP addresses. It prints the reputation check details for the IPs, such as the Abuse Confidence Score, ISP, and Usage Type.

## Dependencies

This script requires Python 3 and the `requests` Python library. 

## Installation

To install the necessary dependencies, run:

```
pip install requests
```

## Usage

The variable API_KEY has been set with my key. Feel free to change with yours by signing up on the AbuseIPDB website.

To run the script, execute the following in a terminal:

```
python ip_reputation_check.py
```

Where `ip_reputation_check.py` is the filename of the script.

## IPs

You can change the IP addresses to be checked in the `ip_list` variable in the script. 