

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        course_map = defaultdict(list)
        for prereq in prerequisites:
            course_map[prereq[0]].append(prereq[1])

        stack, visited, cycle = [], set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in course_map.get(course, []):
                if not dfs(pre):
                    return False
            visited.add(course)
            cycle.remove(course)
            stack.append(course)
            return True

        for x in range(0, numCourses):
            if x in visited:
                continue
            result = dfs(x)
            if not result:
                return []
        return stack
