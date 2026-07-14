class Solution(object):
    def maximumWealth(self, accounts):
        newlist=[]
        for row in range(len(accounts)):
            sum=0
            for column in range(len(accounts[row])):
                sum+=accounts[row][column]
            newlist.append(sum)
        return max(newlist)
        
