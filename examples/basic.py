from gameshow import *

questions = [
    Question(
        TextQuestion("What is the Answer to the Ultimate Question of Life, the Universe, and Everything else"),
        BuzzerInput(),
        TextSolution("42")
    ),
    Question(
        TextQuestion("What is the Airspeed velocity of an unladen Swallow"),
        BuzzerInput(),
        TextSolution("An African or European one?")
    ),
    Question(
        TextQuestion("What's the 11th Letter of the Greek Alphabet"),
        TextInput(),
        TextSolution("λ (lambda)")
    )
]

run_gameshow(questions)
