def get_matrix_dimensions() -> tuple:
    dim_x, dim_y = [int(x) for x in input().split()]
    return dim_x, dim_y


def get_matrix_values(dim_x: int) -> list:
    # first get matrix with float values
    # f_matrix = [[float(n) for n in input().split()] for rows in range(dim_x)]
    # i_matrix = []
    # see if float matrix has integer values, if so, convert to integers
    # for row in f_matrix:
    #    i_matrix.append(list(map(lambda x: int(x) if x.is_integer() else x, row)))
    # list comprehension version:
    # i_matrix = [[int(x) if x.is_integer() else x for x in row] for row in f_matrix]
    # two-in-one version: - can't pass string representation of float into int(), therefore int(float(x))
    i_matrix = [[int(float(x)) if float(x).is_integer() else float(x) for x in input().split()] for rows in range(dim_x)]
    return i_matrix


def sum_matrices(dim_A: tuple, dim_B: tuple, mat_A: list, mat_B: list) -> list:
    if dim_A == dim_B:
        mat_C = [[mat_A[x][y] + mat_B[x][y] for y in range(dim_A[1])] for x in range(dim_A[0])]
        return mat_C
    else:
        return ['The operation cannot be performed']


def scalar_matrix(scalar: int, dim_A: tuple, mat_A: list) -> list:
    mat_S = [[mat_A[x][y] * scalar for y in range(dim_A[1])] for x in range(dim_A[0])]
    return mat_S


def transpose_main_diag(dim_A: tuple, mat_A: list) -> list:
    '''
    my first solution using list comprehension:
    mat_T = [[mat_A[y][x] for y in range(dim_A[0])] for x in range(dim_A[1])]
    another solution using map, list, zip and unpacking:
    mat_T = list(map(list, zip(*mat_A)))
    a solution using list comprehension, zip and unpacking:
    '''
    mat_T = [list(n) for n in zip(*mat_A)]
    return mat_T


def transpose_side_diag(dim_A: tuple, mat_A: list) -> list:
    '''
    using own functions creatively:
    mat_T = transpose_main_diag(dim_A, transpose_vertical(dim_A, transpose_horizontal(dim_A, mat_A)))
    ----------------------------
    reversing the method in main_diag, executed while slicing from the end instead of the beginning:
    mat_T = reversed([list(n) for n in zip(*mat_A[::-1])])
    ----------------------------
    using list, map, zip, unpacking arguments and reversed, while slicing from the end:
    '''
    mat_T = list(reversed(list(map(list, zip(*mat_A[::-1])))))
    return mat_T


def transpose_horizontal(dim_A: tuple, mat_A: list) -> list:
    # step through the matrix in reverse, row by row
    mat_T = mat_A[::-1]
    return mat_T


def transpose_vertical(dim_A: tuple, mat_A: list) -> list:
    # mat_T = [[mat_A[x][dim_A[1] - (y + 1)] for y in range(dim_A[1])] for x in range(dim_A[0])]
    # or, much easier:
    # mat_T = [[col for col in reversed(row)] for row in mat_A]
    # or just step through the columns of the matrix in reverse, row by row
    mat_T = [row[::-1] for row in mat_A]
    return mat_T


def print_matrix(matrix: list) -> str:
    result = 'The result is:\n'
    for row in range(len(matrix)):
        line = ''
        for col in matrix[row]:
            if isinstance(col, int) or float('{:.2f}'.format(col)).is_integer():
                num = '{:5.0f}'.format(round(col, 0) + 0) # add 0 to eliminate minus sign (-0)
            elif (float('{:.2f}'.format(col)) * 100) % 10 == 0:
                num = '{:5.1f}'.format(col)
            else:
                num = '{:5.2f}'.format(col)
            line = f'{line} {num}'
        result = f'{result}{line}\n'
    return result


def multiply_matrices(dim_A: tuple, dim_B: tuple, mat_A: list, mat_B:list) -> list:
    if dim_A[1] == dim_B[0]:
        mat_C = []
        '''
        first solution
        for row_a in range(dim_A[0]):
            add_row = []
            for col_b in range(dim_B[1]):
                result = 0
                for col_a in range(dim_A[1]):
                    result += mat_A[row_a][col_a] * mat_B[col_a][col_b]
                add_row.append(result)
            mat_C.append(add_row)
        '''
        # second solution using zip and some list comprehension
        for row_a in mat_A:
            add_row = []
            # zip(*mat_B) transposes B and returns iterable zip object, so turning cols into rows
            for col_b in zip(*mat_B):
                # zip(row, col) matches rows of matrix A with rows of transposed matrix B
                add_row.append(sum([x * y for (x, y) in zip(row_a, col_b)]))
            mat_C.append(add_row)
        return mat_C
    else:
        return ['The operation cannot be performed', ]


