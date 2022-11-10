class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. Set the first searching area from the first value of the input array and the last value of the array
        2. If the target is same with the middle value of the searching area, return the middle value's index
        3. If the target is smaller than the middle value of the searching area, move "high" to the right left value of the middle value of the searching area
        4. If the target is bigger than the middle value of the searching area, move "low" to the right right middle value of the searching area
        5. Repeat 2~4 to narrow down the searching area
        6. If target is not found until searching area has one value only, return -1
        """
        if not nums: return -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1            