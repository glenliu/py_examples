# encoding UTF-8


def is_prime(number):
    i = 2

    while i < number:
        print(i)
        if number % i == 0:
            print("feile, she is heshu"+"\tIt can be divided by:"+str(i))
            return "heshu"
        i += 1

    return "sushu"


print(is_prime(10))