# this is the list comprehension version of multiply matrix, based on for-loop solution above
def multiply_matrices_compr(dim_A: tuple, dim_B: tuple, mat_A: list, mat_B: list) -> list:
    if dim_A[1] == dim_B[0]:  # check if amount of columns matrix A and amount of rows matrix B match
        '''
        Mat_C = []
        Building up to single line list comprehension:
        for row_a in range(dim_A[0]):
            add_row = []
            for col_b in range(dim_B[1]):
                result = sum([mat_A[row_a][col_a] * mat_B[col_a][col_b] for col_a in range(dim_A[1])])
                add_row.append(result)
            mat_C.append(add_row)
        ----------------------------------
        mat_C = []
        for row_a in range(dim_A[0]):
            add_row = [sum([mat_A[row_a][col_a] * mat_B[col_a][col_b] for col_a in range(dim_A[1])]) for col_b in range(dim_B[1])]
            mat_C.append(add_row)            
        ----------------------------------
        mat_C = [[sum([mat_A[row_a][col_a] * mat_B[col_a][col_b] for col_a in range(dim_A[1])]) for col_b in range(dim_B[1])] for row_a in range(dim_A[0])]
        ----------------------------------
        Much easier to understand version, using zip and unpacking:
        mat_C = []
        for row_a in mat_A:
            add_row = [sum([a * b for (a, b) in zip(row_a, col_b)]) for col_b in zip(*mat_B)]
            mat_C.append(add_row)
        '''
        # final solution, fully contained in one list comprehension, using zip and unpacking :)
        mat_C = [[sum([a * b for (a, b) in zip(row_a, col_b)]) for col_b in zip(*mat_B)] for row_a in mat_A]
        return mat_C
    else:
        return ['The operation cannot be performed', ]

def determinant(matrix: list) -> float:
    size = len(matrix)
    if size == 2:  # base case for determinant
        a, b = matrix[0]
        c, d = matrix[1]
        det = (a * d) - (b * c)
        return det
    elif size == 1:  # if matrix has only 1 element, that element is the determinant
        return matrix[0][0]
    else:
        subtotal = 0
        # this solves the determinant using Laplace expansion along first column of (sub)matrix
        for count, row in enumerate(matrix):
            submatrix = [row[1:] for row in matrix]  # create submatrix where current column is deleted
            del submatrix[count]  # also delete current row
            # recursive function call
            subtotal += row[0] * ((-1) ** count) * determinant(submatrix)
        return subtotal


