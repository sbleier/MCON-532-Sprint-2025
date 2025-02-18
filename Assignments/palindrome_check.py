def is_palindrome(s: str) -> bool:
    """checks if string is palindrome"""
    s = "".join(char.lower() for char in s if char.isalnum())  #removes spaces and non-alphanumeric chars from string
    return s == s[::-1]  #checks if string is equal to reversed string (using slicing)


if __name__ == "__main__":
    s = input("Please enter input")
    print(is_palindrome(s))