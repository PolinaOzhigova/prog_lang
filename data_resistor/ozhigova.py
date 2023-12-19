import zmq
import logging
import csv
import datetime
import time

values = ['p', 'm', 't']
time_out = 900

logging.basicConfig(filename='ozhigova.log', level=logging.CRITICAL)
logger = logging.getLogger()
def write_log(message):
    logging.critical(f"{datetime.datetime.utcnow()} : {message}")
write_log("Start program")

def file_write(current_time, tag, value):
    with open('ozhigova.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([tag, value, current_time])

def connect():

    context = zmq.Context()
    client = context.socket(zmq.SUB)
    try:
        client.connect("tcp://192.168.0.102:5555")
        client.subscribe('')
    except:
        write_log(f"Unable to connect to server")
        connect()

    poller = zmq.Poller()
    poller.register(client, zmq.POLLIN)

    try:
        while True:

            socket = dict(poller.poll(timeout=time_out))

            if client in socket and socket[client] == zmq.POLLIN:

                message = client.recv_string()
                current_time = datetime.datetime.utcnow()

                if len(message):

                    if len(message) == 1 and message not in values:
                        write_log(f"Not in correct values(p, m, t): {message}")

                    elif len(message) == 1:
                        file_write(current_time, message, 'True')

                    else:
                        message_list = message.split(' ')

                        if message_list[0] not in values:
                            write_log(f"Not in correct values(p, m, t): {message_list[0]}")

                        else:
                            file_write(current_time, message_list[0], message_list[1])

                else:
                    write_log(f"Message is 0")

                time.sleep(1)

            else:
                write_log(f"Connection was lost. Retrying in 1 seconds.")
                time.sleep(1)
                connect()

    except KeyboardInterrupt:
        write_log(f"Keyboard interrupt or computer was turned off. End of program.")

connect()