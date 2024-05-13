def simpleArraySum(ar):
    return sum(ar)

# Input size of the array
#n = int(input("Enter the size of the array: "))

n= int(input())

# Input array elements
#ar = list(map(int, input("Enter the array elements separated by space: ").split()))

ar = list (map(int, input().split()))

# Calculate the sum of array elements using the function
result = simpleArraySum(ar)
#print("The sum of the array elements is:", result)

print (result)


#Explanations:

#1 input(): This function reads a line of input from the user and returns it as a string.

#2 strip(): This method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (including newline characters) from the string.

#3 split(): This method splits the string into a list of substrings based on the specified delimiter. By default, if no delimiter is specified, it splits the string based on whitespace characters (space, tab, newline, etc.).

#4 map(int, ...): This function applies the int() function to each element of the iterable (in this case, the list of substrings obtained after splitting) and returns an iterator. This effectively converts each substring (which represents an integer) into an actual integer.

#5 list(...): Finally, the list() function converts the iterator obtained from map() into a list. So, we get a list of integers after converting each substring to an integer.