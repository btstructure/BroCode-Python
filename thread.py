#thread is a flow of execution. Like a separe order of instructions.
#However each thread takes a turn running to achieve concurrency.
#GIL = (global interpreter lock)
#allows only one thread to hold the control of Python interpreter at any one time

#cpu bound = program/task spends most of it's time waiting for internal events, use for multiprocessing

#io bound = program/task spends most of it's time waiting for external events, use for multithreading

import threading
import time



def eat_breakfest():
    time.sleep(3)
    print("You eat breakfest")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep
    print("You finished studying")

eat_breakfest()
drink_coffee()
study()

#1 thread is running these functions concurrently

print(threading.active_count())
print(threading.enumerate())