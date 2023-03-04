# Imports
import datetime
import time
import requests

unix_timestamp = time.mktime(datetime.datetime.now().timetuple())
url = "http://10.0.0.98:5000/"
requests.post()

# displaying unix timestamp after conversion
print("unix_timestamp => ", unix_timestamp)
