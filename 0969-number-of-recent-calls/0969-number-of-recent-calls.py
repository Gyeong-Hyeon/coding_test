class RecentCounter:
    def __init__(self):
        self.counter = 0
        self.ts = []
        self.start = 0
    
    def ping(self, t: int) -> int:
        self.ts.append(t)
        target = t-3000
        while self.ts[self.start] < target:
            self.start+=1
        return len(self.ts)-self.start