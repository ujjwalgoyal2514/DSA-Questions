"""Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist). The array is guaranteed to be in ascending order before the peak element and in descending order after it.

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Example 1:

Input: 
n = 3
arr[] = {1, 2, 3}
Peak Element's Index: 2
Output: 1
Explanation: 
If the index returned is 2, then the output printed will be 1. 
Since arr[2] = 3 is greater than its adjacent elements, and 
there is no element after it, we can consider it as a peak 
element. No other index satisfies the same property.
Example 2:

Input:
n = 3
arr[] = {3, 4, 2}
Peak Element's Index: 1
Output: 1
Explanation: 
If the index returned is 1, then the output printed will be 1.
Since arr[1] = 4 is greater than its adjacent elements, and
there is no element after it, we can consider it as a peak
element. No other index satisfies the same property.
Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size n as input parameters and return the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106
"""
# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        max=arr[n-1]
        index=n-1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                if max<arr[i]:
                    max=arr[i]
                    index=i
        return index