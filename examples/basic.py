from gameshow import GameShow
from gameshow.questions import MultipleChoiceQuestion as MCQ, GuesstimationQuestion as GQ, InputQuestion as IQ


modules = ["buzzers"]

MCQ.options = {
    "timeout": 30,
    "randomize_order": True,
    "input_method": "buzzer",
}

questions = [
    MCQ("What's 1+1?", ["1", "2", "3", "4"], "2"),
    MCQ("What did Einstein earn the Nobel Price for?", ["General Relativity", "Special Relativity", "The Photoelectric Effect"], 2),
    IQ("Name 3 Video Games for the PlayStation 1", 3),
    GQ("How many different people have served as US President", 45)
]


gameshow = GameShow(questions, modules=modules)
gameshow.start()
