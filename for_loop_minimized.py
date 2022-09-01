from lib2to3.pgen2.token import DOUBLESLASH


lst = [1,2,3]
doubled = []

for num in lst:
    doubled.append(num*2)
print(doubled)

doubled = [num*2 for num in lst]
print(doubled)