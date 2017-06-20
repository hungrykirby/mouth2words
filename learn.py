import argparse
import math

import re
import threading
import sys

from pythonosc import dispatcher
from pythonosc import osc_server

import config
import arrange_nums as an

config.mode = input("mode > ")
config.is_new = input("is_new > ")

def keys():
    while True:
        console_input = input()
        if console_input == "s":
            config.is_input_word = True
        elif console_input == "e":
            config.is_input_word = False
            config.finish_input_word = True
        elif console_input == "o":
            config.is_calibration = True
        elif console_input != config.c:
            config.c = console_input
            print("c =", config.c)
        else:
            print("else")

def osc_loop():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="localhost", help="The ip to listen on")
    parser.add_argument("--port", type=int, default=8082, help="The port to listen on")
    args = parser.parse_args()

    learner = an.Arrange()
    learner.make_dir_train_or_test()

    _dispatcher = dispatcher.Dispatcher()
    #_dispatcher.map("/found", osc.set_found)
    _dispatcher.map("/raw", learner.fetch_numbers)

    server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), _dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()



dual_loop = threading.Thread(target=osc_loop,name="dual_loop",args=())
dual_loop.setDaemon(True)
dual_loop.start()

if __name__ == "__main__":
    keys()
