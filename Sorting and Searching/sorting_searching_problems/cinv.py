t = int(input())
for k in range(0, t):
	n = int(input())
	arr = list(map(int, input().split()))

	def bubble_sort(arr):
		no_of_swaps = 0
		swapped_list = []
		n = len(arr)

		for i in range(0, n):
			if_swapped = False

			for j in range(0, n - i -1):
				if arr[j] > arr[j + 1]:
					no_of_swaps+= 1
					swapped_list.append(j)
					arr[j + 1], arr[j] = arr[j], arr[j + 1]

					if_swapped = True

			if not if_swapped:
				print(no_of_swaps)
			
				return

	bubble_sort(arr)
