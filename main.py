import datetime
from difflib import SequenceMatcher

class Max:
    def __init__(self):
        self.creation_date = datetime.date(2024, 4, 26)
        self.name = "Max"
        self.creator = "Dulanga Dasanayake"

    def respond(self, user_input):
        user_input = user_input.lower()
        if self.similarity(user_input, "hi") > 0.8:
            return "Hey, buddy!"
        elif self.similarity(user_input, "hello") > 0.8:
            return "Hello there!"
        elif self.similarity(user_input, "what is your name") > 0.8:
            return f"My name is {self.name}."
        elif self.similarity(user_input, "how old are you") > 0.8:
            return f"I was created on {self.creation_date.strftime('%B %d, %Y')}."
        elif self.similarity(user_input, "who are you") > 0.8:
            return "I am an AI program, written in Python."
        elif self.similarity(user_input, "who made you") > 0.8:
            return f"I was created by {self.creator}."
        elif self.similarity(user_input, "can you create pictures") > 0.8:
            return "Unfortunately, I can't create pictures yet."
        elif self.similarity(user_input, "what colour is the sky") > 0.8 or self.similarity(user_input, "colour of sky") > 0.8:
            return "The sky is usually blue."
        elif self.similarity(user_input, "planet") > 0.8:
            return "We live on planet Earth."
        elif self.similarity(user_input, "how are you") > 0.8:
            return "I'm doing great! How about you?"
        elif self.similarity(user_input, "i am fine") > 0.8 or self.similarity(user_input, "i'm fine") > 0.8:
            return "I'm happy to hear that!"
        elif self.similarity(user_input, "when were you made") > 0.8:
            return f"I was made on {self.creation_date.strftime('%B %d, %Y')}."
        else:
            return "I'm sorry, I didn't quite understand that."

    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

def main():
    ai = Max()
    print("Welcome! You can now chat with Max.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = ai.respond(user_input)
        print(f"Max: {response}")

if __name__ == "__main__":
    main()
