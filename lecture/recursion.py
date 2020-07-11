# fn which prints every number from N to zero
# def print_numbers(n):
# for i in range(n, 0, -1):
# print(i)

def print_num(num):
    print(num)
    # a base case (i.e the code that tells us to stop running this function)
    if num == 0:
        return

    # recursive case (i.e the case which takes us to the next subproblem)
    print_num(n - 1)
    return


print_num(4)


def double_print_num(n):
    print(n)
    if n == 0:
        return

    double_print_num(n - 1)
    double_print_num(n - 1)
    return


double_print_num(3)
