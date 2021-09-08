from datetime import datetime
time = datetime.now()
while True:
    userInput = input("Please enter a number: ")
    userInput2 = input("Please enter a second number: ")
    try:
        inputSum = (int(userInput) + int(userInput2))
    except ValueError as e:
        print("Please ensure you enter numbers")
        file = open ('testfile.txt', mode = 'a')
        file.write(str(e) + " | " + str(time) + "\n" )
        file.close()
    else:
        print(inputSum)
        break




