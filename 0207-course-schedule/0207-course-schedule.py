class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule = {}
        for s, f in prerequisites:
            if s == f:
                return False

            nodes = schedule.get(s, [])[:]
            while nodes:
                node = nodes.pop(0)
                if f == node:
                    return False
                to_visit = schedule.get(node)
                if not to_visit:
                    continue
                if f in to_visit:
                    return False
                nodes.extend(to_visit)
            schedule[f] = schedule.get(f,[]) + [s]
        return True