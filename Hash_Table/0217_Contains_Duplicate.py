class Solution(object):
    def containsDuplicate(self, nums):
        lengthoflist = len(nums)
        temp = set(list(nums))
        lengthofset = len(temp)
        if(lengthoflist==lengthofset):
            return False
        else:
            return True
