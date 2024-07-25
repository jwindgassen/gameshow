from flask import request
from flask_socketio import emit
import logging


logger = logging.getLogger(__name__)


def initialize_buzzers(app):
    logger.info("Initializing buzzers")

    @app.socket.on("buzzer")
    def buzzer():
        logger.info(f"{request.sid} buzzered")
        app.model.set_buzzer(request.sid, True)

        # Notify other users, that this user buzzered
        emit("buzzers", app.model.get_broadcast_data("buzzer_active"), broadcast=True)

    @app.socket.on("clearBuzzers")
    def clear_buzzers():
        logger.info(f"Clearing buzzers")
        app.model.set_buzzer(request.sid, False)

        # Notify all Clients
        emit("buzzers", app.model.get_broadcast_data('buzzer_active'), broadcast=True)
