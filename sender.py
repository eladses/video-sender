import socket
import struct
import cv2

HOST = "192.168.68.84"  # Server address
PORT = 5006             # Server port

OP_FRAME=0x06
OP_WAIT=0x07

OP_CONTINUE=0x08
OP_END=0x09

OP_ERROR=0x00

class CommunicationManager:
    def __init__(self):
        self.ip = HOST
        self.port = PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1) 
        self.conn, addr = self.sock.accept()
        print(f"connect to {addr}")


    def __del__(self):
        self.sock.close()

    def listen(self):
        msg_op=b''
        while len(msg_op)==0:
            msg_op = self.conn.recv(2)
        msg_op = int.from_bytes(msg_op, byteorder='big', signed=False)
        if msg_op==OP_CONTINUE:
            return 1
        elif msg_op==OP_END:
            return 0


    def send_op(self, op):
        self.conn.sendall(struct.pack("!H", op))

    def send_frmae(self,frame):
        self.send_op(OP_FRAME)

        _, byte_array = cv2.imencode('.jpg', frame)

        self.conn.sendall(struct.pack("!I", len(byte_array)))

        self.conn.sendall(byte_array)
        return 1

    def send_end_connection(self):
        self.send_op(OP_END)



if __name__=="__main__":
    message = "Hello, UDP Server!"
    cm = CommunicationManager()
    cm.send_data(message)
