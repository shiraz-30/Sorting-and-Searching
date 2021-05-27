"""
(x**2 + x**0.5 = c) where c = real number
Given the value of c, find x. (1 <= c <= 10**10)
Print upto 6 decimal places.
Eg:- 
c = 2 => x = 1

Logic ->
Generally in binary search, we remove half of the search space by either doing
low = mid + 1 or high = mid - 1.
But here our answer can be a real no., so if we reduce by doing a +1 or -1, 
then we can loose the most accurate answer.
Better solution -> low = mid or high = mid.

For treating real no.s -> we calculate the delta between l and r and compare
with epsilon(precision you want for your ans). 
epsilon -> 10**(-6) or 10**(-7). 
"""

def calc(c):
	l, r = 1, 1e10 # 1e10 = 10**10
	mid = 0.0

	for i in range(0, 200):
		mid = (l + r) / 2

		if mid*mid + mid**0.5 == c:
			return mid
		elif mid*mid + mid**0.5 > c:
			r = mid
		else:
			l = mid

	return mid

c = float(input())
ans = calc(c)

print("%0.6f" % ans)

# TC -> O(1)
