the_count  = [1,2,3,4,5,6,7,8,9,10]
fruits = ['apple','banana','orange','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is the count {number}")
    
print("\n")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
    
print("\n")

#same as above
for i in change :
    print(f"I got {i}")
    
print("\n")

# we can build list, start with empty

elements = []
for i in range (0, 6): elements.append(i)

# now we print them out
for i in elements:
    print(f"Element was: {i}")