
def read_number_sequence():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [float(value) for value in user_input.split()]

    print("The sequence of numbers is:")
    print(numbers)


def read_array():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    array = []

    for i in range(rows):
        while True:
            user_input = input(
                f"Enter {columns} numbers for row {i + 1}: "
            )
            row = [float(value) for value in user_input.split()]

            if len(row) == columns:
                array.append(row)
                break

            print(f"Please enter exactly {columns} numbers.")

    print("The array is:")
    for row in array:
        print(row)


def main():
    print("=== Lab 2: Keyboard Input ===")
    read_number_sequence()
    read_array()

if __name__ == "__main__":
    main()

def read_numbers_from_file():
    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        numbers = content.split()
        print("Numbers read from file:", numbers)

    except FileNotFoundError:
        print("Error: The specified file does not exist.")

    read_numbers_from_file()