import random
import mysql.connector



conn = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="your_password",
    database="betgame"
)
create_table_query = """
CREATE TABLE moeny (
    id INT AUTO_INCREMENT PRIMARY KEY,
    credits INT(8),
)
"""
cursor = conn.cursor()
cursor.execute(create_table_query)

insert_data_query = "INSERT INTO money (credits) VALUES (%s)"
user_data = (4)
cursor.execute(insert_data_query, user_data)
conn.commit()


def jacknpoy(credit):
    print("You Played Rock Paper and Scissors")
    temp = True
    while temp:
        bet = int(input("\nHow much you want to bet? "))
        if bet > credit:
            print("Not enough credits")
        else:
            pick = str(input("1. Rock\n2. Scissors\n3. Paper\nChoose: "))
            if pick == '1':
                pick = "Rock"
            elif pick == '2':
                pick = "Scissors"
            elif pick == '3':
                pick = "Paper"

            compChoice = random.choice(["Rock", "Paper", "Scissors"])
            print(f"\nYou chose {pick.upper()}, computer chose {compChoice.upper()}.\n")
            if pick == compChoice:
                print("It a Tie!")
            elif pick == "Scissors":
                if compChoice == "Paper":
                    print("Scissors Cut Paper! You win!")
                    credit = credit + bet
                else:
                    print("Rock smashes scissors! You lose")
                    credit = credit - bet
            elif pick == "Paper":
                if compChoice == "Rock":
                    print("Paper covers rock! You win!")
                    credit = credit + bet
                else:
                    print("Scissors Cut Paper! You lose.")
                    credit = credit - bet
            elif pick == "Rock":
                if compChoice == "Scissors":
                    print("Rock smashes scissors! You win!")
                    credit = credit + bet
                else:
                    print("Paper covers rock! You lose.")
                    credit = credit - bet
            print(f"Your Credit is now {credit} \n")
            while True:    
                choice = input("Do you want to try again? Press Y or N: ")
                if choice == 'N' or choice == 'n':
                    temp = False
                    break
                elif choice == 'Y' or choice == 'y':
                    break
            


def coinToss():
    print("You Played Coin Toss\n")
    pick = str(input("1. Heads\n2. Tails\nChoose: "))


class main:
    print("---------Welcome------------")
    while True:
        money = int(input("How much you want to deposit: "))
        if money < 1000:
            print("Can't deposit below 1000")
        else:
            print(f"You Deposited {money} peso")
            break

    choice = input("\nWhat game you want to play: ")
    if choice == '1':
        jacknpoy(money)
    elif choice == '2':
        coinToss()
