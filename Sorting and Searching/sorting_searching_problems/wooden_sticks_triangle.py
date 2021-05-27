"""
Q -> Not a Triangle (NOTATRI)

You have N (3 <= N <= 2000) wooden sticks, which are labelled from 1 to N. 
The i-th stick has a length of Li (1 <= Li <= 10^6). You friend has challenged you
to a simple game: you will pick three sticks at random, and if your friend can 
form a triangle with them( degenerate triangles included), he wins; otherwise,
you win. You are not sure if your friend is trying to trick you, so you would 
like to determine your chances of winning by computing the number of ways you
could choose three sticks(regardless of order) such that it is impossible to 
form a triangle with them.

INPUT -> The input file consists of multiple test cases. Each test case starts 
with the single integer n, followed by a line with the integers L1,.....,Ln. 
The input is terminated with N = 0, which should not be processed.

OUTPUT -> For each test case, output a single line containing the number of 
triples.

EXAMPLE -> 

Input:
3
4 2 10
3
1 2 3
4
5 2 9 6
0

Output:
1 (4,2,10)
0
2 (5,2,9 and 2,9,6)

Explanation:
For the first test case, 4 + 2 < 10, so you will win with the one availble triple.
For the second case, 1 + 2 = 3; since degenerate triangles are allowed, the 
answer is 0.

Logic ->
That for any 2 sides a,b , if we find all the possible c's such that a + b < c, 
then we will have all those as the answer.
"""

import bisect

n = int(input())

while True:
	li = [int(x) for x in input().split()]
	li.sort()
	ans = 0

	for i in range(0, n - 2):
		for j in range(i + 1, n - 1):
			ans = ans + (len(li) - bisect.bisect_right(li, li[i] + li[j]))

	print(ans)

	n = int(input())
	if n == 0:
		break

