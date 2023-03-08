n = int(input())
all = list(map(str, input().split()))
ans = 0

for i in range(0, n): 

  if all[i] == "Y":
    ans += 1

if ans > 0:
  print("Four")
else: print("Three")
    