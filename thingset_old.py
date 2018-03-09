import socket
import sys
import struct
import argparse
from cbor2 import CBORTag, loads

class CANsocket(object):
    def __init__(self, interface):
        self.s = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.s.bind((interface,))

    def receive(self):
        pkg = self.s.recv(64)
        can_funcid = pkg[8]
        can_status = pkg[9]
        can_id, length, data = struct.unpack('<IB3x8s', pkg)
        can_id &= socket.CAN_EFF_MASK
        return(can_id, can_funcid, can_status, data[:length])


def listen(args):
    try:
        sock = CANsocket(args.interface)
    except OSError as e:
        sys.stderr.write("Could not bind to given interface {}\n'".format(args.interface))
        sys.exit(e.errno)

    print("Start listening on {}..\n".format(args.interface))
    while True:
        can_id, func_id, status, data = sock.receive()
        if status >= 0x80:
            print("Error receiving package from ID {}. Error code: {}".format(can_id, hex(status)))
            continue
        cbor_pkg = loads(data[2:])
        print("Message from ID {} -> 0: {}".format(can_id, cbor_pkg))

def parse_if():
    parser = argparse.ArgumentParser(description="Listen on CAN interface for messages and decode CBOR to ASCII")
    parser.add_argument('interface', type=str, help='interface (eg. vcan0)')
    parser.set_defaults(func=listen)
    return parser.parse_args()

def main():
    args = parse_if()
    args.func(args)

if __name__ == '__main__':
    main()
