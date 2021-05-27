"""
Given two integers A and B. You have a list of size n. 
A = no. of painters
B = no. of units of time taken by the any painter to paint 1 unit of a board.
The list represents the length of N boards.
Calculate minimum time required to paint all boards considering, any painter will
only paint contiguous sections of board.
2 painters cannot share the board.
(A <= 10**3 , B <= 10**6, arr[i] <= 10**6, n <= 10**5)

Eg:- A = 2, B = 5, Boards -> [1,10] => 50 units
"""
import sys
def numberOfPainters(boards, mid, B):
	count = 1 # we require atleast one painter
	time_taken_by_current_painter = 0 # initially no one has painted anything so time taken is zero
	for i in range(0, len(boards)): # iterate on all boards
		time_taken_by_current_painter += boards[i]

		if 

		if (time_taken_by_current_painter > mid): # if the total time > mid ;that means the last board considered will be painted
			count += 1
			time_taken_by_current_painter = boards[i]

	return count

a = int(input()) # no. of painters
b = int(input())
arr = [int(x) for x in input().split()]
sum_ = sum(arr)
max_ = max(arr)

low, high = max_, sum_
ans = -1
while low <= high:
	mid = low + (high - low) // 2
	
	if numberOfPainters(arr, mid) <= a:
		ans = mid
		high = mid - 1
	else:
		low = mid + 1

print(ans * b)
