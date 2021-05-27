"""
Q -> There are n rectangles of same size( w * h), w = width and h = height. 
It is required to find a square of the smallest size into while these rectangles
can be packed. We cannot rotate the rectangles. Find the side of the smallest 
square. ( w, h, n <= 10**9 )
Eg:- w = 2, h = 3, n = 10 => ans = 9 (square of 9*9 fits in)
"""

def good(mid, n, w, h): # mid -> side of the square
	return(mid // w) * (mid // h) >= n

def adjust_rectangle(w, h, n):
	low = 0
	high = max(w, h) * n
	ans = -1

	while(low <= high):
		mid = low + (high - low) // 2

		if (good(mid, n, w, h)):
			high = mid - 1
			ans = mid
		else:
			low = mid + 1

	return ans

	# TC -> O(log(max(w, h)* n))
	# SC -> O(1)

w, h, n = [int(x) for x in input().split()]
print(adjust_rectangle(w, h, n))

