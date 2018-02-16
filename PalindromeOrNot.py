from sqlalchemy import true

a=input("Enter a string: ")
b= a[::-1]
print('Reversed Result: ',b)



if (a[:1]==b[:1]):
    print('THis is palindrome string!!')
else:
    print('This is not a palyndrome string!!')


