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
                return f"Charlie: {action} sounds hella good "
            else:
                return "Charlie: Yuk🤮 "

    def chuck(self):
            if self == 'quit':
                return "quit"
            else:
                exist = False
                word_list = make_list(self)
                verbs = ['Kill', 'Torture', 'Drown']
                for word in word_list:
                    for verb in verbs:
                        if word == verb:
                            exist = True
                            action = str(verb)

                if exist:
                    return f"Chuck: Can't you come up with anything else than {action}"
                else:
                    return "Chuck: Get your softass outta here "
