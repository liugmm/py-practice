import socket
import threading


def start_tcpserver_short(host='127.0.0.1', port=65432):
    """TCP短连接socket"""

    # 创建TCP/IP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 绑定套接字到指定host，port
        server_socket.bind((host, port))
        # 监听传入的连接
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        # 接受客户端连接
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # 接受客户端发送的数据
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received from client: {data.decode()}")
                # 发送响应数据
                # resp = "return" + data.decode()
                conn.sendall(data)


def start_udpserver(host='127.0.0.1', port=65432):
    """UDP连接
    使用UDP协议，可以将 socket.SOCK_STREAM 替换为 socket.SOCK_DGRAM，并去掉 listen() 和 accept() 方法。

    Args:
        host (str, optional): _description_. Defaults to '127.0.0.1'.
        port (int, optional): _description_. Defaults to 65432.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP Server listening on {host}:{port}")

        while True:
            print("Waiting for data...")
            data, addr = server_socket.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")

            server_socket.sendto(data, addr)


def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            # 接受客户端发送的数据
            data = conn.recv(1024)
            if not data:
                print(f"Client {addr} disconnected.")
                break
            # 心跳机制
            if data.decode() == "HEARTBEAT":
                print(f"Heartbeat received from {addr}")
                conn.sendall(b'HEARTBEAT_ACK')
            else:
                print(f"Received from client: {data.decode()}")
                # 发送响应数据
                conn.sendall(data)
        except ConnectionResetError:
            print(f"Client {addr} forcibly closed the connection.")
            break
    conn.close()


def start_tcpserver_long(host='127.0.0.1', port=65432):
    """TCP长连接，多个客户端连接，多线程，心跳机制
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_client, args=(conn, addr))
            client_thread.start()
            print(f"Active connection: {threading.active_count() - 1}")


if __name__ == "__main__":
    # start_tcpserver_short()
    # start_udpserver()
    start_tcpserver_long()
