"""
There are n ropes, you need to cut them into K small ropes of equal lengths.
Find the maximum length of pieces you can get.
Precision required -> 10**(-6)
1 <= n,K <= 10**4
1 <= length of ith rope <= 10**7
n = 4, K = 11
802
743
457
539
ans = 200.5
"""

def isCutPossible(x, arr, k):
	sum = 0
	for i in range(0, len(arr)):
		sum += arr[i] // x
	return sum >= k

n, k = [int(x) for x in input().split()]
arr = []

for i in range(0, n):
	y = int(input())
	arr.append(y)

l, r = 0, 1e10
for i in range(0, 200):
	m = (l + r) / 2
	if isCutPossible(m, arr, k) == True:
		l = m
	else:
		r = m

print("%0.6f" % l)

