class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1. Set the search array same with the input array
        2. If the middle value is same with target, return the index of the middle value
        3. If the target is not found until low gets bigger than high, return low
        While loop terminates(low>high) when the last step was the below case:
            1. low and high was pointing the same value = searching area has one value only
            (because each step of the loop, either low and high increase 1 only)
            2. mid was also pointing the same value because high+low//2 = mid = 2high//2
            3. target is bigger than mid because low increases in this case only
            4. low becomes low+1 and it means it's same with mid+1=high+1
            5. It's bigger than high, breaks the loop
        idx should be mid+1 following 3 - which is same with the current low. So retrun low
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
