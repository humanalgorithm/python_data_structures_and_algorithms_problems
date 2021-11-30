class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        course_dict = defaultdict(list)

        for pre in prerequisites:
            course_dict[pre[0]].append(pre[1])

        output = []
        visited = set()
        for course in range(0, numCourses):
            result = self.searchCourse(course, visited, course_dict, set(), output)
            if not result:
                return False
        return output

    def searchCourse(self, course, visited, course_dict, cycle, output):
        if course in cycle:
            return False
        if course in visited:
            return True

        cycle.add(course)
        for pre in course_dict.get(course, []):
            result = self.searchCourse(pre, visited, course_dict, cycle, output)
            if not result:
                return False

        cycle.remove(course)
        visited.add(course)
        output.append(course)
        return True

