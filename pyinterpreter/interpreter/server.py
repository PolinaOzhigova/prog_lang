from .interpreter import Interpreter 
import zmq 
import json 
import threading 
import time 
 
def server(host, port): 
    print(f"Start server at {host}:{port}") 
    context = zmq.Context() 
    socket = context.socket(zmq.REP) 
    socket.bind(f"tcp://{host}:{port}") 
 
    while True: 
        try: 
            message = socket.recv(zmq.NOBLOCK).decode()
            print(f"Recieved message {message}") 
            try:
                result = Interpreter().eval(message) 
            except AttributeError as e: 
                result = {"error": str(e)} 
            js = json.dumps(result).encode() 
            socket.send(js) 
        except zmq.Again: 
            time.sleep(0.05)