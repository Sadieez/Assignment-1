#1. Write a function that accepts a string and calculate the number of upper case letters and lower case letters.

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return {"Uppercase Letters": upper_count, "Lowercase Letters": lower_count}

get user input
user_input = input("Enter a string: ")
print(count_case(user_input))


'''
#2. Write a function to check whether the given number is prime or not.

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")


#3. Write a function to check whether the given number is Armstrong or not.

def is_armstrong(number
    Convert the number to a string to easily get the digits
    num_str = str(number)
    
    Get the number of digits
    num_digits = len(num_str)
    
    Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    '''
'''Check if the sum is equal to the original number
    return sum_of_powers == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


#4. Write a function to accept a list of names and return the sorted order of names back.

def sort_names(names):
     '''Sort the list of names in alphabetical order'''
    return sorted(names)

names_list = input("Enter a list of names separated by commas: ").split(',')
sorted_names = sort_names(names_list)

print("Sorted names:", sorted_names)


#5. Create a program called calculator with functions to perform the following arithmetic calculations, each should take two decimal parameters and return the result of the arithmetic 
#calculation in question. 
#A. Addition                 #B. Subtraction 
#C. Multiplication           #D. Division 
#E. Truncated division       #F. Modulus 
#G. Exponentiation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def truncated_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Division by zero"

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero"

def exponentiate(a, b):
    return a ** b

'''Main function to perform all operations at once'''
def calculator():
    print("Enter two decimal numbers: ")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    print(f"\nResults for numbers {a} and {b}:")
    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    print(f"Division: {a} / {b} = {divide(a, b)}")
    print(f"Truncated Division: {a} // {b} = {truncated_divide(a, b)}")
    print(f"Modulus: {a} % {b} = {modulus(a, b)}")
    print(f"Exponentiation: {a} ** {b} = {exponentiate(a, b)}")
    
calculator()





#6.  Write a program that prompts the user for a series of integers and stores in a list only the values between 1-100, and displays the resulting list. 

def filter_integers():
   
    valid_numbers = []
    
    print("Enter integers one by one. Type 'done' to stop.")
    
    while True:
        user_input = input("Enter an integer: ")
        
        '''Check if the user wants to stop the input'''
        if user_input.lower() == 'done':
            break
        
        '''Try to convert the input to an integer and check if it's in the range of 1-100'''
        try:
            number = int(user_input)
            if 1 <= number <= 100:
                valid_numbers.append(number)
            else:
                print("Number is not between 1 and 100. It will be ignored.")
        except ValueError:
            print("That's not a valid integer. Please try again.")
    
   
    print(f"Valid numbers between 1 and 100: {valid_numbers}")


filter_integers()



#7.  Write a program that prompts the user to enter a list of names and store them in a list. The program should display how many times the letter 'a appears within the list.  

def count_a_in_names():
    '''Create an empty list to store the names'''
    names = []

    print("Enter names one by one. Type 'done' to stop.")
    
    while True:
        name = input("Enter a name: ")

        ''' If the user types 'done', stop the input process'''
        if name.lower() == 'done':
            break
        
        names.append(name)
    
    '''Count how many times the letter 'a' appears in the list'''
    count_a = sum(name.lower().count('a') for name in names)

    print(f"The letter 'a' appears {count_a} times in the list of names.")


count_a_in_names()



#8.  Write a program that prompts the user to enter integer values to populate two lists, then prints messages to determine the following:  
#(a) Whether the lists are of the same length.  
#(b) Whether the elements in each list sum to the same value.  
#(c) Whether there are any values that occur in both lists 

def compare_lists():
    list1 = []
    list2 = []
    
   
    print("Enter integers for the first list (type 'done' to stop):")
    while True:
        user_input = input("Enter an integer for list1: ")
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            list1.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
   
    print("Enter integers for the second list (type 'done' to stop):")
    while True:
        user_input = input("Enter an integer for list2: ")
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            list2.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    '''(a) Check if both lists are of the same length'''
    if len(list1) == len(list2):
        print("The lists are of the same length.")
    else:
        print("The lists are of different lengths.")
    
    '''(b) Check if the elements in each list sum to the same value'''
    if sum(list1) == sum(list2):
        print("The sums of both lists are equal.")
    else:
        print("The sums of the lists are not equal.")
    
    '''(c) Check if there are any values that occur in both lists'''
    common_elements = set(list1) & set(list2)
    if common_elements:
        print(f"There are common values in both lists: {common_elements}")
    else:
        print("There are no common values in the lists.")


compare_lists()



#9. Write a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day 
#   of the week for the recorded temperature. The function should then add the temperature to the dictionary only if it does not already contain a temperature for that day. The function should 
#   return the resulting dictionary, whether it is updated or not.


