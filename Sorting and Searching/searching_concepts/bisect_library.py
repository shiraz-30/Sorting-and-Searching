import bisect

arr = [int(x) for x in iput().split()]

while True:
	ch = input()
	if ch == 'l':
		x = int(input())

		print(bisect.bisect_left(arr, x)) # TC -> O(log n)
	elif ch == 'r':
		x = int(input())
		print(bisect_right(arr, x)) # TC -> O(log n)
	else:
		break


