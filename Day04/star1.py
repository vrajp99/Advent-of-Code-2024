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

# Now, we look for the word, starting from each position in the input array
# First what are the stepping directions possible?
steps = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if (i, j) != (0, 0):
            steps.append((i, j))
# Now for each position, we looks in all directions for "XMAS"
pattern = "XMAS"
match_count = 0
for row in range(rows):
    for col in range(cols):
        for step_x, step_y in steps:
            curr_x = row
            curr_y = col
            for letter in pattern:
                if word_search[curr_x][curr_y] != letter:
                    break
                else:
                    curr_x += step_x
                    curr_y += step_y
            else:
                match_count += 1

print(match_count)
