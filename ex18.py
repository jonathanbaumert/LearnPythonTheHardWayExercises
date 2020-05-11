def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes just one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

def printNone():
    print("I got nothing")

print_two("Zed","Shaw")
print_two_again("Zed2","Shaw2")
print_one("First!")
printNone()