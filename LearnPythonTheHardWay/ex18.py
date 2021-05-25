#this one is like your script with argv
def print_five(*args):
    arg1,arg2,arg3,arg4,arg5,arg6 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}, arg5: {arg5}, arg6: {arg6}")

#ok, that args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this will only take 1 argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this will print no argument at all
def print_none():
    print(f"I got nothing")

print_five('one', 'two', 'three', 'four', 'five', 'six')
print_two_again('one','two')
print_one('first!')
print_none()