N = int(input())
A = list(map(int, input().split()))

count = 0
while all(a % 2== 0 for a in A):
  A = [a/2 for a in A]
  count += 1
print(count)

#すべての要素がTrueか判定: all()
#いずれかの要素がTrueか判定: any()