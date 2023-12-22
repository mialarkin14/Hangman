# A hangman game in python
import random

def build_sentence(sentence, correct, letter_guesses):
    '''
    A function that builds a guess sentence based on the letetrs guessed
    Returns the number of letters guessed
    '''

    # Set up variables
    guess_sentence = []
    counter = 0
    sen_len = len(sentence)
    k = 0
    y = len(guess_sentence)

    # Initialize the guess_sentence array
    while k < sen_len:
        # Place a zero where there is a letter
        if sentence[k] != " ":
            guess_sentence.append(0)
        # Place a one where there is a space
        elif sentence[k] == " ":
            guess_sentence.append(1)
        k += 1

    while counter < len(letter_guesses):
        # Get a letter from the guessed letters
        letter = letter_guesses[counter]
        # Set up a list that holds the index of that letter in the sentence
        letter_index = []
        # Get the index(es) of the letter
        i = 0
        while i < sen_len:
            if sentence[i] == letter:
                letter_index.append(i)
            i += 1
        # Add to the guess sentence
        j = 0
        while j < len(letter_index):
            index = letter_index[j]
            guess_sentence[index] = letter
            j += 1
        # Move onto the next guessed letter
        counter += 1
    
    # Print out an empty position holder if we are at the start of the game 
    if correct == 0:
        for char in sentence:
            if char != " ":
                print("_", end = "")
            else:
                print(" ", end = "")
        print()
        print()
    
    # Otherwise print out the guessed sentence
    else:
        print()
        x = 0
        while x < sen_len:
            # If there is a zero, print out a blank space
            if guess_sentence[x] == 0:
                print("_", end = "")
            # If there is a one, print a space 
            elif guess_sentence[x] == 1:
                print(" ", end = "")
            # Otherwise, it's a letter so print it
            else: 
                print(guess_sentence[x], end = "")
            x += 1
        print()
        print()
    
    # Return the guess sentence
    return guess_sentence


def choose_sentence(diff_integer):
    '''
    A function that chooses a sentence from the sentences.txt based on the 
    difficulty chossen and returns the sentence
    '''
    rand_num = 0
    # Choosing a sentence based on the difficulty 
    if diff_integer == 1:
        # Generate a random number bewteen 1-19
        rand_num = random.randint(0, 19)
    
    elif diff_integer == 2:
        # Generate a random number bewteen 19-33
        rand_num = random.randint(19, 33)
        
    elif diff_integer == 3:
        # Generate a random number bewteen 33-40
        rand_num = random.randint(33, 40)
    
    with open("sentences_words.txt", "r") as fp:
        lines = fp.readlines()
    
    # Return the sentence
    return lines[rand_num]

def print_letters_guessed(guessed):
    '''
    Prints the letters that the player has guessed
    No return
    '''
    # Prints all of the guessed letters
    print("You have guessed the following letters:\n")
    for letter in guessed:
        print(f"{letter}", end = ", ")
    print() 

def print_hangman(num_incorrect):
    '''
    A function that prints out the hangman picture
    Takes in paramter "num_incorrect" and prints the hangman based
    on the number of incorrect guesses from the player
    No return
    '''

    if num_incorrect == 0:
        # Prints an empty stand if no incorrect guesses
        print("\n")
        print(" +========+")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("===")
        print("\n")
    
    if num_incorrect == 1:
        # Adds a head
        print("\n")
        print(" +========+")
        print(" |        0")
        print(" |")
        print(" |")
        print(" |")
        print("===")
        print("\n")
    
    if num_incorrect == 2:
        # Adds a body
        print("\n")
        print(" +========+")
        print(" |        0")
        print(" |        |")
        print(" |")
        print(" |")
        print("===")
        print("\n")
    
    if num_incorrect == 3:
        # Adds an arm
        print("\n")
        print(" +========+")
        print(" |        0")
        print(" |       /|")
        print(" |")
        print(" |")
        print("===")
        print("\n")
    
    if num_incorrect == 4:
        # Adds a arm
        print("\n")
        print(" +========+")
        print(" |        0")
        print(" |       /|\ ")
        print(" |")
        print(" |")
        print("===")
        print("\n")
    
    if num_incorrect == 5:
        # Adds a leg
        print("\n")
        print(" +========+")
        print(" |        0")
        print(" |       /|\ ")
        print(" |       /")
        print(" |")
        print("===")
        print("\n")
    
    if num_incorrect == 6:
        # Adds a leg
        print("\n")
        print(" +========+")
        print(" |        0")
        print(" |       /|\ ")
        print(" |       / \ ")
        print(" |")
        print("===")
        print("\n")

if __name__ == "__main__":
    
    # Start the game with a greeting to play hangman 
    print("Hi! Let's play Hangman!")
    
    # Choose the difficulty of the game
    difficulty = input("Choose the level of difficulty 1-3\n")
    diff_integer = int(difficulty) 
    
    # If the player inputs a different level, request one within the range
    if diff_integer > 3:
        print("Please choose a level between 1 - 3\n")
    print(f"You have choosen difficulty level {difficulty}! Let the game begin!")
    
    # Set up variables and choose a sentence based on the level of difficulty
    num_incorrect = 0
    num_correct = 0
    letter_guesses = []
    sentence = []
    num_guesses = 0
    string_list = []

    # Save the line in the sentence
    sentence0 = choose_sentence(diff_integer)
    # Take away the newline and make it all lowercase
    sentence = sentence0.strip().lower()
    # Create a sentence list based on the string
    for char in sentence:
        if char != " ":
            string_list.append(char)
        else:
            string_list.append(1)

    # Print out the characters in the sentence
    build_sentence(sentence, num_correct, letter_guesses)
    

    # While the number of incorrect guesses is less than or equal to 6 play the game
    while num_incorrect < 6:
        # Print out the hangman
        print_hangman(num_incorrect)
        # Get a guess from the player
        letter = input("Guess a letter (Please choose only lowercase letters)\n")
        letter_guesses.append(letter)
        num_guesses += 1
        
        # Check if the letter is in the sentence
        if letter not in sentence:
            # If it isn't, increase the number of incorrect guesses
            num_incorrect += 1
        
        # Otherwise the character is correct so increase correct counter
        num_correct += 1
        
        # Print out the leters guessed
        print_letters_guessed(letter_guesses)
        
        # Print out your the sentence being pieced together
        guess_list = build_sentence(sentence, num_correct, letter_guesses)
        
        # If the built sentence is equal the sentence then break
        if guess_list == string_list:
            break
    
    # Case: The player lost 
    if num_incorrect == 6:
        print("Sorry you didn't guess the sentence in the time!")
        print(f"The sentence was: {sentence}")
    
    # Case: The player won 
    else:
        print("Congrats! You Won!")