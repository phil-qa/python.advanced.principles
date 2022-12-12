#include <windows.h>
#include <winsock.h>

#include <stdio.h>
#include <process.h>
#include <stdlib.h>
#include <string.h>

#define SOCKET_OVERLAPPED

#define NO_FLAGS_SET         0

void usage( char *pszProgName )
{
  fprintf( stderr, "usage: %s -port <port no.> -host<hostname> -service <service>\n", pszProgName );
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

//
// Fills out SOCKADDR_IN structure with server's address
//
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


//
// Parse command line arguments to find host name, service
// and port number 
//
void ParseCmdLine(int argc, char **argv, char *szHostName,
				  char *szServiceName, int *pnPortID)
{

	setbuf( stdin, NULL );
  	setbuf( stdout, NULL );
  	setbuf( stderr, NULL );

  	if ( argc > 1 )
  	{
    	int i = 1;

    	argc--;

    	while ( argc )
    	{
      		if ( strnicmp( "-p", argv[i], 2 ) == 0 )
      		{
        		*pnPortID = atoi( argv[i+1] );
        		i += 2;
        		argc -= 2;
      		}
      		else if ( strnicmp( "-h", argv[i], 2 ) == 0 )
      		{
		        strcpy( szHostName, argv[i+1]);
		        i += 2;
		        argc -= 2;
      		}
      		else if ( strnicmp( "-s", argv[i], 2 ) == 0 )
      		{
		        strcpy( szServiceName, argv[i+1]);
		        i += 2;
		        argc -= 2;
		    }
      		else
      		{
        		i++;
        		argc--;
      		}
    	}
  	}

}

void main( int argc, char **argv )
{
	WSADATA wsaData;
	int  nPortID = 0, nNumBytes = 0;
	char szHostName[80] = "";
	char szServiceName[80] = "busboy";
	SOCKADDR_IN dest_sin;
	SOCKET sock;

	// Read command line arguments to find host address, service
	// and/or port number
	ParseCmdLine( argc, argv, szHostName, szServiceName, &nPortID);

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

	// Create a connectionless socket to send request
	// to share price server
	sock = socket( AF_INET, SOCK_DGRAM, 0);

    if ( sock != INVALID_SOCKET )
	{
		char szRequest[100], szResponse[100];
		SOCKADDR_IN client_sin;
	
		// Find local address information
		vGetServerName( NULL, NULL, 0, &client_sin);

		// Use local address information to build IP
		// address string
		strcpy( szRequest, inet_ntoa(client_sin.sin_addr) );

   		// Fill out share price program's address information
		vGetServerName( szHostName, szServiceName, nPortID, &dest_sin );

		printf("\nSending request: '%s'", szRequest);
        
		// Use a broadcast if no host name supplied
		if ( !strlen(szHostName ) )
		{
			BOOL fBroadcast = TRUE;
			dest_sin.sin_addr.s_addr =  INADDR_BROADCAST;
			printf( "    (Using socket broadcast)");

			// Change the socket to allow broadcasts
			if ( setsockopt(sock, SOL_SOCKET, SO_BROADCAST, (char*)&fBroadcast,
			       sizeof(fBroadcast)) )
			{
				DisplayLastError("sendto() failed");
				WSACleanup();
				return;
			}

		}

		// Send local IP string as request to share price
		// program
		nNumBytes = sendto( sock, szRequest, strlen(szRequest)+1, 0,
			    (PSOCKADDR)&dest_sin, sizeof( dest_sin));
		if ( nNumBytes == SOCKET_ERROR )
		{
			DisplayLastError("sendto() failed");
			WSACleanup();
			return;
		}
		
		printf( "\n\nWaiting for response...");

		// Wait for response from share price program
		nNumBytes = recvfrom( sock, szResponse, sizeof(szResponse), 0, NULL, NULL);

		if ( nNumBytes != SOCKET_ERROR )
		{
			szResponse[ nNumBytes ] = '\0';
			printf("\nReceived Response: '%s'\n", szResponse);
		}
		else
			DisplayLastError("recvfrom() failed");
		closesocket(sock);
	}

   	// Deregister application's usage of WinSock
	WSACleanup();
}

