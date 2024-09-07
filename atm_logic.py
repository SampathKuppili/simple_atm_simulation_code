# Variable declarations
bankName = "ABC International Bank"
bankCode = "ABC00001"
bankIfscCode = "ABC000043123"
availableBalance = 1000

# User Options

createOptions = '''
1. Create Account
2. Login 
3. Exit
'''

afterLoginOptions = '''
1. Account Details
2. Credit
3. Debit
4. Check Balance
5. Exit
'''

# Account Creation


def accountCreate():
    global bankUserName, bankUserNumber, bankAccountNo, bankPws
    userName = input("Enter Your Name : ")
    userNumber = int(input("Enter Your Mobile Number: "))
    userAccountNumber = int(input("Enter Your Account Number: "))
    userPassword = int(input("Enter Your Password: "))
    userPwsConform = int(input("Conform Your Password: "))
    bankAccountNo = userAccountNumber
    bankUserName = userName.lower()
    bankUserNumber = userNumber
    bankPws = userPassword
    if userPassword == userPwsConform:
        print("Your account has been created successfully")
    else:
        print("Password does not match with Confirm Password")


def userLogin():
    userNameInput = input("Enter Your Username: ")
    userPasswordInput = int(input("Enter Password: "))
    if userNameInput.lower() == bankUserName and userPasswordInput == bankPws:
        print("\n Hai", bankUserName, "welcome to ABC Bank")

# User Details Function


def userDetails():
    print("Name: ", bankUserName)
    print("Phone Number: ", bankUserNumber)
    print("Bank Name: ", bankName)
    print("Account No: ", bankAccountNo)
    print("Bank Code: ", bankCode)
    print("IFSC Code: ", bankIfscCode)

# Credit Function


def userCredit(amount):
    global availableBalance
    availableBalance = availableBalance + amount
    print("Credit amount: ", amount)
    checkBalance()

# Debit Function


def userDebit(amount):
    global availableBalance
    availableBalance = availableBalance - amount
    print("Debit amount: ", amount)
    checkBalance()

# Check Balance


def checkBalance():
    print("Your Total amount:", availableBalance)
