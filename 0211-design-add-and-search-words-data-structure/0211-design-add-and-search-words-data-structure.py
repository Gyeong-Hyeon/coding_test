class WordDictionary:
    def __init__(self):
        self.words = {chr(k):{} for k in range(97,123)}

    def addWord(self, word: str) -> None:
        node = self.words[word[0]]
        for char in word[1:]:
            if not node.get(char):
                node[char] = {}
            node = node[char]
        node['0'] = True

    def search(self, word: str, words=None) -> bool:
        if words is None:
            words = self.words
        
        if word == '0':
            return words.get('0', False)
        
        if words.get(word[0]):
            if len(word) == 1:
                word+='0'
            return self.search(word[1:], words[word[0]])

        if word[0] == '.':
            if len(word) == 1:
                word+='0'
            for k in words.keys():
                if k == '0':
                    continue
                if self.search(word[1:], words[k]):
                    return True
        return False