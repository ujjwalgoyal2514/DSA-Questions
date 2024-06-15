"""There is a standard numeric keypad on a mobile phone. You can only press the current button or buttons that are directly up, left, right, or down from it (for ex if you press 5, then pressing 2, 4, 6 & 8 are allowed). Diagonal movements and pressing the bottom row corner buttons (* and #) are prohibited.



Given a number n, find the number of possible unique sequences of length n that you can create by pressing buttons. You can start from any digit.

Examples

Input: n = 1
Output: 10
Explanation: Number of possible numbers are 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  
Input: n = 2
Output: 36
Explanation: Possible numbers: 00, 08, 11, 12, 14, 22, 21, 23, 25 and so on. If we start with 0, valid numbers will be 00, 08 (count: 2). If we start with 1, valid numbers will be 11, 12, 14 (count: 3). If we start with 2, valid numbers  will be 22, 21, 23,25 (count: 4). If we start with 3, valid numbers will be 33, 32, 36 (count: 3). If we start with 4, valid numbers will be 44,41,45,47 (count: 4). If we start with 5, valid numbers will be 55,54,52,56,58 (count: 5) and so on.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 25"""
class Solution:
    def getCount(self, n):
        dp = [1]*10
       
        for i in range(1, n):
            temp = [0]*10
            temp[0] = dp[0] + dp[8]
            temp[1] = dp[1] + dp[2] + dp[4]
            temp[2] = dp[1] + dp[2] + dp[3] + dp[5]
            temp[3] = dp[2] + dp[3] + dp[6]
            temp[4] = dp[1] + dp[4] + dp[5] + dp[7]
            temp[5] = dp[2] + dp[4] + dp[5] + dp[6] + dp[8]
            temp[6] = dp[3] + dp[5] + dp[6] + dp[9]
            temp[7] = dp[4] + dp[7] + dp[8]
            temp[8] = dp[5] + dp[7] + dp[8] + dp[9] + dp[0]
            temp[9] = dp[6] + dp[8] + dp[9]
            dp = temp
       
        return sum(dp)