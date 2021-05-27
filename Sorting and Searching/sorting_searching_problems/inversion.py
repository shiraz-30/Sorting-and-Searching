"""
Q -> Let A[0...n-1] be an array of n distinct positive integers. If i < j and
A[i] > A[j] then the pair i, j) is called an inversion of A. Given n and an 
array A your task is to find the number of inversions of A.

INPUT =>
The first line contains t, the number of testcases followed by a blank space.
Each of the t tests start with a number n (n <= 200000). Then n + 1 lines
follow. In the ith line a number A[i - 1] is given (A[i - 1] <= 10^7).
The (n + 1)th line is a blank space.

OUTPUT =>
For every test output one line giving the number of inversions A.

Example:- 
Input:
2

3
3
1
2

5
2
3
8
6
1

Output:
2
5

Explanation:-

If you make all possible pairs then the pair with elements (a[i], a[j]) where
i < j and a[i] > a[j] is a valid inversion.
Eg:- [2, 3, 8, 6, 1]
Pairs:- (2, 1) , (3, 1) , (8, 6) , (8, 1) , (6, 1) -> Valid Inversion
For every element, a pair can be made with elements on the right of it only.
Ans = 5
Left = [2, 3, 8] , Right = [6, 1]
Total inversion = Inversion of left + Inversion of right + Inversion from merge
"""

def merge(arr, left, mid, right):
	temp = [0]*(right - left + 1)
	i, j, k, count = left, mid + 1, 0, 0

	while i <= mid and j <= right:
		if arr[i] < arr[j]:
			temp[k] = arr[i]
			i += 1
			k += 1
		else:
			count += (mid - i + 1)
			temp[k] = arr[j]
			j += 1
			k += 1

	while i <= mid:
		temp[k] = arr[i]
		i += 1
		k += 1

	while j <= right:
		temp[k] = arr[j]
		j += 1
		k += 1

	k = 0
	for i in range(left, right + 1):
		arr[i] = temp[k]
		k += 1

	return count

def merge_sort(arr, left, right):
	if left < right:
		mid = (left + right) // 2
		count_left = merge_sort(arr, left, mid)
		count_right = merge_sort(arr, mid + 1, right)
		count_mergers = merge(arr, left, mid, right)
		return count_left + count_right + count_mergers

	return 0

t = int(input())

for i in range(0, t):
	ch = input()
	n = int(input())
	li = []

	for j in range(0, n):
		x = int(input())
		li.append(x)

	inv_cnt = merge_sort(li, 0, n - 1)
	print(inv_cnt)

