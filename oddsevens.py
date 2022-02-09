# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# generate two random lists of integers
max_length = 100; upper_bound=1000000
nums = generate_random_int_list(max_length, upper_bound)

# see how long this list is
print("The list contains "+str(len(nums))+" values total.")
# create odd and even counter
odd = 0
even = 0
# create for loop that divides each number by two
# if the remainder is 0, the number is even, if not, it is odd.
for x in nums:
    if (x % 2) == 0:
        even += 1
    else:
        odd += 1

print("The list contains " + str(odd) + " odd values")
print("The list contains " + str(even) + " even values")
print("odd numbers make up " + str((odd / len(nums))*100) + " percent of the list")
print("even numbers make up " + str((even / len(nums))*100) + " percent of the list")