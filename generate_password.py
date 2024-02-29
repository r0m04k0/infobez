from random import choice 
import math

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'"


def generate(length):
    password = ""
    for i in range(length):
        password += choice(alphabet)
    return password

P = 10**(-6)
V = 20
T = 3 * 7 * 24 * 60

S = V * T / P
length = math.ceil(math.log(S, len(alphabet)))
print(length)

print(generate(length))


# Реализовать программу для генерации паролей пользователей. 
# Программа должна формировать случайную последовательность символов 
# длины L, при этом должен использоваться алфавит из A символов.