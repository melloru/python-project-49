import prompt
import random
from brain_games.scripts import brain_game


def main():
    name = brain_game.main()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for i in range(0, 3):
        number = random.randint(1, 30)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if number % 2 == 0 else 'no'

        if brain_game.logic(answer, correct_answer, name) is not None:
            return

    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
