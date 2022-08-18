import threading
import socket
import re
import signal
import sys
import time

class Server():
    def __init__(self,port):
        self.listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.listener.bind(('',port))
        self.listener.listen(1)
        print("Listening on port {0}".format(port))
        self.client_sockets =[]
        signal.signal(signal.SIGINT,self.signal_handler)
        signal.signal(signal.SIGTERM,self.signal_handler)


   def run(self):
       while True:
           print("Listening for more clients")
           try:
               (client_socket,client_address) = self.listener.accept()
           except socket.error:
               sys.exit("Could not accept any more connections")
           self.client_sockets.append(client_socket)
           print("Starting client thread for {0}".format(client_address))
           client_thread = ClientListener(self,client_socket,client_address)
           client_thread.start()
           time.sleep(1)

   def echo(self,data):
       print("echoing: {0}".format(data))
       for socket in self.client_sockets:
           try:
               socket.sendall(data)
           except socket.error:
               print("Unable to send message")
