c1 = 'd'
while c1 > 'b':
    for i in range(3):
        print(f'{c1}{i}', end=' ')
    c1 = chr(ord(c1) - 2)
print(chr(14))
