from sys import stdin
from collections import defaultdict

# Read in the data, first the contraints,
# the once we hit a newline, switch to the lists
constraints = defaultdict(set)
list_of_pages = []
newline_seen = False
for line in stdin:
    line_str = line.strip()
    if not newline_seen and len(line_str) == 0:
        newline_seen = True
        continue  # Switch and so not process empty line further
    if newline_seen:
        pages = [int(i) for i in line_str.split(",")]
        list_of_pages.append(pages)
    else:
        page_num1, page_num2 = [int(i) for i in line_str.split("|")]
        constraints[page_num1].add(page_num2)

# For each list of pages, for each page, check the contraint
# satisfaction with all pages that follows
unsat_sorted_mid_sum = 0
for pages in list_of_pages:
    num_pages = len(pages)
    for page_idx, page in enumerate(pages):
        for page_idx_2_chk in range(page_idx + 1, num_pages):
            if pages[page_idx_2_chk] not in constraints[page]:
                break
        else:
            # If we do not find any violation of constraints for current
            # page, move to next page
            continue
        # Otherwise, stop checking since there is a violation
        break
    else:
        # If all pairs are ok the we don't need to make any changes
        # to ordering
        continue
    # Since given lists are small, just use insertion sort
    # while using the contraints for comparision
    for page_idx in range(1, num_pages):
        curr_page = pages[page_idx]
        for move_idx in range(page_idx - 1, -1, -1):
            if pages[move_idx] in constraints[curr_page]:
                pages[move_idx + 1] = pages[move_idx]
            else:
                pages[move_idx + 1] = curr_page
                break
        else:
            pages[0] = curr_page
    # Sum up mid
    unsat_sorted_mid_sum += pages[num_pages // 2]

print(unsat_sorted_mid_sum)
