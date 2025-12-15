from collections import namedtuple
Kam = namedtuple('Kam',['name', 'age', 'major'])
jk = Kam('Burd', '20', 'CS')

print(jk)
mat = namedtuple('mat',['num1', 'num2'])
ma = mat(20, 25)
print(ma.num1 + ma.num2)
