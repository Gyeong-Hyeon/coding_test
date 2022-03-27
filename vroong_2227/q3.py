def maxDifference(px):
    min_px = px[0]
    max_diff = -1
    for i in range(1, len(px)):
        if px[i] > min_px:
            diff = px[i]-min_px
            if diff <= max_diff:
                continue
            max_diff = diff
        else:
            min_px = min(px[:i+1])

    return max_diff

if __name__ == "__main__":
    test_sets = ([7,5,3,1],[7,1,2,5],[2,3,10,2,4,8,1])
    answers = (-1,4,8)
    for test_set, answer in zip(test_sets, answers):
        result = maxDifference(test_set)
        try:
            assert result == answer
            print('정답이 일치합니다.')
        except AssertionError:
            print('정답이 일치하지 않습니다')
            print(f'테스트 케이스:{test_set}',f'정답:{answer}',f'결과값:{result}')
    