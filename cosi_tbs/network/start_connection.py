import _thread
from cosi_tbs.network import server_connection


def start_connection():
    try:
        _thread.start_new_thread(server_connection)
    except:
        print("Error: unable to start thread")