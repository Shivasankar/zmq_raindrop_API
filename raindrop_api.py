import zmq
import sys
import json
import socket
import time


def publisher(channel, value):
    ##publish
    cont = zmq.Context()
    sock = cont.socket(zmq.PUB)
    sock.bind("tcp://*:8888")
    while True:
        #print 'inside while'
        sock.send("%s:%s" % (channel, value))
        print ("%s:%s" % (channel, value))
        time.sleep(1)
        #break
    return


def subscriber(channel, callback):
    print channel, callback
    context1 = zmq.Context()
    sock1 = context1.socket(zmq.SUB)
    sock1.connect("tcp://localhost:8888")
    sock1.setsockopt(zmq.SUBSCRIBE, channel)
    print 'inside subscribe'
    poll_obj = zmq.Poller
    poll_obj.register(sock1, zmq.POLLIN)
    cont = True
    while cont:
        socks = dict(poll_obj.poll())
        #for update in channel:
        #print 'inside for'
        if sock1 in socks and socks[sock1] == zmq.POLLIN:
            msg1 = sock1.recv()
            print msg1
            #print json.dumps(msg1)
            callback(msg1)
    return