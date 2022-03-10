self="Kebab er super digg"
exist = False
word_list = self.split()
verbs = ["Hamburger", "Kebab", "Pizza"]
for word in word_list:
   for verb in verbs:
        if word == verb:
            exist = True
            action = str(verb)

if exist:
    print( f"{action} sounds hella good")
else:
    print("Yuk🤮")