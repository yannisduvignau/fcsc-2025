from pwn import *

# Define the remote connexion details: server address and port
HOST = args.HOST or "chall.fcsc.fr"
PORT = args.PORT or 2109

# Connect to the remote server
# The variable "io" will be used to send and receive text to the remove server
io = remote(HOST, PORT)

