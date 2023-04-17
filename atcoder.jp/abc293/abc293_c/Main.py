H,W=map(int,input().split())
A = [list(map(int, input().split()) )for i in range(H)]
p=[0]*(H+W-1)
def f(h,w):
	if h>=H or w>=W:	return 0
	n=A[h][w]
	if n in p[:h+w]:	return 0
	p[h+w]=n
	if h==H-1 and w==W-1:	return 1
	return f(h+1,w)+f(h,w+1)
N=f(0,0)
print(N)