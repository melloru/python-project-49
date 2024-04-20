import random

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def get_answer_and_question():
    number = random.randint(1, 30)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return correct_answer, str(number)
