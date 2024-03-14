##sockets in Python

import socket ##socket library import
examplesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## opens the socket under the subclass of stream and assigns it 'examplesocket'
examplesocket.connect(('data.pr4e.org ',80)) ### Tells the examplesocket to connect to the host 'data.pr4e.org', where 80 is the port (HTML)

