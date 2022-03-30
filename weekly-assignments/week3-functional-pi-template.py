import math


def calculate_pi(target_error):
    """ Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

        :param target_error: Desired error for PI estimation
        :return: Approximation of PI to specified error bound
        """

    def square(x): return x * x

    # define variables from Gauss Legendre Algorithm
    ao = 1
    bo = 1 / math.sqrt(2)
    to = 1 / 4
    p = 1


    # main (body) here to call your function. Do not modify below this line
    target_error = 1E-10

    # keep track of current approximation and error
    approx = 0
    current_error = 100
    count = 0
    # loop while your current error is larger than the target
    while abs(current_error) > target_error:
        a1 = (ao + bo) / 2
        b1 = math.sqrt(bo * ao)
        t1 = to - (p * square(ao - a1))
        p1 = (2 * p)
        pi = (square(a1 + b1)) / (4 * t1)

        current_error = abs(math.pi - pi)
        count += 1
        print("The value of pi for loop " + str(count) + " is: " + str(pi))
        print("the difference between iteration " + str(count) + " is" + str(math.pi - pi))

        ao=a1
        bo=b1
        to=t1
        p=p1

    # calculate approximation
    approx = pi


    return approx


if __name__ == "__main__":
    # main (body) here to call your function. Do not modify below this line
    desired_error = 1E-10

    approximation = calculate_pi(desired_error)

    print("Solution returned PI=", approximation)

    error = abs(math.pi - approximation)

    if error < abs(desired_error):
        print("Solution is acceptable")
    else:
        print("Solution is not acceptable")
