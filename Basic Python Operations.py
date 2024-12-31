def arithmetic_operations(a, b):  
    print(f"Addition: {a + b}")  
    print(f"Subtraction: {a - b}")  
    print(f"Multiplication: {a * b}")  
    print(f"Division: {a / b if b != 0 else 'Undefined (division by zero)'}")  
  
def string_operations(string):  
    print(f"Original string: {string}")  
    print(f"Uppercase: {string.upper()}")  
    print(f"Lowercase: {string.lower()}")  
    print(f"Reversed: {string[::-1]}")  
    print(f"Is palindrome: {string == string[::-1]}")  
  
def check_even_odd(number):  
    if number % 2 == 0:  
        print(f"{number} is Even")  
    else:  
        print(f"{number} is Odd")  
  
def print_numbers(n):  
    print(f"Printing numbers from 1 to {n}:")  
    for i in range(1, n + 1):  
        print(i, end=" ")  
    print()  
  
def list_operations():  
    numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))  
    print(f"Original List: {numbers}")  
    num_to_append = int(input("Enter a number to append to the list: "))  
    numbers.append(num_to_append)  
    print(f"List after appending {num_to_append}: {numbers}")  
    num_to_remove = int(input("Enter a number to remove from the list: "))  
    if num_to_remove in numbers:  
        numbers.remove(num_to_remove)  
        print(f"List after removing {num_to_remove}: {numbers}")  
    else:  
        print(f"{num_to_remove} is not in the list.")  
    print(f"List length: {len(numbers)}")  
  
def dictionary_operations():  
    student = {  
        "name": input("Enter student name: "),  
        "age": int(input("Enter student age: ")),  
        "grade": input("Enter student grade: ")  
    }  
    print(f"Original Dictionary: {student}")  
    new_age = int(input("Enter the updated age: "))  
    student["age"] = new_age  
    print(f"Updated Dictionary: {student}")  
    print(f"Keys: {list(student.keys())}")  
    print(f"Values: {list(student.values())}")  
  
def file_operations():  
    content = input("Enter content to write to the file: ")  
    with open("example.txt", "w") as file:  
        file.write(content)  
    print("File written successfully.")  
    with open("example.txt", "r") as file:  
        content = file.read()  
        print(f"File content: {content}")  
  
def main():  
    print("Basic Python Program Demonstration")  
    a = int(input("Enter the first number for arithmetic operations: "))  
    b = int(input("Enter the second number for arithmetic operations: "))  
    arithmetic_operations(a, b)  
    string = input("Enter a string to perform string operations: ")  
    string_operations(string)  
    number = int(input("Enter a number to check if it's even or odd: "))  
    check_even_odd(number)  
    n = int(input("Enter the range of numbers to print: "))  
    print_numbers(n)  
    list_operations()  
    dictionary_operations()  
    file_operations()  
  
if __name__ == "__main__":  
    main()