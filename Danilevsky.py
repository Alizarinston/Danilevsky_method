# coding: utf8
from numpy import array, dot, identity, set_printoptions
from time import time

'''A = array([[6.26, 1.10, 0.98, 1.25],
           [1.10, 4.16, 1.00, 0.16],
           [0.98, 1.00, 5.44, 2.12],
           [1.25, 0.16, 2.12, 6.00]])'''

A = array([[2.2, 1, 0.5, 2],
           [1, 1.3, 2, 1],
           [0.5, 2, 0.5, 1.6],
           [2, 1, 1.6, 2]])


def danilevsky(input_matrix=A, iter=0, show=False):

    # m_matrix
    k = 2
    for i in range(len(input_matrix)):
        matrix = identity(len(input_matrix))
        for j in range(len(input_matrix)):
            matrix[k, j] = -((input_matrix[len(input_matrix) - (i + 1)][j])/(input_matrix[len(input_matrix)
                                                                                          - (i + 1)][k]))
            if j == k:
                matrix[k][j] = 1/(input_matrix[len(input_matrix) - (i + 1)][j])

        k -= 1
        if k == -2:
            break

        if show and iter == 1:
            if i == 0:
                print("\nM1:\n", matrix)
        elif show and iter == 2:
            if i == 1:
                print("\nM2:\n", matrix)
        elif show and iter == 3:
            if i == 2:
                print("\nM3:\n", matrix)

        if i == 0:
            v_1 = matrix
        elif i == 1:
            v_2 = matrix
        elif i == 2:
            v_3 = matrix

    # m'_matrix
    k = 2
    for i in range(len(input_matrix)):
        matrix = identity(len(input_matrix))
        for j in range(len(input_matrix)):
            matrix[k, j] = (input_matrix[len(input_matrix) - (i + 1)][j])
            if j == k:
                matrix[k][j] = (input_matrix[len(input_matrix) - (i + 1)][j])
        k -= 1
        if k == -2:
            break

        if show and iter == 1:
            if i == 0:
                print("\nM1':\n", matrix)
        elif show and iter == 2:
            if i == 1:
                print("\nM2':\n", matrix)
        elif show and iter == 3:
            if i == 2:
                print("\nM3':\n", matrix)

        if i == 0:
            u_1 = matrix
        elif i == 1:
            u_2 = matrix
        elif i == 2:
            u_3 = matrix

    mam_matrix_1 = dot(u_1, dot(input_matrix, v_1))
    mam_matrix_2 = dot(u_2, dot(mam_matrix_1, v_2))
    mam_matrix_3 = dot(u_3, dot(mam_matrix_2, v_3))

    if iter == 1 and show is False:
        return mam_matrix_1
    elif iter == 2 and show is False:
        return mam_matrix_2
    elif iter == 3 and show is False:
        return mam_matrix_3
    else:
        return "\n---------"

A_1 = danilevsky(A, iter=1, show=False)
A_2 = danilevsky(A_1, iter=2, show=False)
A_3 = danilevsky(A_2, iter=3, show=False)


def m_iter(it=1, sh=True):

    if it == 1:
        print(danilevsky(A, iter=1, show=sh))
    elif it == 2:
        print(danilevsky(A_1, iter=2, show=sh))
    elif it == 3:
        print(danilevsky(A_2, iter=3, show=sh))


def frobenius_form(input_matrix=A_3):

    print("\nFrobenius:\n", input_matrix)

if __name__ == '__main__':
    start = time()
    set_printoptions(suppress=True, precision=6)

    # m_iter(1)               # an argument is the iteration number of the matrices M and M' you want to see
    frobenius_form()

    print('\nWork time:', round(time() - start, 5), 's')
