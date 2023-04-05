n = int(input())
point = list(map(int, input().split()))

point_sort = sorted(point)

all = 0
for i in range(n, 4*n):
  all += point_sort[i]

print(all/(3*n))