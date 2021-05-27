"""
Petya has the word t, he wants to make the word p from it. Petya begins to 
delete the letters in a certain order, which is described as a permutation of
indices of the letters of the owrd t: a1.....at. Note that after deleting a
letter, the numbering does not change.
His brother Vasya is afraid that Petya may delete too many letters, so he will
not get the word p in the end. Vasya's task is to stop his brother at some 
point and finish deleting himself in such a way, that the resulting word
will be p. Since Petya likes this activity, Vasya wants to stop him as late
as possible. Your task is to tell how many letters Petya can delete out 
before Vasya stops him.
It is guaranteed that the word p can be obtained by deleting letters from t.

INPUT ->
The first and second lines of the input file contain the words t and p, respectively.
Words consist of lowercase letters of the Latin alphabet( 1 <= |p| < |t| <= 200000).
The next line contains the permutations a1.....at of letter indices, which
specifies the order in which Petya deletes the letters of the word t(1 <= ai < |t|,
all ai are different).

OUTPUT ->
Print one number, the maximum number of letters that Petya can delete.

EXAMPLE ->
t = ababcba
p = abb
[5, 3, 4, 1, 7, 6, 2]
ans = 3
"""

def check(mid, t, p, arr):
	temp = "" # temp will show how t looks after mid deletions
	s = set()

	for i in range(0, mid):
		s.add(arr[i] - 1)
	len_t = len(t)

	for i in range(0, len_t):
		if i not in s:
			temp += t[i]

	i, j, len_temp, len_p = 0, 0, len(temp), len(p)
	while i < len_temp and j < len_p:
		if i < len_temp and temp[i] != p[j]:
			i += 1

		elif i < len_temp and j < len_p and temp[i] == p[j]:
			i += 1
			j += 1

	return j == len_p

t = input()
p = input()
arr = [int(x) for x in input().split()]

if len(p) == 0:
	print(len(t))

low, high = 0, len(t) - len(p) + 1

while (low <= high):
	mid = low + (high - low) // 2

	if check(mid, t, p, arr) == True:
		ans = mid
		low = mid + 1
	else:
		high = mid - 1

print(ans)

