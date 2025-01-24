import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 6379))
    print("Server is listening on port 6379...")
    
    while True:
        # Accept a new connection
        connection, address = server_socket.accept()
        
        print("Connection established with:", address)
        connection_should_be_closed = True
        try:
            while True:
                # You can handle communication with the client here
                data = connection.recv(1000000)
                if not data:
                    # If there's no data, the client has closed the connection
                    break
                decoded_data = data.decode('utf-8')  # Decoding the bytes into a string
                decoded_data = decoded_data.strip()
                
                print("Received data:", decoded_data)
                
                if decoded_data == "exit":
                    connection.close()
                    connection_should_be_closed = False
                    print("Connection closed.")
                    break
                
                # Send a response back to the client
                connection.sendall(b"+PONG\r\n")
                
        except Exception as e:
            print(f"Error during communication: {e}")
        
        finally:
            # Close the connection after each client interaction
            if connection_should_be_closed:
                connection.close()
                print("Connection closed.")
        print("COMPLETLY DONE WITH THE EXECUTION")
        break

if __name__ == "__main__":
    main()
