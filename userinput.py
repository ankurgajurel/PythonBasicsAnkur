import time

time.sleep(2)
car = input("What Kind of rental car do you like : ")
time.sleep(1)
print ("Let me check if we have a " + car)
time.sleep(5)
print("I am sorry, we don't have one")

time.sleep(1)
member = int(input("How many people are in your dinner group: " ))
print ("Let me see!")

time.sleep(3)

if(member >= 8) :
    print ("I am sorry!, you need to wait for sometime.")
else :
    print("I have got a table for you.")
    time.sleep(1)
    print("Right this way sir!!!")
