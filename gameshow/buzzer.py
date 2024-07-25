from flask import request
from flask_socketio import SocketIO, emit
import logging
from model import Model


logger = logging.getLogger(__name__)


def initialize_buzzers(socket: SocketIO, model: Model):
    logger.info("Initializing buzzers")

    @socket.on("buzzer")
    def buzzer():
        logger.info(f"{request.sid} buzzered")
        model.set_buzzer(request.sid, True)

        # Notify other users, that this user buzzered
        emit("buzzers", model.get_broadcast_data("buzzer_active"), broadcast=True)

    @socket.on("clearBuzzers")
    def clear_buzzers():
        logger.info(f"Clearing buzzers")
        model.set_buzzer(request.sid, False)

        # Notify all Clients
        emit("buzzers", model.get_broadcast_data('buzzer_active'), broadcast=True)
