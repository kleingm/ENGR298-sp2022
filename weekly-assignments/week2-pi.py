import math


def main():
    """
    Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete,
    return the approximation.
    :return:
    """

    def square(x): return x * x

    # define variables from Gauss Legendre Algorithm
    ao = 1
    bo = 1 / math.sqrt(2)
    to = 1 / 4
    xo = 1
    count = 0
    while count < 10:
        a1 = (ao + bo) / 2
        b1 = math.sqrt(bo * ao)
        t1 = to - (xo * square(ao - a1))
        x1 = (2 * xo)
        pi = (square(a1 + b1)) / (4 * t1)

        print("The value of pi for loop " + str(count) + " is: " + str(pi))
        print("the difference between iteration " + str(count) + " is" + str(math.pi - pi))

        count += 1

        ao = a1
        bo = b1
        to = t1
        xo = x1

    # set pi_estimate to whatever variable you were using for pi
    pi_estimate = pi

    # return the estimated value of pi
    return pi_estimate


if __name__ == "__main__":

    # call the student function
    result = main()

    # print results
    error = abs(math.pi - result)

    # print out the results
    print("You returned the value: ", result)
    print("This has error of: ", error)
    if error < 1E-9:
        print("This is acceptable...")
    else:
        print("The error is too much. Are you looping 10 times?")
