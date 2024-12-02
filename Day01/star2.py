from sys import stdin
from collections import Counter

# Read in inputs to 2 lists
list1 = []
list2 = []
for line in stdin:
    l, r = [int(i) for i in line.strip().split()]
    list1.append(l)
    list2.append(r)

# Get counts of numbers in list2
list2_counts = Counter(list2)

# Now calculate the similarity
sim = 0
for num in list1:
    sim += num * list2_counts[num]
print(sim)
