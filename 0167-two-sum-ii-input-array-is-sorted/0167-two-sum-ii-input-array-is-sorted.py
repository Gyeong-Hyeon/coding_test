class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. start = 0, end = 0
        2. start value is the first value of the array, and end value is the last value of the array
        3. if array[start] + array[end] == target : return start+1, end +1
        4. else: move start or end
        """
        start, end= 0, len(numbers)-1
        while start != end:
            compare = numbers[start] + numbers[end]
            if compare == target:
                return [start+1, end+1]
            if compare > target:
                end-=1
            else:
                start+=1