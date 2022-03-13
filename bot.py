import random


def extract(message, verbs):
    words = message.split()
    for word in words:
        for verb in verbs:
            if word.lower() == verb.lower():
                return verb.lower(), True

    return False, None


class Bot:
    def charlie(self):
        verbs = ["fly", "travel", "sail", "diving"]
        word, exist = extract(self, verbs)
        if exist:
            return f"Charlie: {word} sounds fun!"
        else:
            return "Charlie: If it ain't travelrelated count me out"

    def chuck(self):
        verbs = ["fly", "travel", "sail", "diving"]
        alternatives = ["sing", "code", "swim"]
        alternative = random.choice(alternatives)
        word, exist = extract(self, verbs)
        if exist:
            return f"Chuck: Depends on where we are {word}ing !"
        else:
            return f"Chuck: Why dont we {alternative} instead?"

    def chong(self):
        verbs = ["workout", "lift", "eat"]
        word, exist = extract(self, verbs)
        if exist:
            return f"Kevn: Im not sure about {word}ing!"
        else:
            return f"Kevin: I'd prefere working out"
