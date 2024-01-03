# matrix multiplication interface

import numpy as np 

# i hat column
def i_hat(dimension):
    i_hat = []
    for i in range(dimension):
        entry = int(input(f'i hat entry {i + 1}: '))
        i_hat.append(entry)
    return i_hat

# j hat column
def j_hat(dimension):
    j_hat= []
    for i in range(dimension):
        entry = int(input(f'j hat column entry {i + 1}: '))
        j_hat.append(entry)
    return j_hat

# k hat column
def k_hat(dimension):
    k_hat= []
    for i in range(dimension):
        entry = int(input(f'j hat column entry {i + 1}: '))
        j_hat.append(entry)
    return j_hat

# main function
def main():
    SCOPE_DIMENSION = int(input('Matrix dimension: '))

    if SCOPE_DIMENSION == 2:
        i = i_hat(SCOPE_DIMENSION)
        j = j_hat(SCOPE_DIMENSION)
    else:
        i = i_hat(SCOPE_DIMENSION)
        j = j_hat(SCOPE_DIMENSION)
        k = k_hat(SCOPE_DIMENSION)

# main execution
if __name__ == '__main__':
    main()