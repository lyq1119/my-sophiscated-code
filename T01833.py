def rank(lst,a):
    alst = sorted(lst,reverse=True) 
    return alst.index(a)

def mul(n):
    j = 1
    i = 1
    while i <= n:
        j *= i
        i += 1
    return j
    
def fun(lst,n,k):
    k = k % mul(n)
    for i in range(1,len(lst)):
        lst1 = lst[-i-1:]
        if rank(lst1,lst1[0]) > 0:
            if k - (rank(lst1,lst1[0]))*mul(i) > 0:
                k = k - rank(lst1,lst1[0])*mul(i)
            else:
                lst2 = []
                index = rank(lst1,lst1[0]) - ((k-1)//mul(i)) - 1
                lst1 = sorted(lst1,reverse=True)
                lst2.append(lst1[index])
                lst1.remove(lst1[index])
                k = k - (k//mul(i)) * mul(i)
                for j in range(i):
                    j = i - 1 - j
                    if j <= 4:
                        index = - ((k-1)//mul(j)) - 1
                        lst2.append(lst1[index])
                        lst1.remove(lst1[index])
                        k = k - (k//mul(j)) * mul(j)
                    else:
                        lst2.append(lst1[-1])
                        lst1.remove(lst1[-1])
                return lst[:-i-1]+lst2
    lst2 = []
    lst1 = sorted(lst,reverse=True)
    for j in range(n):
        j = n - j
        if j <= 5:
            index = -((k-1)//mul(j-1))- 1
            lst2.append(lst1[index])
            lst1.remove(lst1[index])
            k = k - (k//mul(j-1)) * mul(j-1)
        else:
            lst2.append(lst1[-1])
            lst1.pop()
    return lst2

for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    print(*fun(lst,n,k))