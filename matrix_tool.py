import numpy as np
print("Enter Matrix A (2x2)")
a11 = int(input("A[1][1]: "))
a12 = int(input("A[1][2]: "))
a21 = int(input("A[2][1]: "))
a22 = int(input("A[2][2]: "))
A = np.array([[a11, a12],
              [a21, a22]])
print("\nEnter Matrix B (2x2)")
b11 = int(input("B[1][1]: "))
b12 = int(input("B[1][2]: "))
b21 = int(input("B[2][1]: "))
b22 = int(input("B[2][2]: "))
B = np.array([[b11, b12],
              [b21, b22]])
while True:
    print("\n===== MATRIX OPERATIONS TOOL =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose of A")
    print("5. Determinant of A")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("\nResult:")
        print(A + B)
    elif choice == 2:
        print("\nResult:")
        print(A - B)
    elif choice == 3:
        print("\nResult:")
        print(np.dot(A, B))
    elif choice == 4:
        print("\nResult:")
        print(A.T)
    elif choice == 5:
        print("\nResult:")
        print(np.linalg.det(A))
    elif choice == 6:
        print("Thank You!")
        break11
    else:
        print("Invalid Choice")