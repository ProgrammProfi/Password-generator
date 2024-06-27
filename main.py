import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = 0
password = ""

while True:
    password = ""
    length = int(input("Введите длину пароля >>>"))
    for i in range(0, length):
        password = password + symbols[random.randint(1, len(symbols) - 1)]
    print(password)
