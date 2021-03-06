# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:03:26 2018

@author: Mohammad SAFEEA

Test script of iiwaPy class.

"""
from iiwaPy import iiwaPy
import time
from threading import Thread
from queue import LifoQueue

def poll_pos(pos,):
    # read some data from the robot
    while True:
        try:
            pos.put(iiwa.getEEFPos())
            time.sleep(1)
        
        except BrokenPipeError:
            print("Connection closed")
            return
        except Exception as E:
            print('The following error happended in obtaining positions: \n')
            print(E)
            return
    
    
    return


ip='172.31.1.147'
iiwa=iiwaPy(ip)
pos = LifoQueue()
t1 = Thread(target = poll_pos, args = (pos,))
t1.daemon = True
t1.start()
total_pos = []
while True:
    user = input("S to Save, C to close \n")
    if user == "S" or user == "s":
        total_pos.append(pos.get())
    if user == "C" or user == "c":
        break

print("Connection closed")
iiwa.close()
print("Position saved: {}".format(total_pos))
