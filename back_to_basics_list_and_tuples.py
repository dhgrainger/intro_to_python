#tuples
def example():
  return 15,19

a,b = example()

print(a)
print(b)

#Lists 

x = [6,5,4,7,9,0,2,9]

print(x)

print(x[3])

x.append(12)

print(x)

x.insert(5,7)

print(x)

x.remove(7)

print(x)

print(x.index(12))

x = ['Doug','Sam','Digby']
x.sort()
print(x)
x.reverse()
print(x)
