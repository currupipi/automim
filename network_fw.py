#! /usr/bin/env python

'''Networking framework'''

import os, sys, subprocess


def get_my_ip():
    import socket
    output = socket.gethostbyname(socket.gethostname())
    return output

