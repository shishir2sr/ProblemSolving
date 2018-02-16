st = input('Enter a string: ')
count = [0]*256
max = -1
b=''
for i in st:
    count[ord(i)] += 1

for i in st:
    if max < count[ord(i)]:
        max = count[ord(i)]
        b = i

print("Maximum Frequency character is: ", b, "\n& Its frequency is", count[ord(i)])
