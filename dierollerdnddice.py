#die roller for dnd 5d4 as example
from random import randint

while True: #always
    try: #in try block to handle errors
        dice = input("What to roll?  \n > ").split('d')  
        # asking for input and splitting the string on the d --- 5d4 example... comes out as a list like [5, 4] 
        rolls = [randint(1, int(dice[1])) #creating 1 die to roll = [starting at 1 to "the 2 number in the list of dice"] == [1, 4]
        for rolls in range(int(dice[0]))] # back to dice list [5, 4] use the first digit as the amount to loop 
        print(f'{sum(rolls)}: {rolls}') #print all of those random numbers added together
    except IndexError: #turns this into a value error
        raise ValueError
    except ValueError: #for when the wrong number or unusable string is put in
        print("Oops!  That was not a valid dice.  ( Try again using the format 1d20 )")


        