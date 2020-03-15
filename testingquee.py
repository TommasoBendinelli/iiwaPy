# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:03:26 2018

@author: Mohammad SAFEEA

Test script of iiwaPy class.

"""
import time
from threading import Thread
from queue import LifoQueue

def poll_pos(pos):
    counter = 0
    # read some data from the robot
    while True:
        try:
            counter = counter + 1
            print("All good")
            #print(keep_polling.get())
            print("All good")
            pos.put(counter)
            time.sleep(1)
            
        except:
            print('an error happened')
            return
    print("Connection closed")
    print(keep_polling.get())
    return


if __name__ == "__main__":
    pos = LifoQueue()
    t1 = Thread(target = poll_pos, args = (pos,))
    t1.daemon = True
    t1.start()

    total_pos = []
    while True:
        user = input("S to Save, C to close")
        if user == "S" or user == "s":
            total_pos.append(pos.get())
        if user == "C" or user == "c":
            break

    print("Position saved: {}".format(total_pos))
