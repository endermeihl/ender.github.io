import math

# Given values
A = 5000000  # Future amount
r = 0.03  # Annual interest rate
n = 1  # Number of times interest applied per time period
t = 20  # Number of time periods the money is invested for

# Calculate P using the annuity compound interest formula
P = A * (r/n) / (math.pow(1 + r/n, n*t) - 1)

print(P)