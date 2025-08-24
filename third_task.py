import numpy as np

def get_matrix_input(matrix_number):
    """
    Prompts the user to enter the dimensions and elements of a matrix.
    Returns the matrix as a numpy array, or None if input is invalid.
    """
    try:
        rows = int(input(f"Enter the number of rows for Matrix {matrix_number}: "))
        cols = int(input(f"Enter the number of columns for Matrix {matrix_number}: "))
    except ValueError:
        print("Error: Please enter a valid integer for rows and columns.")
        return None

    matrix = []
    print(f"Enter the elements of Matrix {matrix_number} row by row, separated by spaces:")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Error: Number of elements must be {cols}.")

    return np.array(matrix)

def display_matrix(matrix, name):
    """
    Prints a matrix with a given name in a clear format.
    """
    print(f"\n--- {name} ---")
    print(matrix)

def main():
    """
    Main function to run the Matrix Operations Tool.
    """
    print("Welcome to the Matrix Operations Tool!")
    
    matrix1 = get_matrix_input(1)
    if matrix1 is None:
        return
    
    matrix2 = get_matrix_input(2)
    if matrix2 is None:
        return

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose of Matrix 1")
        print("5. Transpose of Matrix 2")
        print("6. Determinant of Matrix 1")
        print("7. Determinant of Matrix 2")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            if matrix1.shape == matrix2.shape:
                result = matrix1 + matrix2
                display_matrix(result, "Result of Addition")
            else:
                print("Error: Matrices must have the same dimensions for addition.")
        
        elif choice == '2':
            if matrix1.shape == matrix2.shape:
                result = matrix1 - matrix2
                display_matrix(result, "Result of Subtraction")
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")
        
        elif choice == '3':
            if matrix1.shape[1] == matrix2.shape[0]:
                result = np.dot(matrix1, matrix2)
                display_matrix(result, "Result of Multiplication")
            else:
                print("Error: The number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
        
        elif choice == '4':
            result = np.transpose(matrix1)
            display_matrix(result, "Transpose of Matrix 1")
        
        elif choice == '5':
            result = np.transpose(matrix2)
            display_matrix(result, "Transpose of Matrix 2")
        
        elif choice == '6':
            if matrix1.shape[0] == matrix1.shape[1]:
                try:
                    result = np.linalg.det(matrix1)
                    print(f"\nDeterminant of Matrix 1: {result}")
                except np.linalg.LinAlgError:
                    print("Error: Cannot calculate determinant.")
            else:
                print("Error: Determinant can only be calculated for square matrices.")
        
        elif choice == '7':
            if matrix2.shape[0] == matrix2.shape[1]:
                try:
                    result = np.linalg.det(matrix2)
                    print(f"\nDeterminant of Matrix 2: {result}")
                except np.linalg.LinAlgError:
                    print("Error: Cannot calculate determinant.")
            else:
                print("Error: Determinant can only be calculated for square matrices.")
        
        elif choice == '8':
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()