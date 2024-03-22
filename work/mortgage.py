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

# Exercise 1.10: Making a table

# Modify the program to print out a table showing the month, total paid so far, and the remaining
# principal. The output should look something like this:

# 1 2684.11 499399.22
# 2 5368.22 498795.94
# 3 8052.33 498190.15
# 4 10736.44 497581.83
# 5 13420.55 496970.98
# ...
# 308 874705.88 3478.83
# 309 877389.99 809.21
# 310 880074.1 -1871.53
# Total paid 880074.1
# Months 310

# Exercise 1.11: Bonus

# While you’re at it, fix the program to correct for the overpayment that occurs in the last month.


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

# while principal > 0:
#     months += 1
#     if extra_payment_start_month <= months <= extra_payment_end_month:
#         addl_payment = extra_payment
#     else:
#         addl_payment = 0

#     principal = principal * (1 + rate / 12) - payment - addl_payment
#     total_paid = total_paid + payment + addl_payment

#     print(months, round(total_paid, 2), round(principal, 2))


while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        addl_payment = extra_payment
    else:
        addl_payment = 0

    this_months_payment = payment + addl_payment

    if principal - this_months_payment < 0:
        principal = 0
    else:
        principal = principal * (1 + rate / 12) - this_months_payment
    total_paid = total_paid + this_months_payment

    print(f"{months:<4} {total_paid:8.2f} {principal:>8.2f}")

print(f"Total paid: ${total_paid:.2f}")
print("Months", months)
