#time module 

import time 

print(time.ctime((0))) #ctime() returns the current time in a readable format. 0 is the epoch time that is expressed in seconds, the time at which the computer "thinks" time started

print(time.time()) #time() returns the current time in seconds since the epoch time

print(time.ctime(time.time())) #a way to get the current time in a readable format, using the ctime, we poss time as an argument, which is the current time in seconds since the epoch time

time_object = time.localtime() #localtime() returns the current time as a time object
print(time_object) #a struct time object made up of different key value pairs

#go to docs.python.org/3/library/time.html   to find out more about the time module, go to the strftime section to find out more about the format string
local_time = time.strftime("%B, %d, %Y: %H:%M:%S", time_object) #strftime() returns a string representing the time object in the format specified by the format string
print(local_time)