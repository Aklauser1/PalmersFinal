import random as rgen


#found this handy compact opener on the interwebs 
appleList = open("appleFile.txt").read().splitlines()
bananaList = open("bananaFile.txt").read().splitlines()
kiwiList = open("kiwiFile.txt").read().splitlines()
tomatoList = open("tomatoFile.txt").read().splitlines()
grapeList = open("grapeFile.txt").read().splitlines()


#Prints out my welcome menu for my program 
def menu():
    print("  * * * * * WELCOME * * * * * ")
    print(" A Fruit a Day Keeps Palmer Away")
    print("Fruits that are currently available")
    print("           Apple")
    print("           Banana")
    print("           Grape")
    print("           Kiwi")
    print("           Tomato")


#checks to see if the user input is a fruit that we currently have available
def correctFruit():
    #makes fruitChosen a global variable so it can be accessed in other functions 
    global fruitChosen
    #added .lower() to make it easier for the user
    fruitChosen = input("Which type of Fruit would you like? ").lower()
    while True:
        if fruitChosen == "apple" or fruitChosen == "banana" or fruitChosen == "kiwi" or fruitChosen == "tomato" or fruitChosen == "grape":
            break
        print("Please select a fruit that is currently available")
        #added .lower() to make it easier for the user 
        fruitChosen = input("Which type of Fruit would you like? ").lower()
        
        
#checks to see if month is a valid month        
def correctMonth():
    #makes monthChosen and daysInMonth global variables so they can be accessed anywhere 
    global monthChosen
    global daysInMonth
    #added .lower() to make it easier for the user 
    monthChosen = input("Which month will you be eating {}s in? ".format(fruitChosen)).lower()
    #checks to make sure the input is a valid month 
    while True:
        if monthChosen == "january" or monthChosen == "march" or monthChosen == "may" or monthChosen == "july" or monthChosen == "august" or monthChosen == "october" or monthChosen == "december":
            #assigns month with 31 days 
            daysInMonth = 31
            break
        elif monthChosen == "april" or monthChosen == "june" or monthChosen == "september" or monthChosen == "november":
            #assigns month with 30 days 
            daysInMonth = 30
            break
        elif monthChosen == "february":
            #assigns month with 28 days 
            daysInMonth = 28
            break
        #if not valid month, it asks again for the full name of the month 
        print("Please type in the full name of the valid month.")
        # added .lower() to make it easier for the user 
        monthChosen = input("Which month will you be eating {}s in? ".format(fruitChosen)).lower()
        
        
#created a function that takes the coresponding Fruit List and prints a different random type each day in the month 
def randomizer(fruitList):
     for days in range(1,daysInMonth + 1):
        listCount = len(fruitList)
        place = rgen.randint(0, (listCount) - 1)
        dailyFruit = fruitList[place]
        print("Day {0}: {1}". format(days, dailyFruit))
        fruitList.pop(place)


#creates a random fruit type for each day of the given month for the given fruit
def randomFruits():
    #if the chosen fruit was apple
    if fruitChosen == "apple":
       randomizer(appleList)
    #if the chosen fruit was banana        
    elif fruitChosen == "banana":
        randomizer(bananaList)
    #if the chosen fruit was a kiwi
    elif fruitChosen == "kiwi":
        randomizer(kiwiList)
    #if the chosen fruit was a tomato
    elif fruitChosen == "tomato":
        randomizer(tomatoList)
    #if the chosed fruit was a grape
    elif fruitChosen == "grape":
        randomizer(grapeList)
            
            
def main():
    #calls the menu
    menu()
    #gets the correct fruit input
    correctFruit()
    #gets the correct month input
    correctMonth()
    #creates random fruit types for the days in given month 
    randomFruits()
    
main()