class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                count+=1
                nums[i],nums[j+1]=nums[j+1],nums[i]
                j+=1
        return count
