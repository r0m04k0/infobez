from random import choice 

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'"

length = 8

def generate():
    password = ""
    for i in range(length):
        password += choice(alphabet)
    return password

print(generate())