"""
Given a sorted list and an integer X. Find the first index value in this list
which is greater than or equal to X.
Eg :- [2, 3, 5, 6, 8, 10] size = n         (n <= 10**7)
X = 4 => Ans = 5
"""

def first_index(arr, x):
	ans = -1 # no valid candidate yet
	n = len(arr)
	low, high = 0, n - 1
	while (low <= high):
		mid = low + (high - low) // 2

		if arr[mid] >= x:
			# we have found new valid candidate to become answer
			ans = mid
			high = mid - 1
		else:
			# here we don't find any new candidate so no update to the ans
			low = mid + 1

	return ans

li = [int(x) for x in input().split()]
element = int(input())

print(first_index(li, element))

