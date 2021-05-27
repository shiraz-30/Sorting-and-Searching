def counting_sort(arr):
	# in this implementation we will assume that we get only positive values
	max_element = max(arr)
	freq = [0]*(max_element + 1)

	# this loop will help to create the frequency list
	for i in range(0, len(arr)):
		freq[arr[i]] += 1

	# now we need to prepare prefix sum
	for i in range(1, len(freq)):
		freq[i] = freq[i] + freq[1 - 1]

	output = [0]*len(arr)
	for i in range(len(arr) - 1, -1, -1): # going from previous
		output[freq[arr[i]] - 1] = arr[i]
		freq[arr[i]] -= 1

	return output

	
li = list(map(int, input().split()))

output = counting_sort(li)

print(output)

"""
T.C. -> O(n + K), θ(n + K), Ω(n + K)
S.C. -> O(n + K)
No. of comparisons -> No
No. of swaps -> No
In place -> No
Stability -> Stable
"""


