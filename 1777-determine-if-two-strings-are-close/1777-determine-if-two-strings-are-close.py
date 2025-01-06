class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1, cnt2 = OrderedDict(sorted(Counter(word1).items())), OrderedDict(sorted(Counter(word2).items()))
        rev_cnt2 = {}
        for k,v in cnt2.items():
            rev_cnt2[v] = rev_cnt2.get(v,[]) + [k]

        for (cnt1_k, cnt1_v), (cnt2_k, cnt2_v) in zip(cnt1.items(), cnt2.items()):
            if cnt1_k != cnt2_k:
                return False
            if cnt1_v == cnt2_v:
                rev_cnt2[cnt2_v].remove(cnt2_k)
                continue
            if not rev_cnt2.get(cnt1_v):
                return False
            new_key = rev_cnt2[cnt1_v].pop()
            rev_cnt2[cnt2_v].remove(cnt2_k)
            rev_cnt2[cnt2_v].append(new_key)
            cnt2[cnt2_k], cnt2[new_key] = cnt2[new_key], cnt2[cnt2_k]
        return True