class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels, cnt, start, is_vowel = ['a','e','i','o','u'], 0, 0, [False]*len(s)
        for i in range(k):
            if s[i] in vowels:
                cnt+=1
                is_vowel[i] = True
        
        ans = cnt
        for i in range(k,len(s)):
            if s[i] in vowels:
                is_vowel[i] = True
                if not is_vowel[start]:
                    cnt+=1
                    ans = max(ans,cnt)
            elif is_vowel[start]:
                cnt-=1
            start+=1
        return ans