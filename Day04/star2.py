from sys import stdin

# Read in the input and set the rows and column number
word_search = []
for line in stdin:
    word_search.append([i for i in line.strip()])
rows = len(word_search)
cols = len(word_search[0])
# Add a padding of 4 chars on all of left and right side
# Like so:
# word_ aaaa
# searchaaaa
# aaaaaaaaaa
# aaaaaaaaaa
# aaaaaaaaaa
# aaaaaaaaaa
# First pad the columns, by adding 4 rows
for i in range(4):
    pad = ["a"] * cols
    word_search.append(pad)

# Now pad all the rows, including the newly added one
for row in word_search:
    row.extend(["a"] * 4)

# Now, we look for the MAS in X shape, cenntered at each position in the input array
# First what are the relative postions to look at for a given ceter?
deltas_list = [[(1, 1), (0, 0), (-1, -1)], [(1, -1), (0, 0), (-1, 1)]]
# Now for each position, we looks in the diagonals for "MAS"
pattern = "MAS"
match_count = 0
for row in range(rows):
    for col in range(cols):
        for deltas in deltas_list:
            word = ""
            for delta_x, delta_y in deltas:
                word += word_search[row + delta_x][col + delta_y]
            if word != pattern and word[::-1] != pattern:
                break
        else:
            match_count += 1
print(match_count)
