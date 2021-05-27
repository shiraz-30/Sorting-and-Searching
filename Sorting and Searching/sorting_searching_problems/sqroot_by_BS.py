"""
Q -> Given a perfect square value S between 1 to 10**9, find it's square root.
Eg:- S = 16129 -> ans = 127

The search space that was demonstrated using a list is a sequence of numbers
that represent some function. A lot of times those graphical representation 
need not to come from an actual sequence of data. If we have a problem which
can depict the search space into a monotonic function( increasing/ decreasing) 
i.e. we can directly apply Binary Search on that search space without actual data.
[Discrete Binary Search] 

Eg:- Prime Gap -> Consecutive gap between two prime no.s (this function is not
monotonically increasing/ decreasing) Graph varies up-down continuously. 

We wanted to find the best suitable answer in the the function f(x) = sqrt(x)
where sqrt(x) is a monotonic function, and do it by Binary Search.
"""

def sqrt(x):
	if x == 0 or x == 1:
		return x

	low, high, ans = 0, x, x

	while low <= high:
		mid = low + (high - low) // 2

		if mid * mid == x:
			return mid

		if mid * mid < x:
			# discard the left half
			low = mid + 1
			ans = mid
		else:
			high = mid - 1
	return ans

	# TC -> O(log n)
	# SC -> O(1)             

n = int(input())
print(sqrt(n))

