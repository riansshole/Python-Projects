from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print(f"If you don't want it to be erase, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN/ENTER")
input("> ")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for four lines!")

line1 = input("Line 1 > ")
line2 = input("Line 2 > ")
line3 = input("Line 3 > ")
line4 = input("Line 4 > ")

print("Now I'm going to write these into the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
target.write(line4)

print("And finally we're done. I'm gonna close it.")
target.close()