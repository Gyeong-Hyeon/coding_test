class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        1. Rotate s1 by it's charaters and make hash table which has char as key and number of the char in s1 as value
            Only when all hash table's values become 0 (=We used all characters & same amount/characters in s1), we can return True
        2. From index 0 to len(s1) (=means a sliding window becomes s2[0:len(s1)]), check a character one by one if it's in the hash table or not.
            - If s2[i] in s1:
                - We use this char for making ss, so -1 to hash table[s[i]]
                - After -1, if hash table[s[i]] becomes 0, count+1 to return True when all key's value become 0
                - But s2[i] can be -1 in case the substring used all amount of this char it can use. This substring can't be a permutation of s1 so we need to return back the value of ht[s2[i]] and count.
        3. If index >= len(s1) but the function didn't return True yet, that means a permutation of s1 is not founded yet and we need to move the sliding window's end from index-1 to index. When it moved, index-len(sliding window)'s value will be removed from and index's value will be added to the previous sliding window. In conclusion, keep proceed 2. for s2[index] and add process to check value of s2[index-len(sliding window)] from now.
            - If i >= len(s1) and s2[i-len(s1)] in s1:
                - If hash table[s2[i-len(s1)]] == 0: We need to return the count back(which plused in the previous loop) because this character will not be used to make ss. So count-1
                - Return back the hash table[s2[i-len(s1)]]'s value
                - If hash table[s2[i-len(s1)]] becomes 0 after returning back it's value, then now the sliding window is using same amount of the char with s1. So add 1 to count.
        """
        ht = {}
        #we can use python function Counter instead of the below for loop
        for c in s1:
            if ht.get(c):
                ht[c]+=1
                continue
            ht[c]=1
        #######
        cnt, l = 0, len(s1)
        for i in range(len(s2)):
            if s2[i] in ht: #don't use ht.get(s2[i]) because it'll pass if block when ht[s2[i]]'s value is 0
                if not ht[s2[i]]: cnt-=1
                ht[s2[i]]-=1
                if not ht[s2[i]]: cnt+=1
            if i >= l and s2[i-l] in ht:
                if not ht[s2[i-l]]: cnt-=1
                ht[s2[i-l]]+=1
                if not ht[s2[i-l]]: cnt+=1
            if cnt == len(ht):
                return True
        return False
