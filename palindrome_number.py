def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

n = int(input("Enter a number: "))

if is_palindrome(n):
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")