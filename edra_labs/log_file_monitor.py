import threading
import time
import socket


class Monitor:
    def __init__(self, log_file, update_interval=1):
        self.log_file = log_file
        self.update_interval = update_interval
        self.clients = []
        self.last_position = 0

    def start(self):
        threading.Thread(target=self.monitor_log).start()
        threading.Thread(target=self.handle_clients).start()

    def monitor_log(self):
        while True:
            try:
                with open(self.log_file, 'rb') as f:
                    f.seek(self.last_position)
                    data = f.read()
                    if data:
                        self.last_position += len(data)
                        lines = data.decode('utf-8').splitlines()
                        self.broadcast_lines(lines)
            except Exception as e:
                print(f"Error : {e}")
            time.sleep(self.update_interval)

    def broadcast_lines(self, lines):
        for client in self.clients:
            try:
                client.send(b'\n'.join(lines).encode('utf-8'))
            except Exception as e:
                print(f"Error in broadcasting: {e}")

    def handle_clients(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 8080))
        server_socket.listen()

        while True:
            client_socket, _ = server_socket.accept()
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
        finally:
            self.clients.remove(client_socket)
            client_socket.close()