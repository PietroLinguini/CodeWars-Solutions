from math import sqrt


def is_square(n: int) -> bool:
    if n < 0: return False
    return sqrt(n) == int(sqrt(n))

def is_square(n: int) -> bool:
    return n > -1 and sqrt(n) % 1 == 0