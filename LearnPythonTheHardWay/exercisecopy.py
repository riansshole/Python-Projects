from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print(f"Copying content from {fromfile} to {tofile}")

infile = open(fromfile)
indata = infile.read()

print(f"The data from {fromfile} is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(tofile)}")
print(f"Ready. Press RETURN to copy data or CTRL-C to abort: ")
input("> ")

outfile = open(tofile, 'w')
outfile.write(indata)

print(f"Done.")

outfile.close()
infile.close()