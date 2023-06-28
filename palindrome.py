# String Palindrome: only with the letters within American alphabet
def palindrome(s):
    s = s.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    word = ''.join([x for x in s if x in alphabet])
    return word == word[::-1]

name = "A man, a plan, a canal: Panama"
print(palindrome(name))