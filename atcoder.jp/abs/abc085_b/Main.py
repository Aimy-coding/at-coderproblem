N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))
#set:集合なので、リストとは異なり要素は順番をもちません。また、重複した要素は取り除かれます
#セットから要素を削除するにはremove()を使います