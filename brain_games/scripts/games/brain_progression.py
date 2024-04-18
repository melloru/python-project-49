from math import gcd
import prompt
import random
from brain_games.scripts import brain_game


def main():
    name = brain_game.main()
    print('What number is missing in the progression?')
    for i in range(0, 3):
        step = random.randint(2, 13)
        progression = [random.randint(5, 30)]

        for j in range(0, 9):
            progression.append(progression[j] + step)

        correct_answer = progression[random.randint(1, len(progression) - 1)]
        pass_step = progression.index(correct_answer)
        progression[pass_step] = '..'
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')

        if brain_game.logic(answer, correct_answer, name) is not None:
            return

    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()



