def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':

    #This line checks if the script is being run directly by the Python interpreter, rather than being imported as a module into another script.
    # When a Python file is run as the main program, the special variable __name__ is set to '__main__'.
    # This construct is often used to define code that should only run when the script is executed directly, and not when it's imported as a module.

    ar_count = int(input().strip())

    #This line reads input from the user (or from standard input if the script is being run from the command line).
    # It uses the input() function to read a line of text entered by the user, strip() method to remove any leading or trailing whitespace characters, and int() function to convert the input to an integer.
    # The resulting integer is assigned to the variable ar_count, which presumably represents the number of elements in the array.

    ar = list(map(int, input().rstrip().split()))

    #This line reads another line of input from the user (or from standard input), assuming that the input consists of space-separated integers.
    # It uses the input() function to read the line of text, rstrip() method to remove any trailing whitespace characters,
    # split() method to split the string into a list of substrings (using whitespace as the delimiter), map() function to apply the int() function to each substring (converting them to integers),
    # and finally list() to convert the resulting iterable into a list. The resulting list of integers is assigned to the variable ar, which presumably represents the array of integers.

    result = aVeryBigSum(ar)
    print(result)