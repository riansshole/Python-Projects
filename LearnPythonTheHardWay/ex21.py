def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just function!")

age = add(float(input("Any number:\n")), float(input("Any number:\n")))
height = subtract(float(input("Any number:\n")), float(input("Any number:\n")))
weight = multiply(float(input("Any number:\n")), float(input("Any number:\n")))
iq = divide(float(input("Any number:\n")), float(input("Any number:\n")))

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")
print("\n")
#little puzzle for brain tease
print("Here's a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That becomes ", what, "Can you do it by hands?")