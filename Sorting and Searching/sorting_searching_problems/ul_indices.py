"""
Given an unsorted list, find any element a[i] such that a[i] > a[i - 1]
and a[i] > a[i + 1]. There can be multiple a[i], find any one of them.
Return the index. ( Do something better than O(n) -> Optimized solution )
Eg :- [1, 2, 3, 1] Ans -> 2 index
"""

def find_peak(arr):
	low, high = 0, len(arr) - 1

	while low < high:
		mid = low + (high - low) // 2

		if arr[mid] > arr[mid + 1]:
			# Case- 2
			high = mid
		else:
			low = mid + 1

	return low # TC -> O(log n)

