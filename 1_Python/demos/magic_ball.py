import random


def magic_ball():
    answers = ["Yes.", "No.", "Don't even think about it.",
              "Take a hike!", "Of Course.", "Maybe.", "Sorry, wasn't listening",
              "Not a chance...", "Whatever", "If you try!"]

    input("\nWhat is your question? ")

    random_index = random.randint(0,len(answers) - 1)

    print(answers[random_index])

    play_again = input("\nPlay again? (Yes/No) ")
    if play_again.lower() == str("yes"):
        magic_ball()
    else:
        exit()


def game():
    print("\nWelcome to the magic 8 ball.\n", flush=True)
    stay_or_go = input("Type \'play\' or \'exit\': ")

    if stay_or_go == str("play"):
        magic_ball()

    elif stay_or_go == str("exit"):
        exit()

    else:
        print("What?")
        game()

game()
