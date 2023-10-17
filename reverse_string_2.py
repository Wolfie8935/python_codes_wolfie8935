#reverse string
string = input("Enter a string: ")
reverse = ""

for char in string:
    reverse = char + reverse
    