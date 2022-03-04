# bring in randomness cause we need it in our lives
import random
from statistics import stdev

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# generate two random lists of integers
max_length = 1000; upper_bound=1000000
A = generate_random_int_list(max_length, upper_bound)

B = generate_random_int_list(max_length, upper_bound)

# The two lists are samples from a random distribution.
# Print out whether List A or B has the larger standard deviation.
# use if statements
if stdev(A) > stdev(B):
    print("List A has a larger standard deviation than list B")
if stdev(A) == stdev(B):
    print("List A's standard deviation is equal to List B's standard deviation")
if stdev(A) < stdev(B):
    print("List B has a larger standard deviation than list A")

print("List A's standard deviation is " + str(stdev(A)))
print("List B's standard deviation is " + str(stdev(B)))

# Food for thought: consider how a distribution comparison could be used to determine
# if a machine or process is out of specification? A simple t-test can be used to see
# if processes/results are “different” from one another. How might an engineer utilize this information?