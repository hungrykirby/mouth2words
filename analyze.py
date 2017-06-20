import argparse
import math

import re
import threading
import sys

from pythonosc import dispatcher
from pythonosc import osc_server

import config

import NeighborAlgorithm as na

config.learner = input("learner > ")
config.stream = input("is stream > ")
config.ver = input("version > ")

def keys():
    while True:
        input_word = input()
        if input_word == "s":
            sys.exit()
        elif input_word == "o":
            config.is_calibration = True
        elif config.c != input_word:
            config.c = input_word
            print("c =", config.c)
        else:
            print("else")

def osc_loop():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
      default="localhost", help="The ip to listen on")
    parser.add_argument("--port",
      type=int, default=8082, help="The port to listen on")
    args = parser.parse_args()

    #if config.learner == "na":
    if config.learner != "na":
        sys.exit()
        return None

    config.fitted_data = na.setup()

    _dispatcher = dispatcher.Dispatcher()
    _dispatcher.map("/raw", na.stream)

    server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), _dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()


if config.stream == "s":
    th = threading.Thread(target=osc_loop,name="th",args=())
    th.setDaemon(True)
    th.start()
elif config.stream == "t":
    for i in range(1,21):
        config.length_array = i
        na.setup()
else:
    config.length_array = 21
    na.setup()

if __name__ == "__main__":
    keys()
