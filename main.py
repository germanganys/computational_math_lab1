import copy
from typing import List

EPS = 0.0000000001


# Получаем минор
def minor(matrix: List[List[float]], i, j):
    buff = copy.deepcopy(matrix)
    buff = buff[:i] + buff[i + 1:]
    for row in buff:
        row.pop(j)
    return buff


# Детерминант
def det(matrix: List[List[float]]):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    s = 0
    for i in range(n):
        m = minor(matrix, 0, i)
        s += (-1 ** i) * matrix[0][i] * det(m)
    return s


# Прямая прогонка
def forward_step(matrix: List[List[float]], b: List[List[float]], k: int):
    n = len(matrix)
    a = matrix[k][k]

    for i in range(k + 1, n):
        _a = matrix[i][k]
        matrix[i][k] = 0
        for j in range(k + 1, n):
            if abs(a) < EPS:
                print('Система не совместна')
                exit(0)
            matrix[i][j] += -_a / a * matrix[k][j]
        b[i][0] += -_a / a * b[k][0]


# Обратная прогонка
def find_answer(matrix: List[List[float]], b: List[List[float]], ans: List[float]):
    for i in reversed(range(len(matrix))):
        if abs(matrix[i][i]) < EPS:
            print('Система не совместна')
            exit(0)

        if i == len(matrix) - 1:
            ans[i] = b[i][0] / matrix[i][i]
        else:
            s = b[i][0]
            for j in range(i + 1, len(matrix)):
                s -= matrix[i][j] * ans[j]
            ans[i] = s / matrix[i][i]


if __name__ == '__main__':

    DEBUG = False

    if DEBUG:
        matrix = [[3, 2, -5, 7, 1],
                  [2, -1, 3, 4, 3],
                  [1, 2, -1, 8, 6],
                  [3, 4, 2, 9, -2],
                  [6, 3, 6, 1, 8]]
        b = [[-1],
             [13],
             [9],
             [10],
             [1]]
    else:
        is_file_input = input('Считываем из файла или с терминала [Y/*]: ') == 'Y'

        if is_file_input:
            filename = input('Введите имя файла: ')
            with open(filename) as file:
                n = int(file.readline())
                matrix = [list(map(float, file.readline().split())) for i in range(n)]
                b = [[float(x)] for x in file.readline().split()]
        else:
            n = int(input('Введите размерность:'))
            matrix = [list(map(float, input('(через пробел)>>').split())) for i in range(n)]
            b = [[float(x)] for x in input('B (через пробел):').split()]
    ans = [0.0 for i in range(len(b))]

    # Массив перестановок xi
    indexes = [i for i in range(len(b))]

    mat = copy.deepcopy(matrix)
    b_cp = copy.deepcopy(b)
    for k in range(len(b) - 1):
        max_abs, max_idx = -1, -1
        for i in range(k, len(b)):
            if max_abs < abs(mat[k][i]):
                max_abs = abs(mat[k][i])
                max_idx = i
        for i in range(len(mat)):
            mat[i][k], mat[i][max_idx] = mat[i][max_idx], mat[i][k]

        indexes[k], indexes[max_idx] = indexes[max_idx], indexes[k]
        forward_step(mat, b, k)

    find_answer(mat, b, ans)

    # Переставляем в нужном порядке
    final_ans = [0.0 for i in range(len(b))]

    for i in range(len(mat)):
        for j in range(len(mat)):
            if indexes[j] == i:
                final_ans[i] = ans[j]

    r = [0.0 for i in range(len(b))]

    # Вычисляем вектор невязок
    for i in range(len(b)):
        A = 0
        for idx, a in enumerate(matrix[i]):
            A += a * final_ans[idx]
        r[i] = A - b_cp[i][0]

    print('Матрица: \n' + '\n'.join(str(row) for row in mat))
    print('Найденные коэфф.: ' + str(final_ans))
    print('Вектор неувязок: ' + str(r))
