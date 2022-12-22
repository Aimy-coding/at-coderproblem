N, A, B = map(int, input().split())
print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))
## map(int, str(i)) stringのiの要素（11だったら1と1）を整数化
##そのあと整数化された要素が足し算される
