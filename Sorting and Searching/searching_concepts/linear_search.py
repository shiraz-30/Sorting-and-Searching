def linear_search(arr, target):
	for i in range(0, len(arr)):
		if arr[i] == target:
			return i

	return n - 1

n = int(input())

li = [int(x) for x in input().split()]
target = int(input())

print(linear_search(li, target))

"""
TC -> O(n), θ(n), Ω(1)
SC -> O(1)
SC(if recursively approached) -> O(n)
"""

