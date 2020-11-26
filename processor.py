def get_matrix_dimensions() -> tuple:
    dim_x, dim_y = [int(x) for x in input().split()]
    return dim_x, dim_y


def get_matrix_values(dim_x: int) -> list:
    # first get matrix with float values
    f_matrix = [[float(n) for n in input().split()] for rows in range(dim_x)]
    i_matrix = []
    # see if float matrix has integer values, if so, convert to integers
    for row in f_matrix:
        i_matrix.append(list(map(lambda x: int(x) if x.is_integer() else x, row)))
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


def transpose_matrix(dim_A: tuple, mat_A: list) -> list:
    # my first solution using list comprehension
    # mat_T = [[mat_A[y][x] for y in range(dim_A[0])] for x in range(dim_A[1])]
    # second solution using list comprehension, zip and unpacking
    mat_T = [list(n) for n in zip(*mat_A)]
    # another solution using map, list, zip and unpacking
    # mat_T = list(map(list, zip(*mat_A)))
    return mat_T


def print_matrix(matrix: list) -> str:
    result = ''
    for x in matrix:
        row = ' '.join(map(str, x))
        result = f'{result}{row}\n'
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
        # second solution using zip and list comprehension
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
def multiply_matrices_compr(dim_A: tuple, dim_B: tuple, mat_A: list, mat_B:list) -> list:
    if dim_A[1] == dim_B[0]:  # check if amount of columns matrix A and amount of rows matrix B match
        '''
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
    print('Enter size of matrix:')
    dim_A = get_matrix_dimensions()
    print('Enter matrix:')
    mat_A = get_matrix_values(dim_A[0])
    print(print_matrix(transpose_matrix(dim_A, mat_A)))


def choice_sum():
    print('Enter size of first matrix:',)
    dim_A = get_matrix_dimensions()
    print('Enter first matrix:',)
    mat_A = get_matrix_values(dim_A[0])
    print('Enter size of second matrix:',)
    dim_B = get_matrix_dimensions()
    print('Enter second matrix:',)
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


def main_menu():
        print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit')
        choice = int(input('Your choice:'))
        if choice == 1:
            choice_sum()
            return True
        if choice == 2:
            choice_scalar()
            return True
        if choice == 3:
            choice_multiply()
            return True
        if choice == 4:
            choice_transpose()
            return True
        if choice == 0:
            return False


if __name__ == '__main__':
    while main_menu():
        continue
