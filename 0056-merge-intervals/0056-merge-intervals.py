class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        pre_start, pre_end = intervals[0]
        ans = []
        for start, end in intervals[1:]:
            if start > pre_end:
                ans.append([pre_start, pre_end])
                pre_start, pre_end = start, end
                continue
            if end > pre_end:
                pre_end = end
        ans.append([pre_start, pre_end])
        return ans