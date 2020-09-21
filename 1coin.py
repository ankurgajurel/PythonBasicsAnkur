import random
import time
from collections import Counter

print("0 for heads and 1 for tails")

coinVal = random.randint(0, 1)

time.sleep(1)

memeCountr = Counter.copy(coinVal) 

print("Tossed", coinVal)

time.sleep(1.5)

print(memeCountr)