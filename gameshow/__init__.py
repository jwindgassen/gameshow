from flask import Flask, request
from flask_socketio import SocketIO, emit


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
    users = {}
    answers = {}
    currentQuestion = -1

    @app.route("/")
    def root():
        return app.redirect("index.html")

    @socket.on("login")
    def register_user(data):
        nonlocal users

        users[request.sid] = data
        emit("users", list(users.values()), broadcast=True)

    @socket.on("disconnect")
    def remove_user():
        nonlocal users

        if request.sid in users:
            del users[request.sid]

    @socket.on("buzzer")
    def buzzer():
        print(f"Buzzer from {request.sid}")
        data = [{"name": value["name"], "value": key == request.sid} for key, value in users.items()]
        emit("buzzers", data, broadcast=True)

    @socket.on("clearBuzzers")
    def clear_buzzers():
        print("Clearing buzzers")
        data = [{"name": value["name"], "value": False} for value in users.values()]
        emit("buzzers", data, broadcast=True)

    @socket.on("answer")
    def store_anwer(data):
        nonlocal answers

        print(f"Received Answer from {request.sid}")
        answers[request.sid] = data

    @socket.on("revealAnswers")
    def reveal_answers():
        print(f"Revealing Answers")
        data = [{"name": value["name"], "value": answers[key]} for key, value in users.items()]
        emit("answers", data, broadcast=True)

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


    socket.run(app, "localhost", allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    main()
