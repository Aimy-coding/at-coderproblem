all = [int(input()) for i in range(4)]

ans = 0
if all[0] >= all[1]:
  ans += all[1]
if all[0]< all[1]:
  ans += all[0]
if all[2] >= all[3]:
  ans += all[3]
if all[2] < all[3]:
  ans += all[2]
print(ans)