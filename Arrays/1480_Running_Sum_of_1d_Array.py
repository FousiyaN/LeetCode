class Solution(object):
    def runningSum(self, nums):
        newlist=[]
        sum=0
        for i in range(0,len(nums)):
            sum += nums[i]
            newlist.append(sum)
        return newlist
