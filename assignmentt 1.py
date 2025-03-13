#1. The perimeter of a rectangle with length 9 & width 6

length = 9
width = 6

perimeter = 2*(length + width)

print(f"\n 1.  The perimeter of the rectangle with length {length} and width {width} is {perimeter} units. \n")
      


#2. Python is great, it's wild!

print("2.  Python is great, it's wild! \n")



#3. 2 to the 10th power

''' This program calculates 2 raised to the power of 10.'''

result = 2**10

print(f"3.  2 to the power of 10 is{result}. \n")



#4. 7 factorial minus 5 factorial

'''This program calculates the difference between 7 factorial and 5 factorial.'''

import math

result = math.factorial(7) - math.factorial(5)

print(f"4.  7 factorial minus 5 factorial is {result}. \n")



#5. Your forename multiplied by 5

'''This program repeats the user's forename 5 times.'''

forename = "Sadikshya"

print(f"5.  Your forename multiplied by 5 is: {forename * 5}. \n")



#6. Your name left justified with 15 spaces

'''This program left justifies the user's name with 15 space'''

name = "Sadikshya"

print(f"6.  Left-justified name: {name.ljust(15)}" )
print("\n")


#7. PI to 5 decimal places

'''This program displays the vallue of PI to 5 decimal places.'''

import math
  
print(f"7.   PI to 5 decimal places is {math.pi:.5f}. \n")



#8.  200 modulus 12

'''This program calculates the modulus when 200 is divided by 12.'''

result = 200 % 12

print(f"8.  200 modulus 12 is {result}. \n")



#9.  7.2 as an integer value

'''This program convertsthe float value 7.2 to an integer.'''

result = int(7.2)

print(f"9.  The integer value of 7.2 is {result}. \n")



#10.  The unicode encoding for your name

'''This program displays the unicode encoding for each character in the user's name.'''

name ="Sadikshya"

unicode_values = [ord(char) for char in name]
print(f"10.   The unicode encoding for each character in '{name}' is: {unicode_values}. \n")
