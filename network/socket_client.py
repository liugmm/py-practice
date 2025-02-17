import socket
import time
import threading
import queue
import asyncio


def start_tcpclient_short(host="127.0.0.1", port=65432):
    """TCP短连接socket"""
    # 创建一个TCP/IP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 连接服务器
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # 发送数据到服务器
        message = "Hello, Socket!"
        client_socket.sendall(message.encode())
        print(f"Send to server: {message}")

        # 接受服务器的返回
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")


def start_udpclient(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = "Hello, UDP Server!"
        print(f"Send to server: {message}")
        client_socket.sendto(message.encode(), (host, port))

        data, addr = client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")


def send_heartbeat(client_socket: socket.socket):
    while True:
        try:
            client_socket.sendall(b'HEARTBEAT')
            threading.Event().wait(5)
        except ConnectionResetError:
            print("Server closed the connection.")
            break


def receive_messages(client_socket: socket.socket, message_queue: queue.Queue):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print("Server closed the connection.")
                break

            if data == "HEARTBEAT_ACK":
                # print("Received HEARTBEAT_ACK from server.")
                ...
            else:
                # 将普通消息放入队列
                message_queue.put(data)
                print(f"Received message from server: {data}")

        except ConnectionResetError:
            print("Server forcibly closed the connection.")
            break


def start_tcpclient_long(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # 创建消息队列
        message_queue = queue.Queue()

        # 启动心跳线程
        heartbeat_thread = threading.Thread(
            target=send_heartbeat, args=(client_socket, ))
        heartbeat_thread.daemon = True
        heartbeat_thread.start()

        # 启动消息接受线程
        received_thread = threading.Thread(
            target=receive_messages, args=(client_socket, message_queue))
        received_thread.daemon = True
        received_thread.start()

        while True:
            try:
                # 检查消息队列是否有消息
                if not message_queue.empty():
                    message = message_queue.get()
                    # print(f"Received message from server: {message}")

                # 从用户获取输入信息
                message = input("Enter message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("Closeing connection...")
                    break
                # 发送消息到服务器
                client_socket.sendall(message.encode())

                # 给线程执行时间，将接受的消息推送到队列
                # time.sleep(0.1)

            except ConnectionResetError:
                print("Server forcibly closed the connection.")
            except KeyboardInterrupt:
                print("\nClient is shutting down")
                break


if __name__ == "__main__":
    # start_tcpclient_short()
    # start_udpclient()
    start_tcpclient_long()
