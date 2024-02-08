# Matrix Multiplication

matrix_A_rows = int(input('Enter number of rows for matrix-A: '))
matrix_A_cols  = int(input('Enter number of columns for matrix-A: '))


matrix_B_rows = int(input('\nEnter number of rows for matrix-B: '))
matrix_B_cols  = int(input('Enter number of columns for matrix-B: '))

if matrix_A_cols == matrix_B_rows:

    # matrix_A = [[int(input(f"column {j+1} -> Enter {i+1} element:")) for j in range(matrix_A_cols)] for i in range(matrix_A_rows) ]
    print('\nEnter values for matrix A: ')
    matrix_A = []
    for i in range(matrix_A_rows):
        row = []
        for j in range(matrix_A_cols):
            element = int(input(f"column {j+1} -> Enter {i+1} element: "))
            row.append(element)
        matrix_A.append(row)

    # matrix_B = [[int(input(f"column {j+1} -> Enter {i+1} element:")) for j in range(matrix_B_cols)] for i in range(matrix_B_rows) ]

    print('\nEnter values for matrix B: ')
    matrix_B = []
    for i in range(matrix_B_rows):
        row = []
        for j in range(matrix_B_cols):
            element = int(input(f"column {j+1} -> Enter {i+1} element: "))
            row.append(element)
        matrix_B.append(row)

    print('\nMatrix-A: ')
    for i in matrix_A:
        print(i)

    print('\nMatrix-B: ')
    for i in matrix_B:
        print(i)

    # result = [[0 for j in range(matrix_B_cols)] for i in range(matrix_A_rows)]

    result = []
    for i in range(matrix_A_rows):
        row = []
        for j in range(matrix_B_cols):
            row.append(0)
        result.append(row)


    # main logic for matrix multiplication (multiplication operation)
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
        

    print('\nMultiplication of Matrix-A and Matrix-B is: ')
    for i in result:  #print result
        print(i)
else:
    print('Multiplication of matrices is not possible (columns of matrix-A = row of matrix-B)')    

