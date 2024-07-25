from pydantic import BaseModel, ConfigDict, alias_generators
from typing import Literal, Any
import logging


logger = logging.getLogger(__name__)


class User(BaseModel):
    model_config = ConfigDict(alias_generator=alias_generators.to_camel)

    name: str
    role: Literal["Player", "Moderator"]
    buzzer_active: bool
    answer: str


class Model:
    """
    Store the current state of the game, like the player list, player inputs, etc.
    """
    _users: dict[str, User] = {}   # Current Users, indexed by the corresponding sid

    @property
    def users(self):
        return list(self._users.values())

    @property
    def users_json(self):
        return [user.model_dump(by_alias=True) for user in self._users.values()]

    def register_user(self, sid: str, data):
        user = User.model_validate(data)
        logger.info(f"Registering new {user} with {sid = !r}")
        self._users[sid] = user

    def unregister_user(self, sid: str):
        if sid in self._users:
            logger.info(f"Unregistering User with {sid = !r}")
            del self._users[sid]

    def set_buzzer(self, sid: str, value: bool, disable_others: bool = True):
        if sid not in self._users:
            logger.error(f"Can't find user with {sid = !r}")

        if disable_others:
            logger.debug("Disabling other buzzers")
            for user in self._users.values():
                user.buzzer_active = False

        logger.debug(f"Setting buzzer for {sid = !r} to {value}")
        self._users[sid].buzzer_active = value

    def set_answer(self, sid: str, answer: str):
        if sid not in self._users:
            logger.error(f"Can't find user with {sid = !r}")

        logger.debug(f"Setting answer from {sid = !r} to {answer = !r}")
        self._users[sid].answer = answer

    def get_broadcast_data(self, field: str) -> list[dict[str, Any]]:
        """
        Return a list of dicts that can be broadcast to all clients, e.g., when a user buzzers
        :param field: The field used as value. E.g., "buzzer_active" or "answer"
        :return: A list of dicts, where each dict look like { name: <username>, value: <value> }
        """
        return [
            {"name": user.name, "value": getattr(user, field)}
            for user in self._users.values()
        ]
