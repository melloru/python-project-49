import random
import operator

DESCRIPTION = 'What is the result of the expression?'

OPERATORS = [('+', operator.add),
             ('-', operator.sub),
             ('*', operator.mul)]


def get_answer_and_question():
    op, fn = random.choice(OPERATORS)
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    correct_answer = fn(num1, num2)
    return correct_answer, f'{num1} {op} {num2}'
