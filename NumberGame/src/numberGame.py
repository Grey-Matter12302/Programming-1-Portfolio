import random
a = random.randrange(1,100)

def nubmerGame():
    test = input("Enter an integer between 1-100:")
    print (test)
    if int(test) > a:
        print("Sorry that number is too high, please try again")
        
    elif int(test) < a:
        print("Sorry that number is too low, please try again")
    
    elif int(test) == a:
        print ("You Got it!")
            
while True:
    nubmerGame()
