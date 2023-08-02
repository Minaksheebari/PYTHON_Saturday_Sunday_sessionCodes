# Write a program in Python to create and print a valid IP Address from the given String of numeric values -
# Sample Input 1  :  addressString = "19216801"

# Output:  IP Address = 192.168.0.1

# Sample Input 2  :  addressString = "190145"

# Output:  IP Address = 190.1.4.5

address = int(input("Enter string to conver in IP Address: "))
print(address)

address = []

print((address[:3]) + "." + (address[3][6]) + "." + (address[3:]))