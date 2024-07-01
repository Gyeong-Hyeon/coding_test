class MedianFinder:
    def __init__(self):
        self.num_list = []
        
    def addNum(self, num: int) -> None:
        if not self.num_list or num >= self.num_list[-1]:
            self.num_list.append(num)
            return
        s=0
        while self.num_list[s] < num:
            s+=1
        self.num_list.insert(s, num)

    def findMedian(self) -> float:
        l = len(self.num_list)
        idx = int(l/2)
        if l%2: #홀수
            return float(self.num_list[idx])
        return (self.num_list[idx] + self.num_list[idx-1])/2