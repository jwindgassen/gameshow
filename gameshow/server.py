from flask import Flask, redirect
from flask_socketio import SocketIO
from .model import Model
from .buzzer import initialize_buzzers


class Server(Flask):
    _socket: SocketIO
    _model: Model

    def __init__(self, import_name, *args, **kwargs):
        super().__init__(import_name, *args, **kwargs)

        self._socket = SocketIO(self)
        self._model = Model()

        # Redirect "/" to "index.html"
        @self.route("/")
        def root():
            return redirect("index.html")

        # Initialize Buzzers
        initialize_buzzers(self)

    @property
    def socket(self):
        return self._socket

    @property
    def model(self):
        return self._model

    def start_server(self, *args, **kwargs):
        self._socket.run(self, *args, **kwargs)
