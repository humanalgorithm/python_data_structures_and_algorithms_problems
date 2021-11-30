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
            cycle.add(course)
            for pre in course_map.get(course, []):
                if pre in visited:
                    continue
                if pre in cycle:
                    return False
                result = dfs(pre)
                if not result:
                    return False
            cycle.remove(course)
            visited.add(course)
            stack.append(course)
            return True

        for x in range(0, numCourses):
            if x not in visited:
                result = dfs(x)
            if not result:
                return []
        return stack
