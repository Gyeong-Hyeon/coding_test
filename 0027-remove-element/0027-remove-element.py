class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1, p2 = 0, len(nums)-1
        while p1 <= p2:
            if nums[p1] != val:
                p1+=1
                continue
            nums[p1] = nums[p2]
            p2-=1
        return p1