class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        node = {
            'opened': 1,
            'closed': 0,
            'comb': '('
        }
        ans = []
        to_visit = [None]

        while node:
            opened, closed = node['opened'], node['closed']
            if opened == n:
                comb = node['comb'] + (')'*(opened-closed))
                ans.append(comb)
                node = to_visit.pop()
                continue
            if closed < opened:
                to_visit.append({
                    'opened': opened,
                    'closed': closed+1,
                    'comb': node['comb'] + ')'
                })
            node['opened']+=1
            node['comb']+='('
        return ans