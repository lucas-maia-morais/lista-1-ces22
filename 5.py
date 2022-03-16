def is_palindrome(x):
    """This function recognizes palindromes"""
    x = str(x) # This will work for numbers and for strings
    for i in range( len(x)//2 ):
        if (x[i] != x[len(x)-i-1]):
            return False
    
    return True
    
if __name__ == "__main__":
    print(is_palindrome('ababa'))