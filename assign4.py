
"""

Teresa Henderson
CST 100 - Bansal
06/08/2016

assign4.py

Part 1:  Prints sequences of numbers as strings

Author's Comments:

I used a lot of arbitrary letter variables for
Part 1.  I didn't see the point of making them very descriptive
since they are counters.  Variables
used for specific purposes are named for
their function.

"""

# Part 1: a
print("Assignment Part 1a")
for i in range(10):
    print(" ")
    for j in range(10):
        print(j, end=" ")

print("\n\nAssignment Part 1b")

# Part 1: b1
for k in range(10):
    print(" ")
    print(k, end=" ")
    for l in range(10):
        print(k, end=" ")

print("\n\nAssignment Part 2b")

# Part 1: b2
for m in range(11):
    print(" ")
    for n in range(m):
        print(n, end=" ")

print("\n\nAssignment Part 1c: Extra Credit\n")

# Part 1: Extra Credit

# setup a list to store numbers in
store = []
# give starting number for the list
s = 10
# for a range of 1 to 10
for r in range(1, 10, 1):
    # nested for each item in the range
    for c in range(0, r, 1):
        store.append(s+c)
    # print the output of store without list brackets
    print(", ".join(str(e) for e in store))
    # for each number, add the number of rows
    # e.g. row 1 has 1 added to it, row 2 has 2 added to it, etc.
    s += r
    # reset store for the next run through
    store = []



