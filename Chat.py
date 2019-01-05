#!/usr/bin/python

class Chat:

    GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

    GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

    def check_for_greeting(self, sentence):
        """If any of the words in the user's input was a greeting, return a greeting response"""
        for word in sentence.words:
             if word.lower() in self.GREETING_KEYWORDS:
                return random.choice(self.GREETING_RESPONSES)


chat = Chat()
print(chat.check_for_greeting(sentence="ff fgt"))