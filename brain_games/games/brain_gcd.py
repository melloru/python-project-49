import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_answer_and_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 30)
    correct_answer = math.gcd(num1, num2)
    return correct_answer, f'{num1} {num2}'
