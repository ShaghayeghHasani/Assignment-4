n = int(input("How many terms do you want to print? "))
a = 0
b = 1
count = 0

if n == 1:
    print(a)
else:
    while count<n :
        print(a)
        sum = a + b
        count+= 1
        a = b
        b = sum
