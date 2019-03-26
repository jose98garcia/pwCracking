#Four Methods for Password Cracking

#Menu for testing
def menu():
    print("Choose a method for password cracking")
    print("-------------------------------------")
    print("1. Password with only lowercase letters")
    print("2. Password with lower and uppercase letters")
    print("3. Password with lower, uppercase letters, and digits")
    print("4. Password with lower, uppercase letters, digits, and symbols")

    option = input()
    option = int(option)

    while((option < 1) or (option > 4)):
        print("That is not an option. Try again.")
        option = input()
        option = int(option)

    return option
#---------------------------------------------------------------------------------------------

def readFile():
    f = open("pwd.txt", "r")
    if(f.mode == "r"):
        contents = f.read()
        return contents
    return 

#---------------------------------------------------------------------------------------------

#Takes you to the right option from menu
def chooseMethod(num):
    if(num == 1):
        methodOne()
    elif(num ==2):
        methodTwo()
    elif(num == 3):
        methodThree()
    elif(num == 4):
        methodFour()
    else:
        print("Invalid method... something went wrong")


#---------------------------------------------------------------------------------------------
#Password with only lowercase letters
def methodOne():
    print("Method one")
    hola = readFile()
    print(hola)

#Password with lower and uppercase letters
def methodTwo():
    print("Method two")

#Password with lower, uppercase letters, and digits
def methodThree():
    print("Method three")

#Password with lower, uppercase letters, digits, and symbols
def methodFour():
    print("Method four")


#---------------------------------------------------------------------------------------------
#Main Program
number = menu()
chooseMethod(number)



    