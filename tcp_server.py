import socket
import sys
import do_localization_fingerprinting
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 50007)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(4096)
            print('received "%s"' % data)

            cells = []
            raw = json.loads(data)
            for d in raw:
                cells.append({"bssid":d['ssid'], "signal level": d['rssi'] })

            pos_x, pos_y = do_localization_fingerprinting.localize(cells)
            print('Position: ', pos_x, pos_y)
            break
    finally:
        connection.close()