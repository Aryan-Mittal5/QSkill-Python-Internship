import numpy as np

# Function to input a matrix
def input_matrix(name):
    rows = int(input(f"\nEnter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter elements of {name} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


# Function to display matrix
def display_matrix(title, matrix):
    print(f"\n{title}")
    print("-" * 30)
    print(matrix)
    print("-" * 30)


while True:
    print("\n========== MATRIX OPERATIONS TOOL ==========")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    try:
        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A.shape == B.shape:
                display_matrix("Result (A + B)", A + B)
            else:
                print("\nMatrices must have the same dimensions.")

        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A.shape == B.shape:
                display_matrix("Result (A - B)", A - B)
            else:
                print("\nMatrices must have the same dimensions.")

        elif choice == "3":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if A.shape[1] == B.shape[0]:
                display_matrix("Result (A × B)", np.matmul(A, B))
            else:
                print("\nNumber of columns of A must equal number of rows of B.")

        elif choice == "4":
            A = input_matrix("Matrix")

            display_matrix("Transpose", A.T)

        elif choice == "5":
            A = input_matrix("Matrix")

            if A.shape[0] == A.shape[1]:
                det = np.linalg.det(A)
                print("\nDeterminant =", round(det, 2))
            else:
                print("\nDeterminant can only be calculated for a square matrix.")

        elif choice == "6":
            print("\nThank you for using Matrix Operations Tool!")
            break

        else:
            print("\nInvalid choice. Please try again.")

    except Exception as e:
        print("\nError:", e)