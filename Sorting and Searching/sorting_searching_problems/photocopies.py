"""
Q -> You have a practical, and you went to the photocopy shop to bring
'n' copies of a page. 
There are 2 machines at the shop, first one copies a sheet in x second
and the second copies in y second.
You can run both machines parallely and can create photocopy of both
original and copies page.
Find the minimum time required to make n copies.
( n <= 10**8 and x,y <= 10)

high = max(x,y)*n -> machine that takes more time, we will make all copies by it
mid = to create n copies, we will check if it is a good mid(if it's possible 
to print n copies in mid seconds)
low = min time taken for copies 

1st copy will be done seperately
1st machine -> mid/x copies
2nd machine -> mid/y copies

=> mid/x + mid/y + 1 >= n
"""

def good(mid, n, x, y):
	return (mid // x) + (mid // y) >= n - 1

def printing_copies(n, x, y):
	if n == 1:
		return min(x, y)

	low = 0
	high = max(x, y) * n

	while low <= high:
		mid = low + (high - low) // 2

		if good(mid, n, x, y):
			ans = mid
			high = mid - 1
		else:
			low = mid + 1

	return ans + min(x, y)

n, x, y = [int(x) for x in input().split()]
print(printing_copies(n, x, y))

