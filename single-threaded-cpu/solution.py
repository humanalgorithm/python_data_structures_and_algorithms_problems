class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        task_heap, result = [], []

        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x: x[0])

        counter = 0
        time = tasks[0][0]

        while task_heap or counter < len(tasks):
            while counter < len(tasks) and time >= tasks[counter][0]:
                heapq.heappush(task_heap, [tasks[counter][1], tasks[counter][2]])
                counter += 1
            if not task_heap:
                time = tasks[counter][0]
            else:
                proc_time, index = heapq.heappop(task_heap)
                time += proc_time
                result.append(index)
        return result

