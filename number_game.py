import random

answer = random.randint(1, 10)

while True:
    try:
        guess = int(input("guess a number btw 1~10: "))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print("hey idiot, i said btw 1~10")
    except ValueError:
        print("please enter a number")
        continue
