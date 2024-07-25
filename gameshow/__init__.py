from flask import request
from flask_socketio import emit
from model import Model
from server import Server

QUESTIONS = [
    {
        "type": "buzzer",
        "number": 1,
        "text": "What is the Answer to the Ultimate Question of Life, the Universe, and Everything else",
        "solution": 42,
    },
    {
        "type": "buzzer",
        "number": 2,
        "text": "What is the Airspeed velocity of an unladen Swallow",
        "solution": "An African or European one?",
    },
    {
        "type": "input",
        "number": 3,
        "text": "What's the 11th Letter of the Greek Alphabet",
        "solution": "λ (lambda)"
    }
]


def main():
    app = Server(__name__, "/")
    currentQuestion = -1

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
        print(f"Showing Solution")
        emit("solution", QUESTIONS[currentQuestion]["solution"], broadcast=True)

    @app.socket.on("nextQuestion")
    def next_question():
        nonlocal currentQuestion
        currentQuestion += 1

        print(f"Showing new question {currentQuestion}")
        data = {**QUESTIONS[currentQuestion]}
        del data["solution"]
        emit("question", QUESTIONS[currentQuestion], broadcast=True)

    app.start_server("localhost", allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    main()
