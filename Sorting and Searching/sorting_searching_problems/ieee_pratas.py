"""
IEEE is having its AGM next week and the president wants to serve cheese prata
after the meeting. The subcommittee members are asked to go to the food connection
and get P(P <= 1000) pratas packed for the function. The stall has L cooks
(L <= 50) and each cook has a rank R(1 <= R <= 8). A cook with a rank R can 
cook 1 prata in the first R minutes 1 more prata in the next 2R minutes, 1 more
prata in 3R minutes and so on( he can only cook a complete prata) (For example
if a cook is ranked 2.. he will cook one prata in 2 minutes one more prata in 
the next 4 mins an one more in the next 6 mins hence in total 12 mins he cooks
3 pratas in 13 mins also he can cook only 3 pratas as he does not have enough
time for the 4th prata). The webmaster wants to know the minimum time to get 
the order done. Please write a program to help him out.

INPUT ->
The first line tells the number of test cases. Each test case consist of 2 lines.
In the firs line of the test case we have P the number of prata ordered. In the
next line the first integer denotes the number of cooks L and L integers follow
in the same line each denoting the rank of a cook.

OUTPUT -> 
Print an integer which tells the number of min minutes needed to get the order done.

EXAMPLE ->

Input:
3
10
4 1 2 3 4
8
1 1
8
8 1 1 1 1 1 1 1 1 

Output:
12
36
1
"""

def good(arr, n, p, mid):
	count = 0
	for i in range(0, n):
		alloted_time = mid
		pratas_by_current_chef = 0
		time_by_current_chef = arr[i] # rank R of the ith chef

		while alloted_time > 0:
			alloted_time = alloted_time - time_by_current_chef
			if alloted_time >= 0:
				pratas_by_current_chef += 1
				time_by_current_chef += arr[i]

		count += pratas_by_current_chef
		if count >= p:
			return True
	return False

t = int(input())
for i in range(0, t):
	p = int(input())
	arr = [int(x) for x in input().split()]
	n = arr.pop(0)

	low, high = 0, 10**7
	ans = -1

	while low <= high:
		mid = low + (high - low) // 2
		if good(arr, n, p, mid):
			high = mid - 1
			ans = mid
		else:
			low = mid + 1
	print(ans)

