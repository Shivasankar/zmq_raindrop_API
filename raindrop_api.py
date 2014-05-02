import zmq
import socket
import time
from threading import *


def publisher(channel, value):
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.bind("tcp://*:8888")
    time.sleep(1)
    print (channel, value)
    sock.send_multipart((channel, value))

def subscriber(channel, callback):
    try:
        print "New Thread Created"
        Thread(target=subscriber_thread, args=(channel, callback)).start()
    except Exception, ertxt:
        print ertxt


def subscriber_thread(channel, callback):
    ctx = zmq.Context()
    sock = ctx.socket(zmq.SUB)
    sock.connect("tcp://127.0.0.1:8889")
    sock.setsockopt(zmq.SUBSCRIBE, channel)
    poll_obj = zmq.Poller()
    poll_obj.register(sock, zmq.POLLIN)
    while True:
        socks = dict(poll_obj.poll())
        if sock in socks and socks[sock] == zmq.POLLIN:
            channel, msg1 = sock.recv_multipart()
            print msg1
    callback(msg1)