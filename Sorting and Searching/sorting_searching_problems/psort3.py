n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

pairs = []
for i in range(0, n):
	
	pairs.append((arr[i] , brr[i]))
	pairs.sort()

for i in range(0, n):
	print(*pairs[i], end = " ")

