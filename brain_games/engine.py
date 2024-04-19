import prompt


def start_game(game):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)

    rounds_count = 3
    for i in range(rounds_count):
        correct_answer, question = game.get_answer_and_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if str(answer) != str(correct_answer):
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}\n'
                  f'Lets try again, {name}!')
            return
        print('Correct!')

    print(f'Congratulations, {name}')
