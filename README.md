# python-websocketbridge

A simple bridge program which forwards data between a server socket and client websockets.

This is a little bit like an echo server.


Usage:

```
python -m websocketbridge 5050 5051
```

or in a script:

```
import websocketbridge

websocketbridge.runserver(socket_port=5050, websocket_port=5051)
```


