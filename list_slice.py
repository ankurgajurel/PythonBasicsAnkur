#working with part of the list (which is generally refered as SLICE)
my_foods = ["Pizza",'Burger','Sandwich','Momo','chowmin']

#slicing and printing
print("The First three dishes on the list are : ")
print(my_foods[:3]) #first three

print("The three dishes in the middle are: ")
print(my_foods[1:4]) #three in the middle

print("The last three dishes on the list are: ")
print(my_foods[-3:]) #three at the last


friend_foods = my_foods[:] #making a copy of the list, bear in mind a seperate copy

#following block of codes prove that they are separate

print ("\nMy Favroit foods are: \n")
my_foods.append("Panipuri")
print(my_foods)

print("\n My friend's favroit foods are: \n")
friend_foods.append("Samosa")
print(friend_foods)
