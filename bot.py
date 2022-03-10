import random


def make_list(message):
    return message.split()


class Bot:
    def charlie(self):
        if self == 'quit':
            return "quit"
        else:
            exist = False
            word_list = make_list(self)
            verbs = ["Hamburger", "Kebab", "Pizza"]
            for word in word_list:
                for verb in verbs:
                    if word == verb:
                        exist = True
                        action = str(verb)

            if exist:
                return f"Charlie: {action} sounds hella good"
            else:
                return "Charlie: Yuk🤮"
