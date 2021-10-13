import logging
from websocket_server import WebsocketServer

server = WebsocketServer(8080, host='127.0.0.1', loglevel=logging.INFO)
server.run_forever()