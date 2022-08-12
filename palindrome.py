def palindrome(s):
    return s==s[::-1]
    
s=input("Enter your text/number\n")
a=(palindrome(s))
if a:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")

print("Palindrome") if s == s[::-1] else print("Not")