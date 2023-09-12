import random


def jacknpoy(credit):
    print("You Played Rock Paper and Scissors\n")
    while True:
        bet = int(input("How much you want to bet? "))
        if bet > credit:
            print("Not enough credits")
        else:
            break
    pick = str(input("1. Rock\n2. Scissors\n3. Paper\nChoose: "))
    if pick == '1':
        pick = "Rock"
    elif pick == '2':
        pick = "Scissors"
    elif pick == '3':
        pick = "Paper"
    x = random.choice(["Rock", "Paper", "Scissors"])
    if pick == x:
        print("You Won")
        credit = credit + bet
    elif pick != x:
        print("You Lose")
        credit = credit - bet
        if credit == 0:
            print(f"Your Credit is now {credit}")
            exit()
    print(f"Your Current credits is now {credit}")


def coinToss():
    print("You Played Coin Toss\n")
    pick = str(input("1. Heads\n2. Tails\nChoose: "))


while True:
    money = int(input("How much you want to deposit: "))
    if money < 1000:
        print("Can't deposit below 1000")
    else:
        print(f"You Deposited {money} peso")
        break

print("---------Welcome------------")
choice = input("What game you want to play: ")
if choice == '1':
    jacknpoy(money)
elif choice == '2':
    coinToss()
