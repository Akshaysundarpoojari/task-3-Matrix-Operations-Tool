import numpy as np

def get_matrix(rows, cols):
    print(f"\nEnter {rows * cols} elements:")
    elements = list(map(float, input().split()))

    if len(elements) != rows * cols:
        print("Invalid number of elements!")
        return None

    return np.array(elements).reshape(rows, cols)

while True:
    print("\n===== MATRIX OPERATIONS TOOL =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice in ['1', '2', '3']:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        print("\nMatrix A")
        A = get_matrix(rows, cols)

        print("\nMatrix B")
        B = get_matrix(rows, cols)

        if A is None or B is None:
            continue

        if choice == '1':
            print("\nResult:")
            print(A + B)

        elif choice == '2':
            print("\nResult:")
            print(A - B)

        elif choice == '3':
            print("\nResult:")
            print(np.dot(A, B))

    elif choice == '4':
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        print("\nMatrix")
        A = get_matrix(rows, cols)

        print("\nTranspose:")
        print(A.T)

    elif choice == '5':
        n = int(input("Enter size of square matrix: "))

        print("\nMatrix")
        A = get_matrix(n, n)

        print("\nDeterminant:")
        print(np.linalg.det(A))

    elif choice == '6':
        print("Thank you!")
        break

    else:
        print("Invalid choice!")