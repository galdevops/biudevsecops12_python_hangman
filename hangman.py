import random

# 1: Phrase list from hangman_phrases.py
from hangman_phrases import phrases_list

# 2: Game start settings
chosen_phrase = random.choice(phrases_list).lower().split(' ')
end_of_game = False
correct_guesses = []
score = 0

# 3: Update phrase display
def phrase_display(guess=None):
    updated_display = []
    for word in chosen_phrase:
        display_letters = ''
        for _ in range(len(word)):
            if guess == word[_]:
                display_letters += guess
            elif word[_] in correct_guesses:
                display_letters += word[_]
            else:
                display_letters += "_"
        updated_display.append(display_letters)
    return updated_display

# 4: Initiate display
chosen_phrase_display = phrase_display()


# 5: Start game - ask guess, check guess, update user, score & display
print('Hangman game starting now, goodluck!')

while not end_of_game:
    print(' '.join(chosen_phrase_display))
    # ask guess
    guess = input("Guess a letter: ").lower()

    # If already guessed, update user
    if guess in correct_guesses:
        print(f"You've already guessed {guess}")

    # Check if guessed letter is in chosen_phrase
    if any(guess in sublist for sublist in chosen_phrase) and guess not in correct_guesses:
        correct_guesses.append(guess)
        chosen_phrase_display = phrase_display(guess)
        score += 5
        print(f"You guessed right! You earn 5 points.")
    else:
        if score > 0:
            score -= 5
        print(f"You guessed {guess}, that's not in the phrase. You lose 5 points.")

    # if user has got all letters, it's a win
    if not any("_" in sublist for sublist in chosen_phrase_display):
        end_of_game = True
        print(' '.join(chosen_phrase_display))
        print(f"Congrats, you've won with score {score}")
