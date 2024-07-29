from dataclasses import dataclass
from flask import request
from flask_socketio import emit
from .server import Server
from .question import QuestionType
from .input import InputType
from .solution import SolutionType


@dataclass
class Question:
    question: QuestionType
    input: InputType
    solution: SolutionType

    def serialize(self, number: int) -> dict[str, dict]:
        return {
            "number": number,
            "question": self.question.serialize(),
            "input": self.input.serialize(),
        }


def run_gameshow(questions: list[Question]):
    app = Server(__name__, "/")
    current_question = -1

    @app.socket.on("login")
    def register_user(data):
        app.model.register_user(request.sid, data)
        emit("users", app.model.users_json, broadcast=True)

    @app.socket.on("disconnect")
    def remove_user():
        app.model.unregister_user(request.sid)
        emit("users", app.model.users, broadcast=True)

    @app.socket.on("answer")
    def store_answer(data):
        app.model.set_answer(request.sid, data)

    @app.socket.on("revealAnswers")
    def reveal_answers():
        emit("answers", app.model.get_broadcast_data("answer"), broadcast=True)

    @app.socket.on("showSolution")
    def show_answer():
        emit("solution", questions[current_question].solution.serialize(), broadcast=True)

    @app.socket.on("nextQuestion")
    def next_question():
        nonlocal current_question
        current_question += 1

        print(f"Showing new question {current_question}")
        emit("question", questions[current_question].serialize(current_question), broadcast=True)

    app.start_server("localhost", allow_unsafe_werkzeug=True)
