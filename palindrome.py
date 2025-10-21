print("Enter a string to perform the operations of Palindrome and counting vowels : ")
s = input("Enter a string: ")

def Palindrome(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    if s == rev_str:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
        
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print(f"The number of vowels in '{s}' is {count}")

Palindrome(s)
count_vowels(s)
