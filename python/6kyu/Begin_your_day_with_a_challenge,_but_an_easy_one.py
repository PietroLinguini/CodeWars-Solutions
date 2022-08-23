def one_two_three(n):
    if n == 0: return [0,0]
    second = ""
    for _ in range(n):
        second += "1"
    first = ""
    while n >= 9:
        first += "9"
        n -= 9
    if (n > 0): first += str(n)
    return [int(first), int(second)]

# ALTERNATIVES
def one_two_three(n):
    first, second = "9" * (n / 9), "1" * n
    if n % 9: first += str(n % 9)
    return [int(first) if first else 0, int(second) if second else 0]

one_two_three = lambda n: [int(n/9*'9'+(n%9>0)*repr(n%9)or 0),int(n*'1'or 0)]
def one_two_three(n):
    return [int('9'* (n / 9) + (str(n % 9) if n % 9 else '') or 0), int(('1'*n) or 0)]