#____________________________________________________________________________________
#   Purpose: Create a set and unionize, difference the set
#   Author: Felix       Date: April 2, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

Fruits1 = {'apple', 'banana', 'orange', 'strawberry'}

Fruits2 = {'Kiwi', 'Pineapple', 'Coconut', 'Mango'}

AllFruits1 = Fruits1.union(Fruits2)
print(AllFruits1)

FruitDifference = Fruits1.difference(Fruits2)
print(FruitDifference)

AllFruits2 = Fruits2.union(Fruits1)
print(AllFruits2)

FruitDifference1 = Fruits2.difference(Fruits1)
print(FruitDifference1)

Numbers1 = {1,2,3,4}
Numbers2 = {4,5,6,7}

AllNumbers1 = Numbers1.union(Numbers2)
print(AllNumbers1)
NumbersDifference = Numbers1.difference(Numbers2)
NumbersDifference2 = Numbers2.difference(Numbers1)
print(NumbersDifference2, NumbersDifference)
