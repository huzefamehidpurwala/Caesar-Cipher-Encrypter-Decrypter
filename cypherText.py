from string import whitespace, punctuation, digits, ascii_lowercase as letters
# from enchant import Dict
from requests import get

dic1 = dict()
dic2 = dict()
for i, l in enumerate(letters):
  dic1.update({l.lower(): i})
  dic1.update({i: l.upper()})
  dic2.update({l.upper(): i})
  dic2.update({i: l.lower()})


def is_proper_english(string):
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
"""


def encrypt(str1, k):
  if k > 25:
    return None
  enc = ""
  for s in str1.lower():
    if s in whitespace + punctuation + digits:
      enc += s
      continue
    enc += dic1.get((dic1.get(s) + k) % 26)
  return enc


def decrypt(str1, k):
  if k > 25:
    return None
  enc = ""
  for s in str1.upper():
    if s in whitespace + punctuation + digits:
      enc += s
      continue
    enc += dic2.get((dic2.get(s) - k) % 26)
  return enc


def hackit(str1):
  for k in range(1, 26):
    for s in str1.split():
      if len(s.strip(whitespace + punctuation + digits)) < 3:
        continue
      if is_proper_english(decrypt(s, k).strip(whitespace + punctuation + digits)):
        if is_proper_english(decrypt(str1.strip(whitespace + punctuation + digits), k)):    
          return decrypt(str1, k), k
  return None, None


def welcome():
  print("What you want to do?")
  print("\t1. Encrypt a message")
  print("\t2. Decrypt a Cipher Text")
  print("\t3. Hack a Cipher Text")
  print("To exit enter q")
  return eval(input(":-> "))


while True:
  flag = welcome()
  if flag == 1:
    print(encrypt(input("\nEnter the text to encrypt: "), int(input("Enter the key number: "))), end="\n\n")
  elif flag == 3:
    str2, key = hackit(input("\nEnter the message to hack: "))
    print(f"\nstr: {str2} | key: {key}", end="\n\n")
  elif flag == 2:
    print(decrypt(input("\nEnter the text to decrypt: "), int(input("Enter the key number: "))), end="\n\n")
  else:
    # print("\nPlease enter a numerical value between 1-3 and try again!", end="\n\n")
    break
