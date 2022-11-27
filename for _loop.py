#for loop = a statement that will execute it's block of code a limited amount of times
#unlike a while loop, a for loop is limited

import time 
#counting up to ten

#in python i will start at 0
# for i in range(10):
    #print(i)
    # print(i+1)

#the second number is exclusive, without +1 it'll stop at 99
# for j in range(50,100+1):
#     print(j)

# for x in "Bilbo":
#     print(x)

#a countdown that starts at 10 and ends at 0, the -1 is the counter, it'll count down by 1
for seconds in range(10,0,-1):
    print(seconds)
    #time.sleep counts by the second
    time.sleep(1)

print("Happy New Year!")