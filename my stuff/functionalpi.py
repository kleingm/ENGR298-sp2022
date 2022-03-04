import math


def functionalpi(i):
    """
    :param i: desired error of the functional pi
    :return: calculated pi within margin of error
    """
    def square(x): return x * x
    # define variables from Gauss Legendre Algorithm
    ao = 1
    bo = 1 / math.sqrt(2)
    to = 1 / 4
    xo = 1
    count = 0
    while (count < 10):
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


# main (body) here to call your function. Do not modify below this line
desired_error = 1E-10

approximation = functionalpi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
