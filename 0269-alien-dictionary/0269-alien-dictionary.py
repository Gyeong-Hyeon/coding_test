class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d = {char: [] for word in words for char in word}

        for word_1, word_2 in zip(words, words[1:]):
            for char_1, char_2 in zip(word_1, word_2):
                if char_1 != char_2:
                    d[char_2].append(char_1)
                    break
            else:
                if len(word_1) > len(word_2):
                    return ""
        
        visited, answer = {}, []
        def visit(node):
            if node in visited:
                return visited[node]
            visited[node] = False
            for next_node in d[node]:
                if not visit(next_node):
                    return False
            visited[node] = True
            answer.append(node)
            return True
        
        if not all(visit(node) for node in d):
            return ""
        return "".join(answer)