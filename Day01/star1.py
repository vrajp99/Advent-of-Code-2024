from sys import stdin

# Read in inputs to 2 lists
list1 = []
list2 = []
for line in stdin:
    l, r = [int(i) for i in line.strip().split()]
    list1.append(l)
    list2.append(r)

# Sort to math up both lists
list1.sort()
list2.sort()

# Sum over absolute value of difference
diff = 0
for l, r in zip(list1, list2):
    diff += abs(l - r)
print(diff)
