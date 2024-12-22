import os
import random
from generateSource import generateSource

def generate_source_file(file_path):
    if not os.path.isfile(file_path):
        generateSource(file_path)

def get_feedback(secret_word, guess):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback.append(f"{guess[i]}: Correct position")
        elif guess[i] in secret_word:
            feedback.append(f"{guess[i]}: Wrong position")
        else:
            feedback.append(f"{guess[i]}: Not in word")
    return feedback

def main():
    # Generate the source file if it doesn't exist
    generate_source_file("inputfile.txt")

    # Read the words from the file
    with open("inputfile.txt", "r", encoding="utf-8") as file:
        words = list(file.read().split())
    
    # Select a random word and total number of attempts
    secret_word = random.choice(words)
    attempts = 7

    print("Guess the 5-letter word!")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if guess == secret_word:
            print("Congratulations! You've guessed the word correctly.")
            break

        feedback = get_feedback(secret_word, guess)
        for f in feedback:
            print(f)
        print("\n")
    else:
        print(f"Sorry, you've used all your attempts. The word was '{secret_word}'.")

if __name__ == "__main__":
    main()