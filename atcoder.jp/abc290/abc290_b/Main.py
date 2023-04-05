n, k = map(int, input().split())

rank = str(input())
ans = []
count = 0
for i in range(n):
  if rank[i] == "o" and count < k:
    ans.append("o")
    count += 1
  else:
    ans.append("x")
print(*ans, sep = "")


    