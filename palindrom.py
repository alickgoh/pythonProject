wrd = input("Please enter a word: ")
wrd = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd.upper() == rvs.upper():
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")