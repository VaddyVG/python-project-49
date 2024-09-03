import random
import prompt
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def play_even_game():
    name = welcome_user()
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    
    while correct_answers_count  < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").lower().strip()
        
        correct_answer = "yes" if is_even(number) else "no"
        
        if answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")


def main():
    play_even_game()


if __name__ == "__main__":
    main()
