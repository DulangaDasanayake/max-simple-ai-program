import datetime
from difflib import SequenceMatcher

class Max:
    def __init__(self):
        self.creation_date = datetime.date(2024, 4, 26)
        self.creator = "ChatGPT"

    def respond(self, user_input):
        if self.similarity(user_input.lower(), "hi") > 0.8:
            return "Hey, buddy..."
        elif self.similarity(user_input.lower(), "hello") > 0.8:
            return "Hello there."
        elif self.similarity(user_input.lower(), "who are you") > 0.8:
            return "I am a simple AI program."
        elif self.similarity(user_input.lower(), "when did you made") > 0.8:
            return "I was made on " + str(self.creation_date) + "."
        elif self.similarity(user_input.lower(), "who made you") > 0.8:
            return "I was made by " + self.creator + "."
        else:
            return "There seems to be a problem. I couldn't understand your input."

    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

def main():
    ai = Max()
    print("Welcome! You can interact with the Max AI program.")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = ai.respond(user_input)
        print("Max AI: " + response)

if __name__ == "__main__":
    main()
