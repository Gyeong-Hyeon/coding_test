def findSubstrings(s):
    cnt = len(s)
    for i in range(2, len(s)+1):
        for j in range(len(s)-i+1):
            ss = set(s[j:j+i])
            if len(ss) != i:
                continue
            cnt+=1

    return cnt

if __name__ == "__main__":
    assert findSubstrings("bcada") == 12
    assert findSubstrings("abcd") == 10
    assert findSubstrings("aaaba") == 7

#문제풀이 소요시간 31분