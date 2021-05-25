i = 10
number = []
def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
    return total

while i < 100000000:
    i *= 2
    number.append(i)

print("The number: ")
for num in number:
    print(num)

print("The sum of my list is: ", sum(number))