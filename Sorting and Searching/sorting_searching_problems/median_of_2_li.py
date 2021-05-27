"""
Q -> There are two sorted lists of different sizes. Find the median of the elements
from both the lists.
Try to do this in less than O(n), O(m), O(n + m)

Eg:- [1, 12, 15, 26, 38] and [2, 13, 17, 30, 15]
Ans => 16
Sort both the lists and the mid elements come to be 15 and 17.
So, (15 + 17) // 2 = 16
"""

import sys
def median(a, b):
	if len(a) > len(b):
		return median(b, a)

	x, y = len(arr), len(b)
	low = 0
	high = x
	while low <= high:
		partitionX = (low + high) // 2
		partitionY = ((x + y + 1) // 2) - partitionX

		if partitionX == 0:
			maxLeftX = -1*sys.maxsize
		else:
			maxLeftX = a[partitonX - 1]

		if partitionY == 0:
			maxLeftY = -1*sys.maxsize
		else:
			maxLeftY = a[partitonY - 1]

		if partitionX == x:
			minRightX = sys.maxsize
		else:
			minRightX = a[partitionX]

		if partitionY == y:
			minRightY = sys.maxsize
		else:
			minRightY = b[partitionY]

		if maxLeftX <= minRightY and maxLeftY <= minRightX:

			if (x + y) % 2 == 0:
				return max(max(maxLeftX, maxLeftY) + min(minRightY, minRightX)) / 2
			else:
				return max(maxLeftX, maxLeftY)

		elif maxLeftX > minRightY:
			high = partitionx - 1
		else:
			low = partitionX + 1

	return -1

x = [int(i) for x in input().split()]
y = [int(j) for y in input().split()]



		
