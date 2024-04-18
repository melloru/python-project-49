import prompt
import random
import operator
from brain_games.scripts import brain_game


def main():
    name = brain_game.main()
    print('What is the result of the expression?')
    for i in range(3):
        operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
        op, fn = random.choice(operators)
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)

        print("{} {} {} {}".format('Question:', num1, op, num2))
        correct_answer = fn(num1, num2)

        answer = prompt.string('Your answer: ')

        if brain_game.logic(answer, correct_answer, name) is not None:
            return
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
