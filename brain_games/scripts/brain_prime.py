import random
import math
from brain_games.cli import welcome_user
from brain_games.game_engine import run_game


def simple_number(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = f"{number}"
    correct_answer = "yes" if simple_number(number) else "no"
    return question, correct_answer


def main():
    name = welcome_user()
    game_description = ('Answer "yes" if given number is prime.'
                        'Otherwise answer "no".')
    run_game(game_description, generate_question_and_answer, name)


if __name__ == "__main__":
    main()
