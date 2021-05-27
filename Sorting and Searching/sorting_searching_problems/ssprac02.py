def bubble_sort(arr):
	n = len(arr)

	for i in range(0, len(arr)):
		swapped = False 

		for j in range(0, len(arr) - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		

		if not swapped:			
			return 
		print(*arr)

	return


n = int(input())
li = list(map(int, input().split()))
bubble_sort(li)
