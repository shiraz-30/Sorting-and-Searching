def merge(a, b):
	n = len(a) # legnth of the first list
	m = len(b) # length of the second list
	output = [0]*(n + m) # final output list which will be returned
	i, j, k = 0, 0, 0 # i => left list index, j => right list index, k => mid index

	while (i < n and j < m):
		if a[i] < b[j]:
			output[k] = a[i]
			i += 1
			k += 1
		else:
			output[k] = b[j]
			j += 1
			k += 1

	while (j < m):
		# list b is remaining and a is exhausted
		output[k] = b[j]
		j += 1
		k += 1

	while (i < n):
		# list a is remaining and b is exhausted
		output[k] = a[i]
		i += 1
		k += 1

	return output


def merge_sort(arr, left, right):
	if (left == right):
		# base case
		return [arr[left]] # or return [arr[right]]

	mid = (left + right) // 2

	left_half = merge_sort(arr, left, mid) # recursively we extracted the left sorted part 
	right_half = merge_sort(arr, mid + 1, right) # recursively we extracted the right sorted part
	output = merge(left_half, right_half) # merged both the halves

	return output 

li = list(map(int, input().split()))
print("Before sort", li)
output = merge_sort(li, 0, len(li) - 1)
print("After sort", output)


"""
TC -> O(nlog(n)), θ(nlog(n)), Ω(nlog(n))
SC -> O(n)
No. of comparisons -> O(nlog(n))
No. of swaps -> No
In place -> No
Stability -> Stable
"""


