import random
from brain_games.game_engine import run_game
from brain_games.cli import welcome_user


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = f"{number}"
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer


def main():
    name = welcome_user()
    game_description = ('Answer "yes" if the number is even, '
                        'otherwise answer "no".')
    run_game(game_description, generate_question_and_answer, name)


if __name__ == "__main__":
    main()
