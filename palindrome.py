while True:
    str = input("Enter a string: ")
    rev_str = ""
    for char in str:
        rev_str = char + rev_str
    if str == rev_str:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")