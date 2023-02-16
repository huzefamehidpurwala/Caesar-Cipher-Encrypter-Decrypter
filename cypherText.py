from string import whitespace, punctuation, ascii_lowercase as letters
from enchant import Dict
# from requests import get

dic1 = dict()
dic2 = dict()
for i, l in enumerate(letters):
    dic1.update({l.lower(): i})
    dic1.update({i: l.upper()})
    dic2.update({l.upper(): i})
    dic2.update({i: l.lower()})

"""
def is_properly_english(string):
    words = string.split()  # split string into words
    for word in words:
        response = get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 404:  # check if word is not found in the dictionary
            return False
    return True
"""

def is_proper_english(string):
    d = Dict("en_US")  # load English dictionary
    words = string.split()  # split string into words
    for word in words:
        if not d.check(word):  # check if word is spelled correctly
            return False
    return True

def encrypt(str1, k):
    if k > 25:
        return None
    enc = ""
    for s in str1.lower():
        if s in whitespace + punctuation:
            enc += s
            continue
        enc += dic1.get((dic1.get(s) + k) % 26)
    return enc

def decrypt(str1):
    enc = ""
    for k in range(1, 26):
        for s in str1.upper():
            if s in whitespace + punctuation:
                enc += " "
                continue
            enc += dic2.get((dic2.get(s) - k) % 26)
        if is_proper_english(enc):
            return enc, k
        else:
            enc = ""

    return None, None


if input("Enter y to encrypt or anything else to decrypt: ").lower() == "y":
    print(encrypt(input("Enter the text to encrypt: "), int(input("Enter the key number: "))))
else:
    str2, key = decrypt(input("Enter the text to decrypt: "))
    print(f"str: {str2} | key: {key}")
