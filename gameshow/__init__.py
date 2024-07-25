from flask import Flask, request
from flask_socketio import SocketIO, emit
from model import Model
from buzzer import initialize_buzzers

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
    app = Flask(__name__, "/")
    socket = SocketIO(app)
    model = Model()
    currentQuestion = -1

    @app.route("/")
    def root():
        return app.redirect("index.html")

    @socket.on("login")
    def register_user(data):
        model.register_user(request.sid, data)
        emit("users", model.users_json, broadcast=True)

    @socket.on("disconnect")
    def remove_user():
        model.unregister_user(request.sid)
        emit("users", model.users, broadcast=True)

    @socket.on("answer")
    def store_anwer(data):
        model.set_answer(request.sid, data)

    @socket.on("revealAnswers")
    def reveal_answers():
        emit("answers", model.get_broadcast_data("answer"), broadcast=True)

    @socket.on("showSolution")
    def show_answer():
        print(f"Showing Solution")
        emit("solution", QUESTIONS[currentQuestion]["solution"], broadcast=True)

    @socket.on("nextQuestion")
    def next_question():
        nonlocal currentQuestion
        currentQuestion += 1

        print(f"Showing new question {currentQuestion}")
        data = {**QUESTIONS[currentQuestion]}
        del data["solution"]
        emit("question", QUESTIONS[currentQuestion], broadcast=True)

    # Initialize Buzzers
    initialize_buzzers(socket, model)

    socket.run(app, "localhost", allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    main()
