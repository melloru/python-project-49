import random

DESCRIPTION = 'What number is missing in the progression?'


def get_answer_and_question():
    start = random.randint(5, 30)
    step = random.randint(2, 13)
    length = 10
    stop = start + length * step

    progression = list(range(start, stop, step))
    hidden_index = random.randrange(length)

    correct_answer, progression[hidden_index] = progression[hidden_index], '..'

    return correct_answer, ' '.join(map(str, progression))
