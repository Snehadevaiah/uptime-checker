import requests
import time

# URL of the application to check
url = "http://your-application-url.com"

# Interval between checks in seconds
interval = 60

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The application is UP. Status code: {response.status_code}")
        else:
            print(f"The application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"The application is DOWN. Error: {e}")

if _name_ == "_main_":
    while True:
        check_application_status(url)
        time.sleep(interval)
