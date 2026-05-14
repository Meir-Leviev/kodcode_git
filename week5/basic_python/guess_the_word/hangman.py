import random

hangman = r"""
  _    _             _   _    _____   __  __             _   _
 | |  | |     /\    | \ | |  / ____| |  \/  |     /\    | \ | |
 | |__| |    /  \   |  \| | | |  __  | \  / |    /  \   |  \| |
 |  __  |   / /\ \  | . ` | | | |_ | | |\/| |   / /\ \  | . ` |
 | |  | |  / ____ \ | |\  | | |__| | | |  | |  / ____ \ | |\  |
 |_|  |_| /_/    \_\|_| \_|  \_____| |_|  |_| /_/    \_\|_| \_|
"""
winner = r"""
  __      __.__
 /  \    /  \__| ____   ____   ___________
 \   \/\/   /  |/    \ /    \_/ __ \_  __ \
  \        /|  |   |  \   |  \  ___/|  | \/
   \__/\  / |__|___|  /___|  /\___  >__|
        \/          \/     \/     \/


"""
looser = r"""
  .____
  |    |    ____   ____  ______  ____  _______
  |    |   /  _ \ /  _ \/  ___/_/ __ \_  __ \
  |    |__(  <_> |  <_> \___ \ \  ___/|  | \/
  |_______ \____/ \____/____  > \___  >__|
          \/                \/      \/

                +-------+
                |       |
                |       O
                |      /|\
                |      / \
                |
                -----

"""


def generate_word() -> str:
    # A list of 30 diverse English words in lowercase
    word_list = [
        "abundance", "breeze", "canyon", "dusk", "echo",
        "frost", "glimmer", "horizon", "ink", "jovial",
        "kindle", "lunar", "mist", "nebula", "ocean",
        "pinnacle", "quartz", "rhythm", "summit", "thistle",
        "umbra", "vortex", "willow", "xenon", "yonder",
        "zenith", "amber", "beacon", "cascade", "drift"
    ]
    random_word = random.choice(word_list)
    return random_word


def get_user_guess() -> str:
    while True:
        guess = input('Please enter your guess: ')
        if not guess.isalpha() or len(guess) > 1:
            print("Invalid input. Please enter a single English letter.")
            continue
        else:
            return guess


def is_letter_in_word(letter, secret) -> bool:
    return letter in secret


def find_index(letter, word: str) -> list[int]:
    position = [i for i, char in enumerate(word) if char == letter]
    return position


def reveal_letters(indices: list[int], secret) -> str:
    out_str = ''
    for i in range(len(secret)):
        if i in indices:
            out_str += secret[i]
        else:
            out_str += ' _ '
    return out_str


def print_status(current_word: str, guesses: int,
                 wrong_letters: list[str]) -> None:

    print(f"""
    ---- STATUS ----
     Guess the word

   {current_word}

    wrong guesses left:{guesses}
    wrong letters:
        {wrong_letters}
""")


def check_game_over(revealed_letters, secret, guesses):
    if len(revealed_letters) == len(secret) or guesses < 0:
        return False
    else:
        return True


def game_loop():
    print(hangman)
    secret = generate_word()
    guesses = 10
    revealed_indices = []
    wrong_guesses = set()
    current_word = ''
    running = True
    while running:
        current_word = reveal_letters(revealed_indices, secret)
        print_status(current_word, guesses, wrong_guesses)
        u_guess = get_user_guess()
        if not is_letter_in_word(u_guess, secret):
            guesses -= 1
            print(f'{u_guess} not in word')
            wrong_guesses.add(u_guess)

        elif u_guess not in current_word:
            print('Good guess!')
            tmp = find_index(u_guess, secret)
            revealed_indices += tmp

        else:
            guesses -= 1
        running = check_game_over(revealed_indices, secret, guesses)
    if guesses < 0:
        print(f'THE WORD WAS {secret} ')
        print(looser)
    else:
        print(winner)


def main():
    game_loop()


if __name__ == '__main__':
    main()
