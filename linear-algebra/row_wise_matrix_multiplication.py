# row wise matrix multiplication

import numpy as np

def row_one(dimension):
    row_one = []
    for i in range(dimension):
        entry = int(input(f'Row one entry {i + 1}: '))
        row_one.append(entry)
    return row_one

def row_two(dimension):
    row_two = []
    for i in range(dimension):
        entry = int(input(f'Row two entry {i + 1}: '))
        row_two.append(entry)
    return row_two

def row_three(dimension):
    row_three = []
    for i in range(dimension):
        entry = int(input(f'Row three entry {i + 1}: '))
        row_three.append(entry)
    return row_three

def multiply(mat1, mat2):
    return np.matmul(mat1, mat2)

def matrix_initiation():
    DIMENSION = int(input('Matrix dimension: '))

    if DIMENSION == 2:
        row_1 = row_one(DIMENSION)
        row_2 = row_two(DIMENSION)
        matrix = np.array([row_1,
                           row_2])
        return matrix
    elif DIMENSION == 3:
        row_1 = row_one(DIMENSION)
        row_2 = row_two(DIMENSION)
        row_3 = row_three(DIMENSION)
        matrix = np.array([row_1,
                           row_2,
                           row_3])
        return matrix
    else:
        print('This comuptational tool can only compute 2x2 and 3x3 matrices')

    
# main function
def main():
    matrix_1 = matrix_initiation()
    matrix_2 = matrix_initiation()    

    print(multiply(matrix_1, matrix_2))


# main execution
if __name__ == '__main__':
    main()