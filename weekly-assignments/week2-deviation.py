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


def main(list_A, list_B):
    """
    Examine list_A and list_B. Determine which has the largest standard deviation and return it as largest_list

    :param list_A: A list of random integers
    :param list_B: A list of random integers
    :return: The list that has the greatest standard deviation
    """

    # iterate through each list and determine which one has the largest value
    # depending on which one you find, set it equal to "largest_list"
    largest_list = []


    # The two lists are samples from a random distribution.
    # Print out whether List A or B has the larger standard deviation.
    # use if statements
    if stdev(list_A) > stdev(list_B):
       largest_list = list_A
    else:
       largest_list = list_B

    print("List A's standard deviation is " + str(stdev(list_A)))
    print("List B's standard deviation is " + str(stdev(list_B)))

    # do not modify this line
    return largest_list


if __name__ == "__main__":
    # generate two random lists of integers
    max_length = 10
    upper_bound = 100
    A = generate_random_int_list(max_length, upper_bound)

    B = generate_random_int_list(max_length, upper_bound)

    result = main(A, B)

    print("Your code was passed two lists, A:", A, " and B: ", B)

    if result == A:
        print("You reported list A has the largest standard deviation. Use your calculator to check :) ")
    elif result == B:
        print("You reported list B has the largest standard deviation. Use your calculator to check :) ")
    else:
        print("You returned something than either list... Are you updating the largest_list variable? "
              "Did you modify the return line?")
