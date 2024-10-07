// C++ program to show the example of server application in
// socket programming
#include <cstring>
#include <iostream>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

#define CATCHESS_PORT 8888
#define BUF_SIZE 1024
#define QUEUE 2

using namespace std;

int main()
{
    // creating socket with TCP SOCK_STREAM
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);

    // specifying the address
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(CATCHESS_PORT);
    serverAddress.sin_addr.s_addr = INADDR_ANY;

    // binding socket.
    bind(serverSocket, (struct sockaddr*)&serverAddress,
         sizeof(serverAddress));

    // listening to the assigned socket
    listen(serverSocket, QUEUE);

    while (true){
        // accepting connection request
        int clientSocket
                = accept(serverSocket, nullptr, nullptr);
        char buffer[1024] = { 0 };
        // recieving data
        recv(clientSocket, buffer, sizeof(buffer), 0);
        if(buffer){
            cout << "Message from client: " << buffer
                 << endl;
        }
    }

    // closing the socket.
    close(serverSocket);

    return 0;
}