class MedianFinder:
    def __init__(self):
        self.num_list = []
        
    def addNum(self, num: int) -> None:
        if self.num_list and num <= self.num_list[0]:
            self.num_list.insert(0,num)
            return
        self.num_list.append(num)
        if len(self.num_list) > 1 and num < self.num_list[-2]:
            self.num_list.sort()

    def findMedian(self) -> float:
        l = len(self.num_list)
        idx = int(l/2)
        if l%2: #홀수
            return float(self.num_list[idx])
        return (self.num_list[idx] + self.num_list[idx-1])/2