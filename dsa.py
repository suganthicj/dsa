x11=int(input())
y11=0
z11=list(map(int,input().split()))
for i in range(x11-1):
	for j in range(i+1,x11):
		if z11[i]<z11[j]:
			y11+=1
print(y11)
