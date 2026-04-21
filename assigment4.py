#palindrom

n = input("enter number:")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")