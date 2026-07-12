class Solution(object):
    def isPalindrome(self, x):
        o_num = x
        rev=0
        while x>0:
            a=x%10
            rev=(rev*10)+a
            x=x//10
        if rev==o_num:
            return True
        else:
            return False

        
