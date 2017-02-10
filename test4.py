def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    print is_palindrome("fuckup")
    print is_palindrome("tenet")
print is_palindrome("radar")