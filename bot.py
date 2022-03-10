import random


def check_message(message, verbs):
    exist = False  # Is verb in message?
    action = None  #

    words = message.split()
    for word in words:
        for verb in verbs:
            if word == verb:
                exist = True
                action = verb
    return exist, action


class Bot:
    def charlie(self):
        if self == 'quit':
            return "quit"
        else:
            verbs = ["Hamburger", "Kebab", "Pizza"]
            exist, word = check_message(self, verbs)
            if exist:
                return f"Charlie: {word} sounds hella good "
            else:
                return "Charlie: Yuk🤮 "

    def chong(self):
        if self == 'quit':
            return "quit"
        else:
            verbs = ["Squats", "Bench", "Deadlift"]
            exist, word = check_message(self, verbs)
            if exist:
                return f"Chong: Boi, lets go {word}. Right now!"
            else:
                return "Chong: No weights, no gains 💪🏻 "
