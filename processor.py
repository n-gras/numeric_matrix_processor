def get_matrix_dimensions() -> tuple:
    dim_x, dim_y = [int(x) for x in input().split()]
    return dim_x, dim_y


def get_matrix_values(dim_x: int) -> list:
    matrix = [[int(n) for n in input().split()] for rows in range(dim_x)]
    return matrix


def sum_matrices(dim_A: tuple, dim_B: tuple, mat_A: list, mat_B:list) -> str:
    if dim_A == dim_B:
        mat_C = [[mat_A[x][y] + mat_B[x][y] for y in range(dim_A[1])] for x in range(dim_A[0])]
        result = ''
        for x in mat_C:
            row = ' '.join(map(str, x))
            result = f'{result}{row}\n'
        return result
    else:
        return 'ERROR'


def scalar_matrix(scalar: int, dim_A: tuple, mat_A:list) -> str:
    mat_S = [[mat_A[x][y] * scalar for y in range(dim_A[1])] for x in range(dim_A[0])]
    result = ''
    for x in mat_S:
        row = ' '.join(map(str, x))
        result = f'{result}{row}\n'
    return result


if __name__ == '__main__':
    dim_A = get_matrix_dimensions()
    mat_A = get_matrix_values(dim_A[0])
    scalar = int(input())
    print(scalar_matrix(scalar, dim_A, mat_A))

