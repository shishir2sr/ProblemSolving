a=input("Input string: ")

v = 0
c = 0

vow = list("aeiouAEIOU")
con = list("abcdfghjklmnpqrstvwxyzABCDFGHJKLMNPQRSTVWXYZ")


for i in a:
    if i in vow:
        v+=1
    elif i in con:
        c+=1

print("Total vowels: ", v,"Total consonants: ", c)
