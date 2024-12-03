from sys import stdin
from enum import Enum

# Collect the input into a single string (add the endlines at end for padding)
memory = stdin.read() + "\n" * 10

# I do not want to use regex for this.
# Idea: Use something like recursive descent parsing


class Result(Enum):
    Ok = True
    Error = False


nums = {str(i) for i in range(10)}


# Recognize 1-3 digit numbers and return result and next position
def read_num(from_pos: int) -> tuple[Result, int]:
    if memory[from_pos] not in nums:
        return (Result.Error, from_pos + 1)
    for i in range(1, 3):
        if memory[from_pos + i] not in nums:
            return (Result.Ok, from_pos + i)
    return (Result.Ok, from_pos + 3)


# Recognize mul(num1,num2) and return result, next position and multiplied result
def read_mul(from_pos: int) -> tuple[Result, int, int]:
    # Match mul(
    start_pattern = "mul("
    for i in range(4):
        if memory[from_pos + i] != start_pattern[i]:
            return (Result.Error, from_pos + max(1, i), 0)
    curr_pos = from_pos + 4

    # Match num1
    match read_num(curr_pos):
        case (Result.Ok, end_pos):
            num1 = int(memory[curr_pos:end_pos])
            curr_pos = end_pos
        case (Result.Error, end_pos):
            return (Result.Error, end_pos, 0)

    # Match ,
    if not memory[curr_pos] == ",":
        return (Result.Error, curr_pos, 0)
    else:
        curr_pos += 1

    # Match num2
    match read_num(curr_pos):
        case (Result.Ok, end_pos):
            num2 = int(memory[curr_pos:end_pos])
            curr_pos = end_pos
        case (Result.Error, end_pos):
            return (Result.Error, end_pos, 0)

    # Match )
    if not memory[curr_pos] == ")":
        return (Result.Error, curr_pos, 0)
    else:
        curr_pos += 1

    # Match found
    return (Result.Ok, curr_pos, num1 * num2)


# Read do and don't or mul
def read_do_dont(from_pos: int) -> tuple[Result, int, bool]:

    # Match do
    start_pattern = "do"
    for i in range(2):
        if memory[from_pos + i] != start_pattern[i]:
            return (Result.Error, from_pos + 1, False)
    curr_pos = from_pos + 2

    # Now check whether () or 'nt()
    if memory[curr_pos] == "(":
        # Match ()
        start_pattern = "()"
        for i in range(2):
            if memory[curr_pos + i] != start_pattern[i]:
                return (Result.Error, curr_pos + i, False)
        return (Result.Ok, curr_pos + 2, True)
    elif memory[curr_pos] == "n":
        # Match do
        start_pattern = "n't()"
        for i in range(len(start_pattern)):
            if memory[curr_pos + i] != start_pattern[i]:
                return (Result.Error, curr_pos + i, False)
        return (Result.Ok, curr_pos + len(start_pattern), False)
    else:
        return (Result.Error, curr_pos, False)


# Find all vaild mul operations
def read_memory() -> int:
    curr_pos = 0
    sm = 0
    num = 0
    do = True
    while curr_pos < len(memory):
        # Is it start of do or don't?
        if memory[curr_pos] == "d":
            result, curr_pos, todo = read_do_dont(curr_pos)
            if result.value:
                do = todo
        elif memory[curr_pos] == "m" and do:
            _, curr_pos, num = read_mul(curr_pos)
            sm += num
        else:
            curr_pos += 1
    return sm


print(read_memory())
