#/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    ExtPlane-hardware interface written in Python 3.
    Customize to fit your needs.

    Standard datarefs available at
    http://www.xsquawkbox.net/xpsdk/docs/DataRefs.txt
"""

import asyncio
import logging

def setup_logging():
    logger = logging.getLogger("")
    logger.handlers = []

    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s %(module)-10s:%(lineno)-3s %(levelname)-7s %(message)s',"%y%m%d-%H:%M:%S")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)


class ExtPlaneProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        logging.info("Connected to ExtPlane")

    def data_received(self, data):
        logging.info("Data received from ExtPlane")

    def connection_lost(self, exc):
        logging.info("Disconnected from ExtPlane")
        self.loop.stop(

    def sub(self, dataref, accuracy=None):
        if not isinstance(dataref, str) or len(dataref) == 0:
            return False
        return self.write("sub {}{}".format(dataref, 
                          " {}".format(accuarcy) if accuracy else "")    
       

    def unsub(self, dataref):
        if not isinstance(dataref, str) or len(dataref) == 0:
            return False
        return self.write("unsub {}".format(dataref)

    def set(self, dataref, value):
        if isinstance(value, str):
            value = value.replace(" ", "")
            
        elif isinstance(value, int) or isinstance(value, float):
            value = str(value)
                 
        elif isinstance(value, list):
            value = str(value).replace(" ", "")
        
        else:
            return False

        if not isinstance(dataref, str) or len(dataref) == 0 or\
               len(value) == 0:
            return False
        
        self.write("set {} {}".format(dataref, value)
    

    def write(self, text): 
        self.transport.write(text.encode())

loop = asyncio.get_event_loop()
message = 'Hello World!'
coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                              '127.0.0.1', 50000)
loop.run_until_complete(coro)
loop.run_forever()
loop.close(
