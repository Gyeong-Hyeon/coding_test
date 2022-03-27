def cutThemAll(lengths, minLength):
    while len(lengths) > 1:
        if sum(lengths) < minLength:
            return "Impossible"
            
        if lengths[0] < lengths[-1]:
            lengths.pop(0)
        else:
            lengths.pop()
    return "Possible"
        
if __name__ == "__main__":
    print(cutThemAll([3,5,4,3],9))
    print(cutThemAll([4,3,2],7))
    print(cutThemAll([4,2,3],7))