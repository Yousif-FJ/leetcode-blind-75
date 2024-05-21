def twoSum(self, nums : list[int], target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map = dict()
    for i in range(0, len(nums)):
        indexOfTheNumber = map.get(target - nums[i])
        if indexOfTheNumber != None and i != indexOfTheNumber:
            return [i, indexOfTheNumber]
        else : map[nums[i]] = i
        
result = twoSum(None, [2,7,11,15], 9)
print(result)

result = twoSum(None, [3,2,4], 6)
print(result)

result = twoSum(None, [3,3], 6)
print(result)
