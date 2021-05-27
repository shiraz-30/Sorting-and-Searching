def bubble_sort(arr):
	n = len(arr)

	for i in range(0, n):
		swapped = False # this variable ensures that as soon as the list is sorted we stop the algorithm

		for j in range(0, n - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		

		if not swapped:
			return  # why ?? because now the list will be sorted
		print(arr)
	return

n = int(input())
arr = list(map(int, input().split()))

bubble_sort(arr)

"""
TC -> O(n^2), θ(n^2), Ω(n)
SC -> O(1)
No. of comparisons -> O(n^2)
No. of swaps -> O(n^2)
In place -> Yes
Stability -> Stable
"""

