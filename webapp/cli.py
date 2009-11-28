
import os
import sys
import termios
from time import time

import settings

from remotecontrol import RemoteControl


def main():
    print 'Starting cli interface. Connecting to serial server.'
    remote = RemoteControl(settings.SERIAL_HOST, settings.SERIAL_TCP_PORT)

    print 'Waiting for commads. Use the numpad on your keyboard.'
    last_command_time = 0
    while True:
        try:
            ch = getchar()
            if time() - last_command_time > 0.3:
                last_command_time = time()
                handle_command(remote, ch)
        except KeyboardInterrupt:
            break
    remote.close()

def handle_command(remote, ch):
    keys = {
        '9': remote.right_forward,
        '8': remote.forward,
        '7': remote.left_forward,
        '6': remote.rotate_right,
        '4': remote.rotate_left,
        '3': remote.right_backward,
        '2': remote.backward,
        '1': remote.left_backward
    }
    if ch in keys:
        keys[ch]()

def getchar():
    """ Works like C getchar()

    http://snippets.dzone.com/posts/show/3084 
    """
    fd = sys.stdin.fileno()
    if os.isatty(fd):
        old, new = termios.tcgetattr(fd), termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        new[6][termios.VMIN] = 1
        new[6][termios.VTIME] = 0
        try:
            termios.tcsetattr(fd, termios.TCSANOW, new)
            termios.tcsendbreak(fd,0)
            ch = os.read(fd, 7)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    else:
        ch = os.read(fd, 7)
    return ch

if __name__ == '__main__':
    sys.exit(main())

