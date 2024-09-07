from banking_source import *

print("#"*5, "Welcome to ABC Bank", "#"*5)


while True:
    print(createOptions)
    userInput1 = int(input("Select any one option: "))
    if userInput1 == 1:
        accountCreate()
    elif userInput1 == 2:
        userLogin()
        while True:
            print(afterLoginOptions)
            userInput3 = int(input("Select any one option: "))
            if userInput3 == 1:
                userDetails()
            elif userInput3 == 2:
                enterAmout1 = float(input("Enter Credit amount: "))
                userCredit(enterAmout1)
            elif userInput3 == 3:
                enterAmout2 = float(input("Enter Debit amount: "))
                userDebit(enterAmout2)
            elif userInput3 == 4:
                checkBalance()
            else:
                print("Thank You for Banking")
                break
            userInput2 = input("Do you want to continue (Yes/No): ")
            if userInput2.lower() == "yes":
                continue
            else:
                break
    else:
        break
