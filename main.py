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
        while True:

            # Calling psutil.cpu_precent() for 10 seconds
            cpu_percentage = psutil.cpu_percent(10) * 10
            print('The CPU usage is: ', cpu_percentage)

            # Getting % usage of virtual_memory ( 3rd field)
            ram_percentage = psutil.virtual_memory()[2]
            print('RAM memory % used:', ram_percentage)

            # Getting usage of virtual_memory in GB ( 4th field)
            ram_usage = psutil.virtual_memory()[3] / 1000000000
            print('RAM Used (GB):', ram_usage)
            current_event = {
                'cpu_percentage': cpu_percentage,
                'ram_percentage': ram_percentage,
                'ram_usage': ram_usage
            }
            # send_event()


def send_event(event_type: str, event: dict):
    event_url = "http://ubuntu-cyber.elad.net:5000/api/event"
    current_datetime = time.mktime(datetime.datetime.now().timetuple())
    my_system = platform.uname()
    host = my_system.node
    operating_system = my_system.system
    os_release = my_system.release
    os_version = my_system.version
    machine = my_system.machine
    processor = my_system.processor
    a = requests.post(url=event_url, json={'time': current_datetime, 'host': host, 'event_type': event_type,
                                           'operating_system': operating_system, 'os_release': os_release,
                                           'os_version': os_version, 'machine': machine, 'processor': processor,
                                           'event': event})
    print(a)


def main():
    metrics_collector = MetricsCollector()
    metrics_collector.start()
    metrics_collector.join()


if __name__ == "__main__":
    main()


import psutil
