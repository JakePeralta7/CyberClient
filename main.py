# Imports
import datetime
import time

# assigned regular string date
date_time = datetime.datetime(2021, 7, 26, 21, 20)

# print regular python date&time
print("date_time =>",date_time)

# displaying unix timestamp after conversion
print("unix_timestamp => ", (time.mktime(date_time.timetuple())))
