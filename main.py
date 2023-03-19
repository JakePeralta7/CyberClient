# Imports
import datetime
import time
import requests
import platform
import multiprocessing
import pyuac
import psutil

# Constants
API_URL = "http://ubuntu-cyber.elad.net:5000/api"


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
            current_event = dict(cpu_percentage=cpu_percentage, ram_percentage=ram_percentage, ram_usage=ram_usage)
            send_event(event_type='metrics', event=current_event)


class Agent(multiprocessing.Process):
    def __init__(self):
        super(Agent, self).__init__()

    def run(self):
        while True:
            agent_url = f"{API_URL}/agent"
            last_communication = time.mktime(datetime.datetime.now().timetuple())
            my_system = platform.uname()
            host = my_system.node
            operating_system = my_system.system
            os_release = my_system.release
            os_version = my_system.version
            machine = my_system.machine
            processor = my_system.processor
            requests.post(url=agent_url, json=dict(last_communication=last_communication, host=host,
                                                   operating_system=operating_system, os_release=os_release,
                                                   os_version=os_version, machine=machine, processor=processor))
            time.sleep(600)


def send_event(event_type: str, event: dict):
    event_url = f"{API_URL}/event"
    current_datetime = time.mktime(datetime.datetime.now().timetuple())
    host = platform.node()
    try:
        requests.post(url=event_url, json=dict(time=current_datetime,  event_type=event_type, host=host, event=event))
    except requests.exceptions.ConnectionError:
        print("Server isn't available")


def main():
    agent = Agent()
    agent.start()

    metrics_collector = MetricsCollector()
    metrics_collector.start()


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()
