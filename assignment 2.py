'''
#1. Write a program to take a number input from the user and display whether the number is even or odd.
number =  5 

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#2. Write a program that prompts the user for two integer values and displays the results of the first number divided by the second, with exactly two decimal places displayed.

import math
a=int(input("\n 2. ENTER A NUM:"))
b=int(input("ENTER A NUM:"))
cal=a/b
ans=round(cal,2)
print(ans)

''
#3. Write a program that will convert Celsius value to Fahrenheit.

C=float(input("\n 3. ENTER TEMP:"))
cal=(C*9/5)+32
F=int(cal)
print("THE REQUIRED FAHRENHEIT:",F,"*F")

''
#4.Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from the user as input.
import math
a1=float(input("4.\nEnter the x-coordinate of the first point:"))
b1=float(input("enter the y-coordinate of the first point: "))
a2=float(input("Enter the x-coordinate of the second point: "))
b2=float(input("enter the y-coordinate of the second point: "))
distance=maths.sqrt((a2-a1)**2+(b2-b1)**2)
print (f"The Euclidean distance between 2 coordinates is: {distance:.2f} \n")
''

#5. Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.
p=int(input("\n 5.ENTER PRINCIPLE:"))
t=int(input("ENTER TIME:"))
r=int(input("ENTER RATE:"))
SI=(p*t*r)/100
print(SI)
''

#6.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2000 (both included).
n={num for num in range(1500,2000) if num % 7 == 0 and num % 5 == 0}
print(f"6. \n Number which are divisible by 7 and multiple by 5, between 1500 and 2000(both included) is: {n} \n")

''
#7.Write a Python program that accepts a string and calculates the number of digits and letters.
data=input("7. \nEnter a string vaue: ")
letter=sum(char.isalpha() for char in data)
digit=sum(char.isdigit() for char in data)
print(f"Number of letters in string: (letter) \nNumber of digits in string: (digit) \n")
'''
#8.Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
#I. The program should generate a random number for the answer.
#II. The program should prompt the user for a number input.
#III. The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
#IV. The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
#V. If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.

import random
ans=random.randint(-1000,1000)
trial=5
print("8.\nNUMBER GUESSING GAME")
print("Try to guess the number that has been randomly choosen .\n")
print{"You are given 5 chances to guess the number correctly.\n"}
for i in range(trial):
    guess=int(input("Enter you number: "))
    if guess == ans:
        print("Correct guess! You win the game.")
        break
    elif guess<ans:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    remaining_trails = trail - (i + 1)
    if remaining_trails > 0:
        print(f"You have {remaining_trials} chances left.")
        else:
            print(f"Game Over! The correct number was (ans).")
        
