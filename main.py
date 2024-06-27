import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = 0
password = ""

while True:
    password = ""
    length = int(input("Введите длину пароля >>>"))
    count = int(input("Введите кол-во паролей >>>"))
    for i in range(count):
        password = ""
        for i in range(length):
            password = password + symbols[random.randint(0, len(symbols) - 1)]
        print(f"Пароль: {password}\n")
        
