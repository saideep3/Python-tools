import random


class Employee:
    'Common base class for all employees'
    empCount = 0
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

    GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

    def __init__(self):
        pass

    def check_for_greeting(self,sentence):
        print(sentence)
        for word in sentence.split():
            if word.lower() in self.GREETING_KEYWORDS:
                print(random.choice(self.GREETING_RESPONSES))
                return random.choice(self.GREETING_RESPONSES)


chat = Employee()
chat.check_for_greeting("hi how are you")
