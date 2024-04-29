import datetime
from difflib import SequenceMatcher

class Max:
    def __init__(self):
        self.creation_date = datetime.date(2024, 4, 26)
        self.name="Max"
        self.creator = "Dulanga Dasanayake"

    def respond(self, user_input):
        if self.similarity(user_input.lower(), "hi") > 0.8:
            return "Hey, buddy..."
        elif self.similarity(user_input.lower(), "hello") > 0.8:
            return "Hello there."
        elif self.similarity(user_input.lower(), "what is your name") > 0.8:
            return "I am " + str(self.name) + "."
        elif self.similarity(user_input.lower(), "how old are you") > 0.8:
            return "I am Just Born."
        elif self.similarity(user_input.lower(), "who are you") > 0.8:
            return "I am a simple AI program written by python."
        elif self.similarity(user_input.lower(), "can you create pictures") > 0.8:
            return "No."
        elif self.similarity(user_input.lower(), "when did you made") > 0.8:
            return "I was made on " + self.creation_date + "."
        elif self.similarity(user_input.lower(), "who made you") > 0.8:
            return "I was made by " + self.creator + "."
        elif self.similarity(user_input.lower(), "what colour is the sky") > 0.8:
            return "Blue."
        elif self.similarity(user_input.lower(), "colour of sky") > 0.8:
            return "Blue."
        elif self.similarity(user_input.lower(), "planet") > 0.8:
            return "Our planet is earth."
        elif self.similarity(user_input.lower(), "h") > 0.8:
            return "Hello How Are You.."
        elif self.similarity(user_input.lower(), "i") > 0.8:
            return "Hello How Are You.."
        elif self.similarity(user_input.lower(), "i am fine, thanks you") > 0.8:
            return "I am Happy to here that.."
        elif self.similarity(user_input.lower(), "i'm fine") > 0.8:
            return "I am Happy to here that.."
        elif self.similarity(user_input.lower(), "how are you") > 0.8:
            return "I am Just Fine.. How About You.."
        else:
            return "There seems to be a problem. I couldn't understand your input."

    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

def main():
    ai = Max()
    print("Welcome! Now You can chat with the Max")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = ai.respond(user_input)
        print("Max: " + response)

if __name__ == "__main__":
    main()
