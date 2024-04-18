import prompt
import random
from brain_games.scripts import brain_game


def main():
    name = brain_game.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(0, 3):
        number = random.randint(5, 30)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes'
        for j in range(2, number // 2 + 1):
            if number % j == 0:
                correct_answer = 'no'
                break

        if brain_game.logic(answer, correct_answer, name) is not None:
            return

    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
