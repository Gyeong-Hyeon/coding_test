def widestGap(n: int, start: list, finish: list) -> int:
    import re

    road = '0'*n
    for s,f in zip(start, finish):
        car_length = f-s+1
        road = road[:s-1] + '1'*car_length + road[f:]
    
    gaps = re.split(r'1+', road)
    widest_gap = max(list(map(lambda x : len(x), gaps)))

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
    
    #문제 풀이 소요시간 58분