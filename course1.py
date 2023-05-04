# Colors codes
RED = "\033[91m"
BLACK = "\033[0m"
YELLOW = "\033[33m"

# Opening title
HANGMAN_ASCII_ART = """Welcome to the Hangman game!\n\
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ \n"""

# Maximum number of guesses
MAX_TRIES = 6

# Representation of the 7 states of the game
STATE1 = "    x-------x"
STATE2 = """    x-------x
    |
    |
    |
    |
    |"""
STATE3 = """    x-------x
    |       |
    |       0
    |
    |
    |
"""
STATE4 = """    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
STATE5 = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""
STATE6 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""
STATE7 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

# Dict of the game's 7 states
HANGMAN_PHOTOS = {0: STATE1, 1: STATE2, 2: STATE3, 3: STATE4, 4: STATE5, 5: STATE6, 6: STATE7}


# Prints the opening screen
def opening_screen():
    print("\n", RED + HANGMAN_ASCII_ART + BLACK)
    print("The Maximum Amount Of Attempts Is:", MAX_TRIES, "\n")


# Receives from the user the data to find the secret word
def find_secret_word():
    file_path = input("Enter the path to the words file: ")
    index = int(input("Enter the index of the word in the file: "))
    print('\n')

    return choose_word(file_path, index)


# Prints the state received as an argument
def print_hangman(num_of_tries):
    print(RED + "Current State of the hangman:")
    print(HANGMAN_PHOTOS[num_of_tries], '\n' + BLACK)


# Finds word in a given index in the file
def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        file_str = file.read()
        words_lst = file_str.split()

        i = index % len(words_lst)   # indicates the final position of the word in the file

        return words_lst[i - 1]


# Checks if the guess is a single alphabetical letter and hasn't been guessed before
def is_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed


# Tries to add a letter to the guessed list if it doesn't exist there
# otherwise prints the past guessed letters
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True

    print('You\'ve already gusessed the letter \'' + letter_guessed + '\'')
    x = list(map(lambda letter: letter + ' -> ', sorted(old_letters_guessed)[:-1:]))
    if x:
        print('The letters you\'ve already gusessed are:', end='  ')
        x.append(sorted(old_letters_guessed)[-1])
        print(''.join(x))
        print()
    return False


# Presents the letters guessed in the secret word in their position in the word
def show_hidden_word(secret_word, old_letters_guessed):
    progress_str = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            progress_str += letter + ' '
        else:
            progress_str += '_ '

    print(YELLOW + progress_str + BLACK + '\n')


# Checks if the player won
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def main():
    # Presents the game's opening screen
    opening_screen()

    # Generates a secret word for the game
    secret_word = find_secret_word()

    # Initializes the past-guessed list the attempts counter
    old_letters_guessed = list()
    num_of_tries = 0

    # Presents the initial state
    print_hangman(num_of_tries)
    print("The Secret Word Pattern Is:", end='   ')
    show_hidden_word(secret_word, old_letters_guessed)

    # Keeps playing if the player didn't win and has more attempts
    while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:
        letter_guessed = input("Guess a letter: ").lower()

        # Checks if the player already guessed the given letter
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                num_of_tries += 1
                print("The letter '" + letter_guessed + "' isn't part of the secret word")
                print_hangman(num_of_tries)

            show_hidden_word(secret_word, old_letters_guessed)

    # Checks if the player won or lost
    print('\n')
    if num_of_tries < MAX_TRIES:
        print(RED + "WIN!" + BLACK)
    else:
        print(RED + "LOSE!" + BLACK)


if __name__ == "__main__":
    main()
