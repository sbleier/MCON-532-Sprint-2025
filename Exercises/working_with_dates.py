from datetime import datetime

from django.utils.timezone import now

d1 = datetime.strptime("07-05-2025", "%d-%m-%Y")
d2 = datetime.strptime("May 7, 2025 2:30 PM", "%B %d, %Y %I:%M %p")
d3 = datetime.strptime("2025/05/07 14:30:00", "%Y/%m/%d %H:%M:%S")

print("Month-Day-Year:", now.strftime("%m-%d-%Y"))
print("Hour:Minute AM/PM:", now.strftime("%I:%M %p"))
print("Log Timestamp:", now.strftime("[%d/%b/%Y:%H:%M:%S]"))

import pytz

utc_now = datetime.now(pytz.utc)
print("UTC Time:", utc_now)

from pytz import timezone
los_angeles = timezone('America/Los_Angeles')
local_time = utc_now.astimezone(los_angeles)
print("Eastern Time:", local_time)

from datetime import timedelta

d4 = datetime(2025, 5, 7)
d5 = datetime(2025, 12, 25)

difference = d5 - d4
print("Difference in days:", difference.days)