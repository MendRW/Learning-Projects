# Given an array of integers return indices of the two numbers such that they add up to a specific target

# You may assume that each input would have exactly one solution and you may not use the same element twice

# Array of numbers exampple [1,2,5,3] target = 4 answer would be 3 and 1
# add the first element to the others, if it is = 4 we break loop. if we don't reach the answer then we repeat with the next number in the array
# this is n.n = o(n^2)
#how can we make this better? if our target is 4 we can instead match for the remaiing value to reach it
# 4-1 = 3 this means for each loop we just need to check for 3

class Solution:
    def twosum(self ,nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
