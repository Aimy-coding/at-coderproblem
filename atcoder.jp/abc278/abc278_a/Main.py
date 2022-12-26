N, K = map(int, input().split())
A =  input().split()
if K >= N:
  answer = [0]*N
  print(' '.join(map(str, answer)))
else:
 
  answer = A[K:N]
  answer.extend([0]*K)
  print(' '.join(map(str, answer)))
