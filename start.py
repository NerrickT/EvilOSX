#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Starts the server using the MVC pattern."""
__author__ = "Marten4n6"
__license__ = "GPLv3"

from os import path, mkdir

from server.controller import Controller
from server.model import Model
from server.modules.helper import DATA_DIRECTORY
from server.version import VERSION
from server.view import View

BANNER = """\
▓█████ ██▒   █▓ ██▓ ██▓     ▒█████    ██████ ▒██   ██▒
▓█   ▀▓██░   █▒▓██▒▓██▒    ▒██▒  ██▒▒██    ▒ ▒▒ █ █ ▒░
▒███   ▓██  █▒░▒██▒▒██░    ▒██░  ██▒░ ▓██▄   ░░  █   ░
▒▓█  ▄  ▒██ █░░░██░▒██░    ▒██   ██░  ▒   ██▒ ░ █ █ ▒ 
░▒████▒  ▒▀█░  ░██░░██████▒░ ████▓▒░▒██████▒▒▒██▒ ▒██▒  @{} (v{})
░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░▒▒ ░ ░▓ ░
 ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░░░   ░▒ ░
   ░       ░░   ▒ ░  ░ ░   ░ ░ ░ ▒  ░  ░  ░   ░    ░  
   ░  ░     ░   ░      ░  ░    ░ ░        ░   ░    ░  
""".format(__author__, VERSION)

MESSAGE_INPUT = "[\033[1m?\033[0m] "
MESSAGE_INFO = "[\033[94mI\033[0m] "
MESSAGE_ATTENTION = "[\033[91m!\033[0m] "


def setup():
    """Creates the required directories used by the server."""
    directories = [
        DATA_DIRECTORY,
        path.join(DATA_DIRECTORY, "builds"),
        path.join(DATA_DIRECTORY, "output")
    ]

    for directory in directories:
        if not path.exists(directory):
            mkdir(directory)


def main():
    print(BANNER)
    setup()

    while True:
        try:
            server_port = int(input(MESSAGE_INPUT + "Server port to listen on: "))
            break
        except ValueError:
            continue

    model = Model()
    view = View()
    Controller(view, model, server_port)

    # Start the view, blocks until exit.
    view.start()

    print(MESSAGE_INFO + "Feel free to submit any issues or feature requests on GitHub.")
    print(MESSAGE_INFO + "Goodbye!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + MESSAGE_ATTENTION + "Interrupted.")