def add_daily_temp(temp_dict, temp_value, day_of_week):
    ''' Check if the day already has a recorded temperature'''
    if day_of_week not in temp_dict:
        '''Add the temperature for the given day if it's not already there'''
        temp_dict[day_of_week] = temp_value
    else:
        print(f"Temperature for {day_of_week} already recorded.")
    
    '''Return the resulting dictionary'''
    return temp_dicttemperatures = {}
    temperatures = add_daily_temp(temperatures, 72, 'Monday')
    temperatures = add_daily_temp(temperatures, 68, 'Tuesday')
    temperatures = add_daily_temp(temperatures, 75, 'Monday')  

print(temperatures)




#10. Write a function named get_daily_temps that prompts the user for the average temperature for each day of the week and returns a dictionary containing the in  formation the user entered.

def get_daily_temps():
    '''Initialize an empty dictionary to store the temperatures'''
    daily_temps = {}
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
     '''Loop through each day and prompt the user for the temperature'''
    for day in days_of_week:
        while True:
            temp_value = input(f"Enter the average temperature for {day}: ")
            try:
                
                temp_value = float(temp_value)
                
                daily_temps[day] = temp_value
                break  
            except ValueError:
                print("Invalid temperature value. Please enter a valid number.")
    
     '''Return the dictionary containing the temperatures for each day'''
    return daily_temps


daily_temperatures = get_daily_temps()
print("\nRecorded temperatures for the week:")
print(daily_temperatures)



#11. Create three dictionaries: 
#    dic1 = {1:10, 2:20} 
#    dic2 = {3:30, 4:40} 
#    dic3 = {5:50, 6:60} 
#   (a) Write code to concatenate these dictionaries to create a new one. Create a variable called nums to store the resulting dictionary.  
#   (b) Write code to add a new key/value pair to the dictionary nums: (7, 70) 
#   (c) Write code to update the value of the item with key 3 in nums to 80 
#   (d) Write code to remove the third item from dictionary nums. 
#   (e) Write code to sum all the items in the dictionary nums 
#   (f) Write code to multiply all the items in the dictionary nums 
#   (g) Write code to retrieve the maximum and minimum values in nums. 


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

'''Create a new dictionary nums by merging all three dictionaries'''
nums = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", nums)

''' (b) Add a new key/value pair (7, 70)'''
nums[7] = 70
print("After adding (7, 70):", nums)

'''(c) Update the value of the item with key 3 to 80'''
nums[3] = 80
print("After updating key 3 to 80:", nums)

'''(d) Remove the third item from dictionary nums (third insertion order)'''
third_key = list(nums.keys())[2]  
del nums[third_key]
print("After removing the third item:", nums)

'''(e) Sum all the values in nums'''
sum_values = sum(nums.values())
print("Sum of all values in nums:", sum_values)

'''(f) Multiply all the values in nums'''
product = 1
for value in nums.values():
    product *= value
print("Product of all values in nums:", product)

'''(g) Retrieve the maximum and minimum values in nums'''
max_value = max(nums.values())
min_value = min(nums.values())
print("Maximum value in nums:", max_value)
print("Minimum value in nums:", min_value)




#12. Create two sets: set1 = {20, 40, 60} set2 = {10, 20, 30, 40, 50, 60} 
#    (a) Write code to perform a union of these sets. Print the length of the resulting set. 
#    (b) Write code to perform an intersection of set1 and set2. 
#    (c) Write code to compute the symmetric difference between set1 and set2 
#    (d) Write code to add the value 40 to set1, did the set change? 
#    (e) Write code to remove value 20 from set2.


set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

'''(a) Perform union of set1 and set2 and print the length'''
union_set = set1 | set2  # or set1.union(set2)
print("Union of set1 and set2:", union_set)
print("Length of union set:", len(union_set))


'''(b) Perform intersection of set1 and set2'''
intersection_set = set1 & set2  # or set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)


'''(c) Compute symmetric difference between set1 and set2'''
symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_diff)


'''(d) Add the value 40 to set1, check if the set changes'''
before_add = set1.copy()  
set1.add(40)  
set_changed = before_add != set1  # Check if set1 changed
print("After adding 40 to set1:", set1)
print("Did set1 change?", set_changed)

''' (e) Remove value 20 from set2'''

set2.discard(20)  '''Using discard to avoid errors if the value doesn't exist'''
print("After removing 20 from set2:", set2)




#13. Create a function called word_intersection that prompts the user for two English words, and displays which letters the two words have in common.


def word_intersection():
   
    word1 = input("Enter the first word: ").lower()
    word2 = input("Enter the second word: ").lower()

 '''Convert words to sets of letters and find the intersection'''
    common_letters = set(word1) & set(word2)

 '''Display the common letters'''
    if common_letters:
        print("Common letters:", ", ".join(sorted(common_letters)))
    else:
        print("No common letters found.")

word_intersection()
