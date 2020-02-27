class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = []
        for subset in self.subsets(nums[1::]):
            ans.append(subset[:])
            subset.append(nums[0])
            ans.append(subset[:])
        return ans
        
