def subsets(nums):
    # n^2 solution seems simple how to optimize?
    # Need to store paths
    def _subsets(nums):
        if len(nums) == 1:
            return [[nums[0]]]
        mid = len(nums) // 2
        return [nums,*_subsets(nums[:mid]),*_subsets(nums[mid:])]

    return _subsets(nums)

nums = [1,2,3]
print(subsets(nums))