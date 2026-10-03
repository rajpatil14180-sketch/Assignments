
#LARGEST OF THREE NUMBERS!!!

a = int(input('enter first number a:'))
b = int(input('enter second number b:'))
c = int(input('enter third number c:'))

if (a > b and a > c):
    print('largest number =',a)
elif (b > a and b > c):
    print('largest number =',b)
elif (c > a and c > b):
    print('largest number =',c)
elif (a == b and a < c):
    print('largest number =',c)
elif (a == b and a > c):
    print('largest number =',a)
elif (b == c  and b < a):
    print('largest number =',a)
elif (b == c  and b > a):
    print('largest number =',b)
elif (c == a and c < b):
    print('largest number =',b)
elif (c == a and c > b):
    print('largest number =',c)
else:
    print('ALL ARE EQUAL :)')

