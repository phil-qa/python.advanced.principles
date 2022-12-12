#!/usr/local/bin/python3
# ReadSharePrices.py solution
# CBD 1st Feb.2011
# Python 3
import os.path
import sys
import getopt
from socket import *

if __name__ == '__main__':

    nPortID = 600;                # Hardcoded
    ServiceName = "garcon"

    # Create a connection based socket to receive share prices
    sock = socket(AF_INET, SOCK_STREAM, 0)

    # Bind socket to local address
    sock.bind(("", nPortID) )

    # Set maximum number of pending requests for connection
    sock.listen(5)
    print("\nWaiting for connection by share price program...")

    # Wait for share price program to connect to socket
    newsock, addr = sock.accept()
        
    # Original socket is no longer required as newsock
    # is connected
    sock.close()

    print("\n\nConnection received waiting for data...\n")
    
    while True:
        # Wait for data from share price program
        bMessage = newsock.recv(1024, 0)
        print("Recieved: " + bMessage.decode())

    # Close connected socket
    newsock.close();




