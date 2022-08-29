#!/usr/bin/python3

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("{:*^20}".format(name))

if __name__ == '__main__':
    print_hi("WELCOME ADAVA")

#creating a tree, finding its height
#every methodology has been implimented here
#so have a look

#finding tree height
tree_height = input("how tall you want your tree: ")
tree_height = int(tree_height)

#starting spaces for tree
spaces = tree_height - 1

#hashes
hashes = 1

#stump spaces  used later
stumps_spaces = tree_height - 1

while tree_height != 0:

#print spaces
    for i in range(spaces):
        print(' ', end="")

#prints the hashes
    for i in range(hashes):
        print('#', end="")

#newline after each row is printed
    print()

#spaces decremented by 1 each time
    spaces -= 1

#hashes increamented by 2 each time
    hashes += 2

#decrement tree height each time to jump out of loop
    tree_height -= 1

#prints spaces before stumps and then height
for i in range(stumps_spaces):
    print(' ', end="")

print('#')
