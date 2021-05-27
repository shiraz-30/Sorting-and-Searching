def insertion_sort(arr):

	for i in range(1, len(arr)):
		key = arr[i] # this element will be now inserted to it's correct position
		j = i - 1 # because the accurate place of insertion will be on the left

		while (j >= 0 and key < arr[j]):
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

		print(arr)

	return

arr = list(map(int, input().split()))

insertion_sort(arr)

"""
TC -> O(n^2) , θ(n^2), Ω(n)
SC -> O(1)
No. of comparisons -> O(n^2)
No. of swaps -> O(n^2)
In place -> Yes
Stability -> Stable
"""

