#working with list
numbers = []

#for loop for number between 1 to 20 inclusive
print("Numbers between 1 to 20 inclusive\n")
for number in range(1,21):
    numbers.append(number)
print (numbers)

#for loop for the odd number between  1 to 20 inclusive
print("Odd numbers between 1 to 20 inclusive\n")
for i in range(2,22,2):
    numbers.remove(i)
print (numbers)

#for loop for multiple of 3 upto 20
print("Table of Three:\n")
for prod in range(1,21):
    print (" 3 * " + str(prod) + " = " + str(prod * 3))

#list of cubes
cubes = []
for i in range(1,11):
    cubes.append(i**3)
print("FROM FOR LOOP:\n")
print (cubes)
#list comprehension
cubes = [num**3 for num in range(1,11)]
print("FROM LIST COMPREHENSION:\n")
print (cubes)
