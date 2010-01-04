
import socket

class RemoteControl(object):
    
    def __init__(self, host='localhost', port=9000):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def key_command(self, ch):
        " Default command handler "
        keys = {
            'o': self.right_forward,
            'w': self.forward,
            'i': self.left_forward,
            'd': self.rotate_right,
            'a': self.rotate_left,
            'l': self.right_backward,
            's': self.backward,
            'k': self.left_backward,
            ' ': self.take,
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

    def take(self):
        self.sock.send('2')

    def body_left(self):
        self.sock.send('7')

    def body_right(self):
        self.sock.send('8')

    def close(self):
        self.sock.close()

