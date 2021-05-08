import copy
import math
import sys

def add(a, b):
    matrix = []
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        matrix.append(row)
    return matrix

def scalar(s, a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] *= s
    return a

def mul(a, b):
    matrix = []
    if len(a[0]) != len(b):
        return None
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            element = 0
            for k in range(len(a[0])):
                element += a[i][k] * b[k][j]
            row.append(element)
        matrix.append(row)
    return matrix

def transpose(a):
    matrix = []
    for j in range(len(a[0])):
        row = []
        for i in range(len(a)):
            row.append(a[i][j])
        matrix.append(row)
    return matrix 

def transpose_sidediagonal(a):
    matrix = transpose(a)
    return transpose_horizontal(transpose_vertical(matrix))

def transpose_horizontal(a):
    matrix = []
    for i in range(len(a)):
        matrix.append(a[len(a) - i - 1])
    return matrix

def transpose_vertical(a):
    matrix = copy.deepcopy(a)
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix

def determinant(a):
    if len(a) != len(a[0]):
        return None

    if len(a) == 1:
        return a[0][0]

    det = 0
    for j in range(len(a[0])):
        det += a[0][j] * cofactor(a, 0, j)
    return det

def minor(a, i, j):
    matrix = []
    for r in range(0, len(a)):
        if r == i:
            continue
        row = []
        for c in range(0, len(a[0])):
            if c != j:
                row.append(a[r][c])
        matrix.append(row)
    return determinant(matrix)

def cofactor(a, i, j):
    return minor(a, i, j) * (-1) ** (i + j)

def inverse(a):
    det = determinant(a)
    if det == None or det == 0:
        return None
    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(cofactor(a, i, j))
        c.append(row)
    ct = transpose(c)
    return scalar(1 / float(det), ct)

def get_matrix(order):
    nm = input(f"Enter size of {order} matrix: ").split()
    n = int(nm[0])
    m = int(nm[1])
    print(f"Enter {order} matrix:")
    matrix = []
    for i in range(n):
        row = input().split()
        for j in range(m):
            row[j] = float(row[j])
            if row[j].is_integer():
                row[j] = int(row[j])
        matrix.append(row)
    return matrix

def print_result(a):
    if a is None:
        print("The operation cannot be performed.")
        return
    print("The result is:")
    for i in range(len(a)):
        row = ""
        for j in range(len(a[0])):
            if j > 0:
                row += " "
            row += format(a[i][j])
        print(row)

def format(num):
    if is_integer(num):
        return str(num)
    if num > 0:
        num += sys.float_info.epsilon
        return cut_p0(str(math.floor(num * 100) / 100))
    elif num < 0:
        num -= sys.float_info.epsilon
        return cut_p0(str(-math.floor(abs(num) * 100) / 100))
    else:
        return "0"

def cut_p0(num_str):
    if num_str.endswith(".0"):
        return num_str[0:len(num_str) - 2]
    return num_str

def is_integer(num):
    if type(num) == "<class int>":
        return True
    return False

def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    return int(input("Your choice: "))

def add_matrix():
    a = get_matrix("first")
    b = get_matrix("second")
    c = add(a, b)
    print_result(c)

def mul_matrix():
    a = get_matrix("first")
    b = get_matrix("second")
    c = mul(a, b)
    print_result(c)

def scalar_matrix():
    a = get_matrix("\b")
    s = float(input("Enter constant: "))
    scalar(s, a)
    print_result(a)

def transpose_matrix():
    print()
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    menuno = int(input("Your choice: "))
    a = get_matrix("\b")
    if menuno == 1:
        b = transpose(a)
    elif menuno == 2:
        b = transpose_sidediagonal(a)
    elif menuno == 3:
        b = transpose_vertical(a)
    elif menuno == 4:
        b = transpose_horizontal(a)
    print_result(b)

def determinant_matrix():
    a = get_matrix("\b")
    det = determinant(a)
    print_result([[det]])

def inverse_matrix():
    a = get_matrix("\b")
    b = inverse(a)
    print_result(b)

while True:
    menuno = menu()
    if menuno == 1:
        add_matrix()
    elif menuno == 2:
        scalar_matrix()
    elif menuno == 3:
        mul_matrix()
    elif menuno == 4:
        transpose_matrix()
    elif menuno == 5:
        determinant_matrix()
    elif menuno == 6:
        inverse_matrix()
    elif menuno == 0:
        break
    print()
