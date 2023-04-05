n = int(input())
call = [-1] + list(map(int, input().split()))
d =[0]* (n+1)

for i in range(1, n+1):
  if d[i] == 0:
    d[call[i]] = 1
ans = [i for i in range(1, n+1) if d[i] == 0]

print(len(ans))
print(*ans,sep=" ")
  