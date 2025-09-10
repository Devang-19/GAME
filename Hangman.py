import random

# List of words for the game
words = ["python", "hangman", "programming", "developer", "openai", "contactbook", "computer"]

def hangman():
    word = random.choice(words).upper()   # Choose a random word
    guessed = set()                       # Letters guessed by player
    wrong_guesses = 0                     # Count wrong guesses
    max_guesses = 6                       # Number of chances
    display_word = ["_"] * len(word)      # Hidden word display

    print("🎮 Welcome to Hangman!")
    print("Guess the word: ", " ".join(display_word))

    while wrong_guesses < max_guesses and "_" in display_word:
        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("⚠️ You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"✅ Good guess! {guess} is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ Wrong guess! You have {max_guesses - wrong_guesses} chances left.")

        print("Word: ", " ".join(display_word))
        print("Guessed Letters: ", " ".join(sorted(guessed)))
        print()

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
hangman()
