class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        if not firstList or not secondList:
            return ans
        
        pf, ps = 0, 0
        while pf < len(firstList) and ps < len(secondList):
            sf, ef, ss, es = firstList[pf][0], firstList[pf][1], secondList[ps][0], secondList[ps][1]
            
            if sf <= ss:
                if ef <= es:
                    if ef >= ss:
                        ans.append([ss, ef])
                    pf+=1
                    continue
                else:
                    ans.append([ss, es])
                    ps+=1
                    continue
            if ef <= es:
                ans.append([sf, ef])
                pf+=1
                continue
            elif sf <= es:
                ans.append([sf, es])
            ps+=1
        return ans