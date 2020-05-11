def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxesOfCrackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheeseAndCrackers(20,30)

print("Or, we can use cariables from our script:")
amtOfCheese = 10
amtofCrackers = 50

cheeseAndCrackers(amtOfCheese,amtofCrackers)

cheeseAndCrackers(10+20,5+6)

cheeseAndCrackers(amtOfCheese+100,amtofCrackers*10)

