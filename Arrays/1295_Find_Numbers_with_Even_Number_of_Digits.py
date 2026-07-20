class Solution(object):
    def findNumbers(self,nums):
        flag = 0
        for i in range(len(nums)):
            temp = nums[i]
            count = 0
            while temp>0:
                count = count+1
                temp=temp//10
            if count%2==0:
                flag += 1
