#!/usr/local/bin/python3
# Advertise.py solution
# Python 3
# CBD 1st Feb.2011
import os.path
import sys
import getopt
from socket import *

def usage(ProgName):
  print("usage: %s -port <port no.> -host<hostname> -service <service>\n"%(ProgName),
         file=sys.stderr)
  os.exit( 0 )

#
# Parse command line arguments to find host name, service
# and port number
#
def ParseCmdLine():

    # Parse command line to find service or port to use
    # to receive requests for share prices
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:s:h:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage(sys.argv[0])
        sys.exit(2)
            
    nPortID = 602
    ServiceName = "busboy"
    HostName = 'INSTRUCTOR'
    
    # garcon is port 600
 
    for opt, arg in opts:
        if opt == "-p":
            nPortID = int(arg)
        elif opt in ("-h"):
            HostName = arg
        elif opt in ("-s"):
            ServiceName = arg
        else:
            assert False, "unhandled option"

    return (HostName, ServiceName, nPortID)

######################################################################

if __name__ == '__main__':

    nNumBytes = 0

    # Read command line arguments to find host address, service
    # and/or port number
    HostName, ServiceName, nPortID = ParseCmdLine()
    
    # Create a connectionless socket to send request
    # to share price server
    sock = socket( AF_INET, SOCK_DGRAM, 0)

    # Find local address information
    # Use local address information to build IP address string
    szRequest = gethostbyname(gethostname())

    # Fill out share price program's address information
    addr = (HostName, nPortID)

    print("\nSending request: '%s' to '%s' Port: %d" %
           (szRequest,  HostName, nPortID))
    
    # Send local IP string as request to share price program
    nNumBytes = sock.sendto(szRequest.encode(), 0, addr)
 
    print( "\n\nWaiting for response...")

    # Wait for response from share price program
    (data,addr) = sock.recvfrom(4096)

    print("Received:", data, addr)
    sock.close()





