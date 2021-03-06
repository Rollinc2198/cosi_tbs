import threading
import socket


class ServerConnection(threading.Thread):
    packet_size = 512

    def __init__(self, host_name, init, ip, port):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setDaemon(True)

        self.host_name = host_name
        self.init = init
        self.ip = ip
        self.port = port
        self.users = []
        self.connected = False
        self.fail = False

    def run(self):
        try:
            self.socket.connect((self.ip, self.port))
            self.socket.send((self.init + self.host_name).encode('utf-8'))

            data = list(self.socket.recv(self.packet_size))
            self.socket.close()
            if data[0] == '\x01':
                self.connected = True
                string = ""
                for c in range(1, len(data)):
                    string += c
                for c in range(0, len(string)):
                    temp = ""
                    while not c == '\t':
                        temp += c
                    self.users.append(temp)
            print(self.users)
        except Exception:
            self.fail = True
