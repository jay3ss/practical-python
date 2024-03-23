# pcost.py
#
# Exercise 1.27
# Exercise 1.27: Reading a data file

# Now that you know how to read a file, let’s write a program to perform a simple
# calculation.

# The columns in portfolio.csv correspond to the stock name, number of shares, and
# purchase price of a single stock holding. Write a program called pcost.py that opens
# this file, reads all lines, and calculates how much it cost to purchase all of the
#  in the portfolio.

# Hint: to convert a string to an integer, use int(s). To convert a string to a floating
# point, use float(s).

# Your program should print output such as the following:

# Total cost 44671.15
with open("Data/portfolio.csv") as f:
    data = f.read().split("\n")[1:]


total = 0
for line in data[:-1]:
    _, shares, cost = line.split(",")
    total += int(shares) * float(cost.replace("\n", ""))

print("Total cost", total)
