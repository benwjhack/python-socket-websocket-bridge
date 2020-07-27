import logging, threading

from simple_websocket_server import WebSocketServer, WebSocket
from simpleprotocol.socketwrapper import ClientSocket

SECRET = "super!!secure--"

SOCKET_PORT = 5050
WEBSOCKET_PORT = 5051

class Bridge(WebSocket):

	def handle(self):
		string = self.data
		logging.info(f"Received {self.data}")
		if not string.startswith(SECRET):
			logging.info("Data discarded, wrong secret!")
			return
		
		self.sock.sendLine(string.strip(SECRET))
	
	def connected(self):
		logging.info(f"Started connection with {self.address}")
		
		sock = ClientSocket('localhost', SOCKET_PORT)
		self.sock = sock
		
		def handle(sock):
			while True:
				m = sock.readLine()
				logging.info(f"Sending {m}")
				self.send_message(m)
		
		t = threading.Thread(target=handle, args=(sock,))
		t.daemon = True
		t.start()
	
	def handle_close(self):
		logging.info(f"Closed connection with {self.address}")
		pass

if __name__ == "__main__":

    import sys

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    args = sys.argv
    if len(args) != 3: # program name, socket port, websocket port
        raise Exception("Two arguments are required (socket port, websocket port)")
    try:
        SOCKET_PORT = int(args[1])
        WEBSOCKET_PORT = int(args[2])
    except ValueError:
        raise ValueError("The arguments must be valid integers")

    logging.info("Starting server...")

    server = WebSocketServer('', WEBSOCKET_PORT, Bridge)
    server.serve_forever()
