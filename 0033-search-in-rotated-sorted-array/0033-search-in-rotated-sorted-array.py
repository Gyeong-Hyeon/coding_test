class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[-1]:
                left = mid+1
            else:
                right = mid-1

        def binarySearch(sub_array:list, pivot:int=0):
            sub_left, sub_right = 0, len(sub_array)-1
            while sub_left <= sub_right:
                sub_mid = (sub_left+sub_right)//2
                if sub_array[sub_mid] == target:
                    return sub_mid + pivot
                if sub_array[sub_mid] < target:
                    sub_left = sub_mid+1
                else:
                    sub_right = sub_mid-1
            return -1
