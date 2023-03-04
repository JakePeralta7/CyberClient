# Imports
import datetime
import time
import requests
import platform


def send_event(event: dict):
    event_url = "http://ubuntu-cyber.elad.net:5000/api/event"
    host = platform.node()
    operating_system = platform.system()
    current_datetime = time.mktime(datetime.datetime.now().timetuple())
    a = requests.post(url=event_url, json={'time': current_datetime, 'host': host, 'operating_system': operating_system,
                                           'event': event})


def main():
    event = {
        'zibi': True,
        'semek': False
    }
    send_event(event)


if __name__ == "__main__":
    main()
