from random import randint
import math

GAME_QUESTION = "Find the greatest common divisor of given numbers."


def generate_round():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    task = (f"{num_1} {num_2}")
    
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    result = num_1 + num_2
    return task, str(result)
