# isPalindrome
# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

def isPalindrome(strng):
    if len(strng) == 0 or len(strng) == 1:
        return True
    else:
        if strng[0] != strng[len(strng)-1]:
            return False
        else:
            isPalindrome(strng[1:len(strng)-1])
    return True

# Examples

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false
