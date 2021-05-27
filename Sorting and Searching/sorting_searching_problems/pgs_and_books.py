"""
Given number of pages of n different books and m is the value of number of 
students. Books are arranged in increasing order of pages. One student can read
consecutive books only. Assign books such that maximum number of pages assigned
to a student is minimum. (n <= 10**5)
"""

def good(arr, s, mid):
	students_req = 1
	pages_read_by_curr_student = 0

	for i in range(len(arr)):
		if arr[i] > mid:
			return False
		if pages_read_by_curr_student + arr[i] > mid:
			students_req += 1
			pages_read_by_curr_student = arr[i]

			if students_req > s:
				return False
		else:
			pages_read_by_curr_student += arr[i]

	return True

def books(arr, s):
	low, high = 0, sum(arr)
	ans = 10**9

	while low <= high:
		mid = low + (high - low) // 2

		if good(arr, s, mid):
			high = mid - 1
			ans = mid
		else:
			low = mid + 1
	return ans

arr = [int(x) for x in input().split()]
m = int(input())

print(books(arr, m))

