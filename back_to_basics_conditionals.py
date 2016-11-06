x = 2
y = 7
z = 10

if x > y:
    print(x,'is greater than',y)
if x < y:
    print(x,'is less than', y)
if x == y:
    print(x, 'is the same as', y)

if x > y:
    print(x,'is greater than',y)
else:
    print(x,'is not greater than',y)

if x > y and y < z:
    print(x,'is greater than',y,' and ',y,' is less than ', z)
elif x < z:
    print(x,'is less than',z)
else:
    print('nothing was the case')
        
