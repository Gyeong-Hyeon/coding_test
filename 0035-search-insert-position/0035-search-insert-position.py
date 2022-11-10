class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1. Set the search array same with the input array
        2. If the middle value is same with target, return the index of the middle value
        3. If the target is not found until low gets bigger than high, return low
        While statement continues to narrow down the searching array untill the array is either:
            Case 1. 2 values in the searching array:
                - "high" is pointing the last index of searching array
                - "low" and "mid" is pointing the first index of searching array
            Case 2. 1 value in the searching array:
                - "high", "low", "mid" is pointing a same index
            That means the last comparing steps is actually comparing "low" value and the target (because "mid" value is same with "low" value).
            If the target value is bigger than "low" value, the while statement excuted once more because "low" becomes same with "high".
            Else(=that means the target value is smaller than "low"), "high" becomes smaller than "low"(because of mid-1) and while statement terminates. The index where the target would be is where "low" value is (because it's smaller than "low"), so, return "low".
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