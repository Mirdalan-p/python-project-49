from random import randint

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    random_num = randint(1, 100)
    task = f"{random_num}"
    result = ''
    i = 0
    for devider in range(2, random_num // 2 + 1):
        if random_num % devider == 0:
            i += 1
    if i <= 0:
        result = 'yes'
    else:
        result = 'no'
    return task, result