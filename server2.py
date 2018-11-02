#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from PIL import Image
import base64
from sys import argv
import gc, sys
import os
import resource
import cv2
from cStringIO import StringIO
import time

class ScreenSharingServer(BaseHTTPRequestHandler):
    def write_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self.write_headers()
        self.wfile.write(capture_image());

def capture_image():
    os.system("screencapture screen.jpeg")
    with open("/Users/i346794/Desktop/Server/screen.jpeg", "rb") as f:
       data = f.read()
       return data.encode("base64")
        
def serverLoop(server_class=HTTPServer, handler_class=ScreenSharingServer):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

##############
# Start Server
##############
serverLoop()