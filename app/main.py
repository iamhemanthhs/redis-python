import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379))
    print("Server is listening on port 6379...")
    server_socket.accept()  # Wait for client
    
    connection, _ = server_socket.accept()
    print(connection, _)
    connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
