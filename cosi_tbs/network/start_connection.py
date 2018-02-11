from cosi_tbs.network import *


def start_connection(host_name, init):
    thread = ServerConnection(host_name, init, "192.168.0.31", 6666)
    thread.start()
    return thread