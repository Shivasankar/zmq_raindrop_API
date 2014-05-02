import zmq


def broker():
    cxt = zmq.Context()
    frontend = cxt.socket(zmq.ROUTER)
    backend = cxt.socket(zmq.DEALER)
    frontend.bind("tcp://*:8888")
    backend.bind("tcp://*:8889")
    poll_obj = zmq.Poller()
    poll_obj.register(frontend, zmq.POLLIN)
    poll_obj.register(backend, zmq.POLLIN)
    while True:
        socks = dict(poll_obj.poll())
        if socks.get(frontend) == zmq.POLLIN:
            message = frontend.recv_multipart()
            backend.send_multipart(message)

broker()