word = str(input())

for i in range(len(word)):
  if word[i].isupper():
    print(i+1)
    break