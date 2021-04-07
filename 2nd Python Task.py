from datetime import date

today = date.today( )
print (today)

from datetime import datetime
now = datetime.now( )

currentTime = now.strftime("%H:%M:%S")
print (currentTime)

import random

database = {}

def init():
    
    isValidOptionSelected = False
    print("Welcome to Money Bank")

    while isValidOptionSelected == False:
    
        haveAccount = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))
        
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print("You have selected an invalid option")

def login():
    print("-------Login to your account--------")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your unique password \n")

    for accountNumber, userDetails in database.items():
        if (accountNumber == accountNumberFromUder):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print("invalid account or password")
    login()

    

def register():
    print("-------Register Now--------")
    email = input("What is your email address? \n")
    firstName  = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("Create your unique password \n")
    generationAccountNumber()

def generationAccountNumber():

    print("here is your account number: 185289634")
    login()
    
    return random.randrange(1111111111,9999999999)
    
    accountNumber = generationAccountNumber()
    
    database[acountNumber] = [ firstName, lastName, email, password ] 

    print ("You have successfully created an account")

    login ()
    
    return database
    
def bankOperation(user):

    
    print("welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) logout (4) exit \n"))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logoutOperation()
    elif(selectedOption == 4):
        exitOperation()
    else:
        print("You have chosen an invalid option")
        bankOperation(user)

def withdrawalOperation():
    print ("withdrawal")

def depositOperation():
    print ("deposit")
def logoutOperation():
    print ("logout")
def exitOperation():
    print("exit")



#print(generationAccountNumber())
init() 

   


