import random

def hangman_game_simulated(guesses):
    # List of words for the game
    words = ['python', 'hangman', 'computer', 'science', 'programming', 'artificial', 'intelligence']
    
    # Randomly select a word from the list
    word = random.choice(words).lower()
    
    # Create a list of underscores to represent the unguessed word
    guessed_word = ['_'] * len(word)
    
    # Set of incorrect guesses and number of tries allowed
    incorrect_guesses = set()
    max_tries = 6
    attempts_left = max_tries
    
    # Simulate game
    print("Word to guess: ", ' '.join(guessed_word))
    print(f"Simulated guesses: {guesses}")
    
    for guess in guesses:
        if attempts_left == 0 or '_' not in guessed_word:
            break
        
        print(f"\nGuessing letter: {guess}")
        
        # Check if the guessed letter is in the word
        if guess in word:
            # Update guessed word
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            # Incorrect guess
            if guess not in incorrect_guesses:
                incorrect_guesses.add(guess)
                attempts_left -= 1
            else:
                print(f"You've already guessed the letter '{guess}'.")
        
        # Display the current status
        print("Word to guess: ", ' '.join(guessed_word))
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts left: {attempts_left}")
    
    # End game
    if '_' not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Simulated guesses for demonstration
simulated_guesses = ['e', 'a', 'r', 't', 'i', 'o', 'n', 's', 'c']
hangman_game_simulated(simulated_guesses)
