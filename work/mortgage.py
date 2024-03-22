# mortgage.py
#
# Exercise 1.7
# Dave’s mortgage

# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with
# Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest
# rate is 5% and the monthly payment is $2684.11.

# Here is a program that calculates the total amount that Dave will have to pay over
# the life of the mortgage:

# Exercise 1.8: Extra payments

# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# Modify the program to incorporate this extra payment and have it print the total
# amount paid along with the number of months required.

# When you run the new program, it should report a total payment of 929,965.62 over 342 months

# Exercise 1.9: Making an Extra Payment Calculator

# Modify the program so that extra payment information can be more generally handled. Make
# it so that the user can set these variables:

# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000

# Make the program look at these variables and calculate the total paid appropriately.

# How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first
# five years have already been paid?

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        addl_payment = extra_payment
    else:
        addl_payment = 0

    principal = principal * (1 + rate / 12) - payment - addl_payment
    total_paid = total_paid + payment + addl_payment

print("Total paid", total_paid, "for", months, "months")
