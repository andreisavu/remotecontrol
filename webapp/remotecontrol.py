
import socket

class RemoteControl(object):
    
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def key_command(self, ch):
        " Default command handler "
        keys = {
            '9': self.right_forward,
            '8': self.forward,
            '7': self.left_forward,
            '6': self.rotate_right,
            '4': self.rotate_left,
            '3': self.right_backward,
            '2': self.backward,
            '1': self.left_backward
        }
        if ch in keys:
            keys[ch]()

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

