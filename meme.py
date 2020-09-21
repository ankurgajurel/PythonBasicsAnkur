class Robot:
    def __init__(self, n, w):
        self.name = n
        self.weight = w

    def introduc_self(self):
        print("My name is " + self.name + "and I am " + self.weight)

r1 = Robot("Ankur", 55)
r2 = Robot("Aakriti", 80)

