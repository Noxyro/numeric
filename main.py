import numpy as np

# import matplotlib.pyplot as plt

# A = np.array([[1, 2, 3], [3, 4, 5]])
# print(A)
#
# zero_array = np.zeros((3, 3))
# print(zero_array)
#
# ten_array = np.arange(10)
# print(ten_array)
#
# en_array = np.arange(1, 11, 1)
# print(en_array)

# (1 0 0)   (2 4 6)   (x1)   (4)
# (2 1 0) * (0 3 5) * (x2) = (7)
# (3 6 1)   (0 0 6)   (x3)   (-1)
#
#    A         B       X      Y
#         W
#
# Inputs: A, B, Y
# Variablen: X
# Output: W

debug_mode = False


def read_int_number(str_input):
    try:
        _size = int(str_input)  # Convert variable to int

        if _size <= 0:
            print("Number must be greater than 0!")
            return

        return _size
    except ValueError:
        print("Invalid number!")


def split_array(str_array, size):
    _split = str_array.split(" ")  # Splits user input into array with contents between spaces

    _split_len = len(_split)  # Get length of splitted array
    if _split_len < size:
        print("Needs more arguments!")
        return

    if _split_len > size:
        print("More arguments given than needed - clipping last " + str(_split_len - size) + " arguments!")

    return _split


def read_array(str_input, size):
    _split = split_array(str_input, size)  # Read array string into variable

    if _split is None:
        return

    _array = np.empty(size)  # Create array with size of matrix
    _spl = 0  # Define count variable
    while _spl < size:  # Iterate each number in splitted array
        try:
            _array[_spl] = float(_split[_spl].replace(",", "."))  # Convert to float and convert , to .
        except ValueError:
            print("Invalid input at position " + str(_spl))
            _array[_spl] = 0
            return
        _spl += 1

    return _array


def read_matrix(size):
    if size is None:
        read_matrix()

    _matrix_array = [np.empty(size)] * size
    _arr = 0
    while _arr < size:
        print("Enter row " + str(_arr + 1) + ": ")
        _array = None
        while _array is None:
            _array = read_array(input(), size)

        if debug_mode:
            print(_array)
        _matrix_array[_arr] = _array
        _arr += 1

    if debug_mode:
        print(np.array(_matrix_array))

    return np.array(_matrix_array)


def main():
    print("Enter dimensions for both matrices: ")
    _size = read_int_number(input())

    _matrix_left = read_matrix(_size)
    _matrix_right = read_matrix(_size)
    _mult = _matrix_left.dot(_matrix_right)
    print(_mult)


main()
