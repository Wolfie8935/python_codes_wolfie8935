#count upper and lower case
input_string = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Upper case count: ", upper_count)
print("Lower case count: ", lower_count)
