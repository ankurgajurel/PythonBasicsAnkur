import random

c = 0

d = 0

for i in range(100):
    a = random.randint(0, 1)
    
    print(a)
    
    if a == 0:
        c += 1
        
    else:
        d += 1
        
if c > d:
    print("The taken side is heads")
    
else:
    print("The taken side is tails")