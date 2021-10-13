import logging
from websocket_server import WebsocketServer

clients = []

def connected(client, server):
	print(client, 'connected')
	clients.append(client)
	
def handle_close(client, server):
	print(client, 'closed')
	clients.remove(client)

def message_received(client, server, message):
	print(message)
	server.send_message_to_all(message)

server = WebsocketServer(8080, host='localhost', loglevel=logging.INFO)
server.set_fn_message_received(message_received)
server.set_fn_new_client(connected)
server.set_fn_client_left(handle_close)

server.run_forever()