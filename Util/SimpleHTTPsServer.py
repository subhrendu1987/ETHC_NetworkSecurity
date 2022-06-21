# Execute as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import subprocess
from os.path import exists

#### Certificate file checking 
COMMAND_SSL=["openssl", "req", "-newkey", "rsa:2048", "-new", "-nodes", "-x509", "-days", "3650", "-keyout", "key.pem", "-out", "cert.pem"]
if(exists("./key.pem") and exists("./cert.pem")):
        print("Certfile exists")
else:
        print("Generating Certfile")
        p = subprocess.run(COMMAND_SSL)
        print("Certfile created")
######################################################################
httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='./cert.pem',keyfile='./key.pem')
httpd.socket = context.wrap_socket(sock=httpd.socket, server_side=True,
                                        do_handshake_on_connect=True,
                                        suppress_ragged_eofs=True,
                                        server_hostname=None,
                                        session=None)
print("Https Server running:  https://localhost:4443")
httpd.serve_forever()