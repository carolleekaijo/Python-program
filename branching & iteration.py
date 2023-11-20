
a = 1
b = 2

if a==b:
    print('yes')


else:
    print('no')    

i = 1

while (i<=10):
    print(i)
    i+=1
    if i ==5:
        print('exit')
        break
j = 'this show that iteration will stop when i = 5'
print(j)

import os
#mac 
os.system('clear') 
#window
#os.system('cls') 

# List of integers
numbers = [1, 2, 3, 4, 5, 6]
# For loop to iterate through the list
for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")

print('This show the iteration of loop in the list')



# List of integers
numbers = [1, 2, 3, 4, 5, 6]
totalnumber = len(numbers)
print(totalnumber) 
# For loop to iterate through the list
for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")

print('This show the iteration of loop in the list')

i=0
while i<totalnumber:
    sq = numbers[i]
    i+=1
    print(sq)

# List of integers
numbers = [1, 2, 3, 4, 5, 6]

# For loop to go through each element in the list
for num in numbers:
    # If-else statement to determine if a number is even or odd
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

print('This show the iteration of for loop in the list and utilized if else conditions')


