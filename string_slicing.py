# slicing - creates a substring by extacting elements from another string
#  indexing[] or slice()
# [start:stop:step]
# start - starting index
# stop - stopping index
# step - 

#start is inclusive and the stop is exclusive, first_name = name[0:5] will return Bilb
name = "Bilbo Baggins"
first_name = name[0:5] 
print(first_name)
last_name = name[6:14]
last_name_no_stop = name[6:]
print(last_name)
print(last_name_no_stop)
#step count every interval by the index
#if you leave the start and stop empty python will assume you start at index 0 and end at the last index
steps_name = name[::2]
print(steps_name)
#to reverse a string
reverse_name = name[::-1]
print(reverse_name)

#using slice

website = "http://google.com"
#slice uses a start, stop, and step but instead of colons, it uses commas
slice = slice(7, -4)
print(website[slice])