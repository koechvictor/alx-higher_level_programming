#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for val in range(len(matrix[row])):
            if (val != len(matrix[row]) - 1):
                print("{:d}".format(matrix[row][val]), end=" ")
            else:
                print("{:d}".format(matrix[row][val]), end="")
        print()
