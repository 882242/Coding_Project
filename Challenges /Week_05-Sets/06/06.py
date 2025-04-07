#____________________________________________________________________________________
#   Purpose: Create a set and freeze it, then confirm it is frozen by trying to modify it
#   Author: Felix       Date: April 7, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

FrozenSet = frozenset([1, 2, 3])
print(FrozenSet)

FrozenSet.add(4) #attempt to add 4