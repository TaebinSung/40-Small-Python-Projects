import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.ca", 443))
print("Inner IP: ", in_addr.getsockname()[0])

