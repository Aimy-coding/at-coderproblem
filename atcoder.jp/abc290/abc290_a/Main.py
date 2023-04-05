n, m = map(int, input().split())

point = [0]+list(map(int, input().split()))

solve = list(map(int, input().split()))
ans = 0
for i in range(m):
  solved = solve[i]
  ans += point[solved]
print(ans)