
import socket

class RemoteControl(object):
    
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def forward(self):
        self.sock.send('43')

    def backward(self):
        self.sock.send('65')

    def rotate_left(self):
        self.sock.send('63')

    def rotate_right(self):
        self.sock.send('45')

    def left_forward(self):
        self.sock.send('3')
    
    def left_backward(self):
        self.sock.send('5')

    def right_forward(self):
        self.sock.send('4')

    def right_backward(self):
        self.sock.send('6')

    def close(self):
        self.sock.close()

