"""
You are given a set S of integers between -30000 and 30000 (inclusive).
Find the total number of sextuples(a, b, c, d, e, f): a, b, c, d, e, f belongs to 
S; d != 0 that satisfy: ((a * b + c)/d - e) = f

INPUT -> 
The first line contains integer N(1 <= N <= 100), the size of a set S.
Elements of S are given in the next N lines, one integer per line.
Given numbers will be distinct.

OUTPUT -> 
Output the total number of plausible sextuples.

EXAMPLES ->
Input:    Input:   Input:    Input:
1         2        2         3
1         2        - 1       5 
          3        1         7
                             10

Output:   Output:  Output:   Output:
1         4        24        10

"""

    