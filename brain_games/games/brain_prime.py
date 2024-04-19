import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_answer_and_question():
    number = random.randint(5, 30)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return correct_answer, str(number)
