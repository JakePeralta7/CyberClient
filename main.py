# Imports
import datetime
import time
import requests
import platform
import multiprocessing


class MetricsCollector(multiprocessing.Process):
    def __init__(self):
        super(MetricsCollector, self).__init__()

    def run(self):
        send_event()
        time.sleep(1)


def send_event(event: dict):
    event_url = "http://ubuntu-cyber.elad.net:5000/api/event"
    my_system = platform.uname()
    host = my_system.node
    operating_system = my_system.system
    os_release = my_system.release
    os_version = my_system.version
    machine = my_system.machine
    processor = my_system.processor
    current_datetime = time.mktime(datetime.datetime.now().timetuple())
    a = requests.post(url=event_url, json={'time': current_datetime, 'host': host, 'operating_system': operating_system,
                                           'os_release': os_release, 'os_version': os_version, 'machine': machine,
                                           'processor': processor, 'event': event})
    print(a)


def main():
    event = {
        'zibi': True,
        'semek': False
    }
    send_event(event)


if __name__ == "__main__":
    main()
