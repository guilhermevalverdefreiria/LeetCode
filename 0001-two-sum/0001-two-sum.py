class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = len(nums) #Tamanho da lista
        for i in range(a):
            for j in range(i+1, a): 
                if nums[i] + nums[j] == target:
                    return [i,j]
            




        