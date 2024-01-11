#!/usr/bin/env python3

"""
This script is used by various workloads to notify DSI that a phase within a workload ended.
The messages from this script are parsed by DSI's PortForwardedEventQueue in events.py.
If profiling is enabled, this will trigger DSI to stop any profilers that are currently running.
"""

import socket
from argparse import ArgumentParser
import json

parser = ArgumentParser()
parser.add_argument("phase_name", type=str, help="Name of the phase that ended")
parser.add_argument("-i", "--ip", type=str, default="0.0.0.0", help="Target ip for the notification")
parser.add_argument("-p", "--port", type=int, default=4400, help="Target port for the notification")
args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((args.ip, args.port))
    message = {"message": "Ending phase"}
    message["phase"] = args.phase_name
    s.send((json.dumps(message) + "\n").encode())
