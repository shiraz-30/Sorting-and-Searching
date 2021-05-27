"""
Farmer John has built a new long barn, with N(2 <= N <= 10**5) stalls. The stalls 
are located along a straight line t positions x1,...,xN(0 <= xi <= 10**9).
His C(2 <= C <= N) cows don't like this barn layout and become aggressive 
towards each other once put into a stall. To prevent the cows from hurting each
other, Farmer John wants to assign the cows to the stalls, such that the 
minimum distance between any two of them is as large as possible. 
What is the largest minimum distance?

INPUT ->
t - the number of test cases, then t test cases follows.
*Line 1: Two space seperated integers: N and C
*Lines 2...N + 1: Line i + 1 contains an integer stall location, xi

OUTPUT ->
For each test case output one integer: the largest minimum distance.

EXAMPLE->
Input:
1
5 3
1
2
8
4
9

Output:
3

Explanation:
Farmer John can put his 3 cows in the stalls at positions 1, 4 and 8, resulting
in a minimum distance of 3.
"""

def good(mid, barn, cows):
	count = 1
	last_position = barn[0] # the last stall where you put a cow

	for i in range(1, len(barn)):
		if barn[i] - last_position >= mid: # distance between last cow and current cow is atleast mid
			count += 1 # yes, put a cow here
			last_position = barn[i]
		if count >= cows:
			return True

	return False

t = int(input())

for i in range(t):
	n, c = [int(x) for x in input().split()]
	barn = []

	for i in range(n):
		x = int(input())
		barn.append(x)

	barn.sort()
	low = 1
	high = barn[len(barn) - 1]
	ans = -1

	while low <= high:
		mid = low + (high - low) // 2

		if good(mid, barn, c):
			ans = mid
			low = mid + 1
		else:
			high = mid - 1

print(ans)
