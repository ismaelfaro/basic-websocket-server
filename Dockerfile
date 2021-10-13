FROM python

RUN pip install websocket-server
COPY server.py server.py 
CMD python server.py