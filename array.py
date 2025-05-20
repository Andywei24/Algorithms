import random

arr: list[int] = [0] * 5
nums: list[int] = [1, 3, 2, 5, 4]

def random_access(nums):
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num

print(random_access(nums))


def insert(nums : list[int], num : int, index : int):
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num

def delete(nums, index):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]
