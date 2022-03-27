def widestGap(n: int, start: list, finish: list) -> int:
    import re

    road = '0'*n
    for s,f in zip(start, finish):
        car_length = f-s+1
        road = road[:s-1] + '1'*car_length + road[f:]
    
    # gaps = re.split(r'1+', road)
    # widest_gap = max(list(map(lambda x : len(x), gaps)))
    
    cnt=0
    widest_gap=0
    
    for gap in road:
        if gap == '1':
            cnt=0
            continue
        
        elif gap == '0':
            cnt+=1

        if cnt > widest_gap:
            widest_gap = cnt         
    return widest_gap

if __name__ == "__main__":
    test_sets = ((10,[3,8],[4,9]),(10,[1,2,5,8],[2,2,6,10]),(10,[3,8,2],[4,9,5]))
    answers = (3,2,2)
    
    for test_set, answer in zip(test_sets, answers):
        result = widestGap(*test_set)
        try:
            assert result == answer
            print('정답이 일치합니다.')
        except AssertionError:
            print('정답이 일치하지 않습니다')
            print(f'테스트 케이스:{test_set}',f'정답:{answer}',f'결과값:{result}')
    
    widestGap(1000,[522,575,426,445,772,81,447,629,497,202],[676,803,657,500,835,196,718,830,680,919])

    #문제 풀이 소요시간 58분