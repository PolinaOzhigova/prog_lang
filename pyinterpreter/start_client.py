import zmq
import json
import time

def eval(sock, expr):
    sock.send(expr.encode())
    return json.loads(sock.recv().decode())

host = "127.0.0.1"
port = 5555

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{host}:{port}")
print(eval(socket, "2+(2*2)"))
print(eval(socket, "2+2*2"))