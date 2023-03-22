s = str(input())
all = int(len(s)/2)+1
ans = []

for i in range(1, all):
  num = 2*i
  ans.append(s[num-1])
  ans.append(s[num-2])
print("".join(ans))
  