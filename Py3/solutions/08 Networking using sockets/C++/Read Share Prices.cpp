#include <windows.h>
#include <winsock.h>

#include <stdio.h>
#include <process.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

#define NO_FLAGS_SET         0

#define SOCKET_OVERLAPPED

void usage( char *pszProgName )
{
  fprintf( stderr, "usage: %s -port <port no.> -service <service>\n", pszProgName );
  exit( 0 );
}


int DisplayLastError( LPSTR lpszFormat, ... )
{
  	int nError = WSAGetLastError();
  	char buf[1024];
  	va_list arg;

  	va_start( arg, lpszFormat );
  	wvsprintf( buf, lpszFormat, arg );
  	va_end( arg );                
  	printf( "%s because error %d\n", buf, nError );
  	return nError;
}

void vGetServerName( PSTR pszHostName, PSTR pszServiceName, int nPortID,
                     PSOCKADDR_IN psin )
{
	// Declare a pointer to a host entry structure
   	PHOSTENT phe;

	// Address family is going to be Internet
   	psin->sin_family = AF_INET;
	psin->sin_port=nPortID;
   	psin->sin_addr.s_addr = INADDR_ANY;

	// If we don't get passed a host name then use this computer
   	if ( pszHostName == NULL || pszHostName[0] == 0 )
   	{
		// Declare a buffer to store the computer name in
     	char  szHostName[MAX_COMPUTERNAME_LENGTH+1];
		
		// Retrieve the name of this computer
     	gethostname( szHostName, sizeof(szHostName) );

		// Get a pointer to a HOSTENT structure 
     	phe = gethostbyname( szHostName );

     	if ( phe == NULL )
     	{
       		printf( "couldn't get host %s by name\n", szHostName );
     	}
   	}
   	else
   	{
		// If we were passed a host name then get the HOSTENT info
     	phe = gethostbyname ( pszHostName );

		// If the host name was in fact an IP address...
     	if ( phe == NULL )
     	{
			// Get the 32 bit address...
       		long addr = inet_addr ( pszHostName );

			// ... and use gethostbyaddr to get the HOSTENT info
       		phe = gethostbyaddr( (LPSTR)&addr, sizeof(addr), PF_INET );
     	}
   	}

	// If after all that we have a pointer to a HOSTENT then copy the 
	// addressing info into the SOCKADDR_IN we were passed
   	if ( phe )
     	memcpy( (LPSTR)&(psin->sin_addr), phe->h_addr, phe->h_length );
   	else
   	{
     	printf( "couldn't get host %s by address or name\n", pszHostName );
   	}

	// If we got passed a service name...
   	if ( pszServiceName && pszServiceName[0] )
   	{

		// Get a SERVENT info structure...
      	PSERVENT pse = getservbyname( pszServiceName, "tcp" );

		// ...and copy the port number into the SOCKADDR_IN
      	if ( pse )
        	psin->sin_port = pse->s_port;
      	else
      	{
        	printf( "couldn't get service %s by name\n", pszServiceName );
      	}
   	}
}

void main( int argc, char **argv )
{
	WSADATA wsaData;
	int  nPortID = 0;
	char szServiceName[80] = "garcon";
	SOCKET sock;

	
	// Initialize WinSock library and ask for version 1.1
	if ( WSAStartup( MAKEWORD(1,1), &wsaData ) )
	{
		DisplayLastError("WSAStartup failed.");
		return;
	}

	// Check that required sockets version was available
	if ( LOBYTE( wsaData.wVersion ) != 1 || HIBYTE( wsaData.wVersion ) != 1 )
	{
      	printf( "couldn't agree on socket lib version\n" );
		return;
	}	

	// Create a connection based socket to receive share prices
	sock = socket( AF_INET, SOCK_STREAM, 0);

    if ( sock != INVALID_SOCKET )
	{
		SOCKET newsock;
		char szMessage[100];
		SOCKADDR_IN local_sin;
		int  nNumBytes;
	
  		// Find local address information
		vGetServerName( NULL, szServiceName, nPortID, &local_sin );

		// Bind socket to local address
		if ( bind( sock, (SOCKADDR*)&local_sin,
			       sizeof(local_sin)) == SOCKET_ERROR )
		{
			DisplayLastError("bind() failed.");
			WSACleanup();
			return;
		}

		// Set maximum number of pending requests for connection
		listen( sock, 1);
		printf( "\nWaiting for connection by share price program...");

		// Wait for share price program to connect to socket
		newsock = accept( sock, NULL, NULL);
		if ( newsock == SOCKET_ERROR )
		{
			DisplayLastError("accept() failed.");
			WSACleanup();
			return;
		}
		
		// Original socket is no longer required as newsock
		// is connected
		closesocket(sock);

		printf( "\n\nConnection received waiting for data...\n");
		do
		{

#ifdef SOCKET_OVERLAPPED

			OVERLAPPED ovl = {0};
			DWORD      dwBytesRead = 0, dwWait;

			// Create manual reset event for overlapped I/O
			ovl.hEvent = CreateEvent( NULL, TRUE, FALSE, NULL);

			// Start overlapped I/O on socket
			if ( !ReadFile( (HANDLE)newsock, szMessage, sizeof(szMessage),
							&dwBytesRead, &ovl) &&
			      GetLastError() != ERROR_IO_PENDING )
			{
				DisplayLastError("ReadFile() failed.");
				WSACleanup();
				return;
			}

    
			dwWait = WAIT_TIMEOUT;
			while ( dwWait != WAIT_OBJECT_0 )
			{
				INPUT_RECORD InputRec;
				DWORD        dwNumEvents;
				HANDLE hWait[2];

				// Set up array of handles to wait on
				hWait[0] = ovl.hEvent;

				// Stdin handle is signalled when there is data
				// in the console input buffer
				hWait[1] = GetStdHandle( STD_INPUT_HANDLE );

				// Wait for data to arrive on socket on stdin
				dwWait = WaitForMultipleObjects( 
					        sizeof(hWait) / sizeof(hWait[0]), hWait,
							FALSE, INFINITE);

				switch(dwWait)
				{
					case WAIT_OBJECT_0:
						// If data received get results
						if ( GetOverlappedResult( (HANDLE)newsock, &ovl,
						    &dwBytesRead, FALSE))
							nNumBytes = dwBytesRead;
						else
						{
							DisplayLastError("ReadFile() failed.");
							WSACleanup();
							return;
						}
						break;

					case WAIT_OBJECT_0 + 1:	
						// Console input was received. Check that its
						// a keypress event
						ReadConsoleInput(GetStdHandle( STD_INPUT_HANDLE ),
							 &InputRec , 1, &dwNumEvents);
						if ( InputRec.EventType == KEY_EVENT )
						{
							printf("\n\nKey press received. Shutting down...");
							WSACleanup();
							return;
						}
						break;

					default:
						DisplayLastError("WaitForMultipleObjects() failed.");
						WSACleanup();
						return;
				}
			}
			// Close Event created for overlapped I/O
			CloseHandle( ovl.hEvent);
				      
#else
			// Wait for data from share price program
			nNumBytes = recv(newsock, szMessage, sizeof(szMessage), 0);
#endif

			if (nNumBytes != SOCKET_ERROR )
			{
				szMessage[nNumBytes]='\0';
				printf(szMessage);
			}
		}
		while (nNumBytes != SOCKET_ERROR);

		// Close connected socket
		closesocket(newsock);
	}
	else
		DisplayLastError("socket() failed.");

   	// Deregister applications usage of share price server
	WSACleanup();
}

