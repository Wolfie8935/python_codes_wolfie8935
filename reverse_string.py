a = input("Enter string: ")
b = []
for i in range(0, len(a)):
  b.append(a[len(a) - 1 - i])

# Print the reversed string.
for i in range(len(b)):
  print(b[i],end="")

# Check if the string is a palindrome.
is_palindrome = True
for i in range(len(a) // 2):
  if (a[i] != a[len(a) - 1 - i]):
    is_palindrome = False
    break

if is_palindrome:
  print("\nPalindrome")
else:
  print("\nNot palindrome")