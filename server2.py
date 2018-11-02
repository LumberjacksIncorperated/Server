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

def capture_image():
    os.system("screencapture screen.jpeg")
    #screenShot = Image.open(r"/Users/i346794/Desktop/Server/screen.jpeg")
    #screenShot = screenShot.convert("RGB")
    #maxsize = (1500, 1500)
    #im_t = screenShot.thumbnail(maxsize, Image.ANTIALIAS)
    #width, height = screenShot.size
    #print("width = %d height - %d" % (width, height))
    #screenShot.save("image.jpeg", 'JPEG')
    with open("/Users/i346794/Desktop/Server/screen.jpeg", "rb") as f:
       data = f.read()
       return data.encode("base64")

class ScreenSharingServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(capture_image());

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=ScreenSharingServer, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()