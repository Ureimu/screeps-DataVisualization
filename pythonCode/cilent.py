import socket
# 不能开防火墙！
HOST, PORT = "47.103.128.236", 3025
# HOST, PORT = "localhost", 3025
data = "emm"

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print(f"Sent:     {data}")
print(f"Received: {received}")
