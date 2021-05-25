from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print(f"Copying from {fromfile} to {tofile}")

#we could do these two on one line, how?
infile = open(fromfile)
indata = infile.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(tofile)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(tofile, 'w')
out_file.write(indata)

print("Alright all done.")

out_file.close()
infile.close()
