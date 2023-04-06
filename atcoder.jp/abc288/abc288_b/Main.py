n, k = map(int, input().split())
s = [str(input()) for i in range(n)][:k]
ans =sorted(s)

for i in range(k):
  print(ans[i])