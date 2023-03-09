n, x = map(int, input().split())
m =[ int(input()) for i in range(n)]
all = sum(m)
n = len(m)
small = sorted(m)[0]
n +=int((x-all)//small)
print(n)