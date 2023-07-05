# I used this script to help solve the machine 'Help' on HacktheBox.
# The webserver is running in GMT.
# In order to calculate the filename, we need to calculate the epoch time of our upload POST request.
# We then md5sum our filetime + epoch time stamp to calculate its name.
 

import requests
import time
import sys

pattern = '%a, %d %b %Y %I:%M:%S %Z'

if len(sys.argv) == 2:
    epoch2 = int(time.mktime(time.strptime(sys.argv[1], pattern)))
    print(epoch2)
else:
    r = requests.head("http://help.htb/support/")
    date_str = r.headers["Date"]
    print("The Current time of the server is:",date_str)
    epoch = int(time.mktime(time.strptime(date_str, pattern)))
    print("The epoch time of that is:", epoch)
    print("If you want to convert to epoch, pass the time as an argument")
    print ("e.g.",sys.argv[0], '"Wed, 05 Jul 2023 12:22:21 GMT"')
