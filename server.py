import logging
from websocket_server import WebsocketServer

def message_received(client, server, message):
	server.send_message_to_all(message)

server = WebsocketServer(8080, host='127.0.0.1', loglevel=logging.INFO)
server.set_fn_message_received(message_received)
server.run_forever()