def matrix_minor(matrix: list) -> list:
    # check if the Matrix is square
    if len(matrix) == len(matrix[0]):
        '''
        My first attempt, using for loops:
        ----------------------
        minor_matrix = create_matrix((len(matrix), len(matrix[0])))
        for i in range(len(matrix)):
            submatrix = matrix[:]
            del submatrix[i]
            for j in range(len(matrix[0])):
                subsub = [row[0:j] + row[j+1:] for row in submatrix]
                minor_matrix[i][j] = determinant(subsub)
        ----------------------
        The final list comprehension version, all in 1 line. This one took some effort to get right :)
        '''
        minor_matrix = [[determinant([row[0:j] + row[j+1:] for row in (matrix[0:i] + matrix[i+1:])]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return minor_matrix

def matrix_cofactor(matrix: list) -> list:
    # list comprehension turning Minor Matrix into Cofactor Matrix
    cof_matrix = [[((-1) ** (count_x + count_y)) * y for count_y, y in enumerate(matrix[count_x])] for count_x in range(len(matrix))]
    return cof_matrix

def inverse_matrix(matrix: list) -> list:
    dimensions = len(matrix), len(matrix[0])
    det = determinant(matrix)
    # check that Matrix determinant is square, and non-zero (Matrix with zero determinant has no inverse
    if (dimensions[0] == dimensions[1]) and det!= 0:
        # inverse of Matrix is (1 / det(Matrix)) * transposed Cofactor Matrix
        inverse = scalar_matrix(1/det, dimensions, transpose_main_diag(dimensions, matrix_cofactor(matrix_minor(matrix))))
        # this is a 'hack' to pass the test that truncates 0.6666666 to 0.66 instead of rounding to 0.67
        return [[int(col * 100) / 100 for col in row] for row in inverse]
    else:
        return ['This matrix doesn\'t have an inverse', ]


def create_matrix(dim_A: tuple) -> list:
    rows = dim_A[0]
    cols = dim_A[1]
    matrix = []
    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            matrix[-1].append(0)
    return matrix


def choice_transpose():
    while True:
        print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\n5. Back')
        t_choice = int(input('Your choice:'))
        if t_choice == 5:
            break
        elif t_choice not in (1, 2, 3, 4):
            print('Invalid choice.')
            continue
        print('Enter size of matrix:')
        dim_A = (5, 5)
        dim_A = get_matrix_dimensions()
        print('Enter matrix:')
        mat_A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        mat_A = get_matrix_values(dim_A[0])
        if t_choice == 1:
            print(print_matrix(transpose_main_diag(dim_A, mat_A)))
            break
        elif t_choice == 2:
            print(print_matrix(transpose_side_diag(dim_A, mat_A)))
            break
        elif t_choice == 3:
            print(print_matrix(transpose_vertical(dim_A, mat_A)))
            break
        elif t_choice == 4:
            print(print_matrix(transpose_horizontal(dim_A, mat_A)))
            break


def choice_sum():
    print('Enter size of first matrix:',)
    dim_A = (3, 3)
    dim_A = get_matrix_dimensions()
    print('Enter first matrix:',)
    mat_A = [[1, -4.3333, 3.2], [2.009, 3, 4.555555], [1.1111, 2, 1]]
    mat_A = get_matrix_values(dim_A[0])
    print('Enter size of second matrix:',)
    dim_B = (3, 3)
    dim_B = get_matrix_dimensions()
    print('Enter second matrix:',)
    mat_B = [[1, 2.3333, 3.2], [2.00, -3, 4.555555], [1.1111, 2, 1.077]]
    mat_B = get_matrix_values(dim_B[0])
    print(print_matrix(sum_matrices(dim_A, dim_B, mat_A, mat_B)))


def choice_scalar():
    print('Enter size of matrix:')
    dim_A = get_matrix_dimensions()
    print('Enter matrix:')
    mat_A = get_matrix_values(dim_A[0])
    print('Enter constant:')
    scalar = int(input())
    print(print_matrix(scalar_matrix(scalar, dim_A, mat_A)))


def choice_multiply():
    print('Enter size of first matrix:',)
    dim_A = (2, 2)
    dim_A = get_matrix_dimensions()
    print('Enter first matrix:',)
    mat_A = [[1, 2], [3, 4]]
    mat_A = get_matrix_values(dim_A[0])
    print('Enter size of second matrix:',)
    dim_B = (2, 2)
    dim_B = get_matrix_dimensions()
    print('Enter second matrix:',)
    mat_B = [[5, 6], [7, 8]]
    mat_B = get_matrix_values(dim_B[0])
    print(print_matrix(multiply_matrices_compr(dim_A, dim_B, mat_A, mat_B)))


def choice_determinant():
    print('Enter size of matrix:',)
    dim_A = (3, 3)
    dim_A = get_matrix_dimensions()
    print('Enter matrix:',)
    mat_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat_A = get_matrix_values(dim_A[0])
    print(f'The result is:\n{determinant(mat_A)}\n')


def choice_inverse():
    print('Enter size of matrix:',)
    dim_A = (3, 3)
    dim_A = get_matrix_dimensions()
    print('Enter matrix:',)
    mat_A = [[2, 1, 3, 4], [4, 5, 2, 1], [1, 3, 4, 1], [2, 5, 1, 3]]
    mat_A = get_matrix_values(dim_A[0])
    print(print_matrix(inverse_matrix(mat_A)))


def main_menu() -> bool:
        print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n'
              '5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
        choice = int(input('Your choice:'))
        if choice == 1:
            choice_sum()
            return True
        elif choice == 2:
            choice_scalar()
            return True
        elif choice == 3:
            choice_multiply()
            return True
        elif choice == 4:
            choice_transpose()
            return True
        elif choice == 5:
            choice_determinant()
            return True
        elif choice == 6:
            choice_inverse()
            return True
        elif choice == 0:
            return False
        else:
            print('Invalid choice.')
            return True


if __name__ == '__main__':
    while main_menu():
        continue
