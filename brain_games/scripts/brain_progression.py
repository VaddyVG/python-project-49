import random
from brain_games.game_engine import run_game
from brain_games.cli import welcome_user


def generate_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    progression = [start + step * i for i in range(length)]

    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])

    progression[missing_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


def main():
    name = welcome_user()
    game_description = "What number is missing in the progression?"
    run_game(game_description, generate_question_and_answer, name)

  
if __name__ == "__main__":
    main()
