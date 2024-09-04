import math
import random
from brain_games.game_engine import run_game
from brain_games.cli import welcome_user


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer


def main():
    name = welcome_user()
    game_description = "Find the greatest common divisor of given numbers."
    run_game(game_description, generate_question_and_answer, name)


if __name__ == "__main__":
    main()
