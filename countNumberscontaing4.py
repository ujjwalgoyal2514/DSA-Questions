"""You are given a number n, Return the count of total numbers from 1 to n containing 4 as a digit.

Examples:

Input: n = 9
Output: 1
Explanation: 4 is the only number between 1 to 9 which contains 4 as a digit.
Input: n = 14
Output: 2
Explanation: 4 and 14 are the only number between 1 to 14 that contains 4 as a digit.
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 105

"""
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        c=0
        for i in range(1,n+1):
            if '4' in str(i):
                c+=1
        return c