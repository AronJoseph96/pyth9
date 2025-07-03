str = input("Enter a string: ")
str_nospace = str.replace(" ", "")
finalstr = str_nospace.lower()
if finalstr == finalstr[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

