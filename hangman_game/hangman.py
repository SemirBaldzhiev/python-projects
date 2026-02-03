from hangman_art import logo, stages
from hangman_words import word_list
import random

def choose_word():
    return random.choice(word_list)

def make_placeholder(word):
    return "_" * len(word)

def is_valid_guess(guess, letters):
    if guess.isspace() or (guess < "a" or guess > "z"):
        print("Please enter a valid letter!")
        return False
        
    if guess in letters:
        print("You have already guessed that letter!")
        return False

    return True
    
def play():
    print(logo)
    
    generated_word = choose_word()
    print(f"Word to guess: {make_placeholder(generated_word)}")
    
    lives = 6
    game_over = False
    correct_letters = []
    
    while not game_over:
        
        user_guess = input("Guess a letter: ").lower()
        
        if not is_valid_guess(user_guess, correct_letters):
            continue
        
        display_word = ""
        
        for letter in generated_word:
            if letter == user_guess:
                display_word += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"Word to guess: {display_word}")

        if user_guess not in generated_word:
            print(f"You guessed {user_guess}, that is not in the word.")
            print(stages[lives])
            lives -= 1
            
            if lives < 0:
                game_over = True
                print(f"YOU LOSE! The word was {generated_word}")
        
        if "_" not in display_word:
            game_over = True
            print("YOU WIN!")
            

play()
