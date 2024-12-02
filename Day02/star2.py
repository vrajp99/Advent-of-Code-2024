from sys import stdin

# Get the input
reports = []
for line in stdin:
    report = [int(i) for i in line.strip().split()]
    reports.append(report)


# Function to classify a report as safe or unsafe:
def is_report_safe(report):
    # Report with 0 or 1 level is always safe
    if len(report) <= 1:
        return True

    # Check whether tentatively increasing or decreasing
    is_increasing = (report[-1] - report[0]) >= 0

    # Set difference range based on increasing or decreasing
    if is_increasing:
        diff_min = 1
        diff_max = 3
    else:
        diff_min = -3
        diff_max = -1

    # Check adjacent elements of report
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff > diff_max or diff < diff_min:
            return False
    return True


# Check if report is safe with Problem Dampner:
def is_report_dampened_safe(report):
    # Remove each element and try for safety
    # If already safe with not dampening, will be safe with dampening when you
    # remove first element
    for i in range(len(report)):
        report_dampened = report[:i] + report[i + 1 :]
        if is_report_safe(report_dampened):
            return True
    return False


# Now find reports safe with dampening and count them
num_safe = sum(map(is_report_dampened_safe, reports))
print(num_safe)
