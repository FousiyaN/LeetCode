"""
LeetCode #28 - Find the Index of the First Occurrence in a String

Approach:
Used Python's built-in find() function.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def strStr(self, haystack, needle):
            return(haystack.find(needle))
