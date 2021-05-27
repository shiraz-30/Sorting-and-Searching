def find_min_element_idx(arr, start):
	"""
	arr is the list
	start is the starting index of the unsorted part
	"""
	min_index = start

	start += 1

	while (start < len(arr)):
		if arr[start] < arr[min_index]:
			min_index = start

		start += 1

	return min_index 

def selection_sort(arr):
	n = len(arr)
	i = 0

	while i < len(arr):
		min_index = find_min_element_idx(arr, i)
		if i != min_index:
			arr[i], arr[min_index] = arr[min_index], arr[i]
		print(arr)							
		i += 1

	return

n = int(input())
arr = list(map(int, input().split()))

selection_sort(arr)

"""
TC -> O(n^2), θ(n^2), Ω(n^2)
SC -> O(1)
No. of comparisons -> O(n^2)
No. of swaps -> O(n)
In place -> Yes
Stability -> Unstable
"""
