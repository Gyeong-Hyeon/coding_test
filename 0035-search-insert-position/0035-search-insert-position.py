class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1. Set the search array same with the input array
        2. If the middle value is same with target, return the indext of the middle value
        3. If the target is not found until the search array == False, return high+1
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return low