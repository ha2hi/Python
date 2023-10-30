# Two Sum
def TwoSum(nums: list[int], target: int) -> list:
    nums_dict = {}
    for idx, num in enumerate(nums):
        nums_dict[num] = idx
    
    for idx, num in enumerate(nums):
        if target-num in nums_dict and idx != nums_dict[target-num]:
            return [idx, nums_dict[target-num]]

nums = [2,7,11,15]
target = 9
TwoSum(nums, target)
