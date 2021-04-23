#!/usr/bin/python3

import os
import signal

try:
    # Open the file 
    file = open("process_ID.txt", "r")
    # Store the pid of the pystemon process
    pid = file.read()
    # Kill the process 
    os.kill(int(pid), signal.SIGKILL)
    # Remove the file 
    os.remove("process_ID.txt")
    # Close the file
    file.close()
except IOError:
    print("File not exist!")
