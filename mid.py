def d(n, k):
    if n %k == 0:
        k += k
        return k
    else:
        return d(k, n%k)

print(d(12,15))
print(12%15)
#12 15
#15 12
#15 % 12 = 3 x
#12 15% 12
#12 3
#12 % 3 = 0
#3 += 3
#return 5


#list, A 0 6
#rang siz = 6 - 0 + 1 = 7
#mid = 6 + 0 // 2 = 3
#if A == list[mid] x
#pos = 3
#elif rang siz == 1 x
#pos = -1
#else +
#if A < list[3] A < E
#pos = find(list, A, 0, 3)
#list, A 0 3
#rang siz = 3 - 0 +1 = 4
#mid = 3 + 0 // 2 = 1
#if A == list[1] A = C x
#elif rang siz == 1 x
#pos = -1
#else +
#if A < list[1] A < C
#pos = find(list,A, 0, 1)
#rang siz = 1 - 0 + 1 = 2
#mid = 1 + 0 // 2 = 0
#if A == list[0] A = B x
#pos = 0
#elif 2 == 1 x
#pos = -1
#else:
#if A < list[0] A < B
#pos = find(list, A, 0, 0)
#rang siz = 0- 0+ 1 = 1
#mid = 0+0//2= 0
#if A == list[0] A ==B x
#elif rang siz = 1: +
#pos = -1
#Yeah idk this is taking too long and its kinda confusing
#If i had more time Id probably nail it but this is takking
#way too long to do maybe the answer will come to me






