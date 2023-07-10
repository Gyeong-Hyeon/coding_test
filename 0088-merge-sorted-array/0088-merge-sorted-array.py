class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        if not m:
            nums1[:] = nums2
            return
        p1, p2, left = 0, 0, m
        while left and p2 < n:
            if nums1[p1] <= nums2[p2]:
                p1+=1
                left-=1
                continue
            nums1[p1], nums1[p1+1:p1+left+1] = nums2[p2], nums1[p1:p1+left] 
            p1+=1
            p2+=1
        if p2 < n:
            nums1[p1:] = nums2[p2:]
        return