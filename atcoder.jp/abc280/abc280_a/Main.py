H, W = map(int, input().split())
S = [str(input()) for i in range(H)]
answer = 0


for h in range(H):
   answer += int(S[h].count("#"))
print(answer)
    
