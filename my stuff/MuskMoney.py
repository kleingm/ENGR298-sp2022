# Problem 1: Recently, Elon Musk sold $1.02 Billion in TSLA shares
# If he placed the entire sale in US Treasury Bonds,
# what would the sale be worth after 10 years? 20 years? Ignore capital gains taxes and highly paid accountants.
# Interest after 10 years with $1.02 billion initial deposit
principal = 1020000000
rate = 1.850
n = 0
while n < 10:
    n = n + 1
    A = principal * (1+rate/100)**n

print("Initial principal is $" + str(principal))
print("Interest rate is " + str(rate / 100))
print("Hold for " + str(n) + " years")
print("The sale would be worth $" + str(A) + " in 10 years")

# Interest after 10 years with $1.02 billion initial deposit
principal = 1020000000
rate = 2.220
n = 0
while n < 20:
    n = n + 1
    T = principal * (1+rate/100)**n

print("Initial principal is $" + str(principal))
print("Interest rate is " + str(rate / 100))
print("Hold for " + str(n) + " years")
print("The sale would be worth $" + str(T) + " in 20 years")


# Food for thought: If Musk placed the entire sale in US Treasury Bonds and lived off the interest alone,
# what would be his annual income?
# print("If Musk placed the entire sale in US Treasury Bonds and lived off the interest alone,"
# print("his annual income would be" + str)
# print("The return in 10 years is $" + str(round(A-1020000000, 2)))
# print("The return in 20 years is $" + str(round(T-1020000000, 2)))
# Food for thought : Assuming university endowment contributions ≥$1M earn 5% year,
# how large a gift to JMU is required to fund 1x student scholarship perpetually?
