n, m = map(int, input().split())
s = [str(input())[3:6] for i in range(n)]
t = [str(input()) for i in range(m)]

count = 0
for i in range(n):
  if s[i] in t:
    count += 1
print(count)
    

