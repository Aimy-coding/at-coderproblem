n , q= map(int,input().split())
event = [ list(map(int, input().split())) for i in range(q)]
dp = [0]* (n+1)
for i in range(q):
  e = event[i][0]
  person = event[i][1]
  
  if e == 1:
    dp[person] += 1
  if e == 2:
    dp[person] += 2
  elif e == 3:
    if dp[person] <2 :
      print("No")
    if dp[person] >= 2:
      print("Yes")
      