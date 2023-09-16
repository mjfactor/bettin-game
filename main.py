import random
import pymongo

myclient = pymongo.MongoClient(
    'mongodb+srv://emjayfactor:81roqrSEZezCGE0F@cluster0.9estbbv.mongodb.net/?retryWrites=true&w=majority')

mydb = myclient["sampleDatabase"]  # mydb is the database
myCollection = mydb["sampleTable"]  # This is the table / collection


def main():
    print("---------Welcome------------")
    choice = input("\nWhat game you want to play: ")
    if choice == '1':
        jacknpoy(y)
    elif choice == '2':
        print("hi")


def jacknpoy(credit):
    newCredit = int()
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
                newCredit = credit
            elif pick == "Scissors":
                if compChoice == "Paper":
                    print("Scissors Cut Paper! You win!")
                    newCredit = credit + bet
                else:
                    print("Rock smashes scissors! You lose")
                    newCredit = credit - bet
            elif pick == "Paper":
                if compChoice == "Rock":
                    print("Paper covers rock! You win!")
                    newCredit = credit + bet
                else:
                    print("Scissors Cut Paper! You lose.")
                    newCredit = credit - bet
            elif pick == "Rock":
                if compChoice == "Scissors":
                    print("Rock smashes scissors! You win!")
                    newCredit = credit + bet
                else:
                    print("Paper covers rock! You lose.")
                    newCredit = credit - bet

            myCollection.update_one({"_id": 1}, {"$set": {"credits": newCredit}})
            for r in myCollection.find():
                s = r['credits']
                print(f"Your Credits is {s}")
            break


# money = int(input("How much you want to deposit: "))
# myCollection.update_one({"_id": 1}, {"$set": {"credits": money}})
for x in myCollection.find():
    y = x['credits']
    print(f"Your Credits is {y}")
main()
