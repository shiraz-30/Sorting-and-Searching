def binary_search(arr, target):
	# first of all we will define the search space
	n = len(arr)
	left, right = 0, n - 1 # boundaries of the search space

	while (left <= right):
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			right = mid - 1
		else:
			left = mid + 1

	return n - 1

"""
TC -> O(log(n)), θ(log(n)), Ω(1)
SC -> O(1)
"""
