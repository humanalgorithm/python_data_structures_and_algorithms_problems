import heapq
from collections import defaultdict


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = defaultdict(int)
        heap_task = []

        for char in tasks:
            task_count[char] += 1

        for key, value in task_count.items():
            heap_task.append((-value, key))

        heapq.heapify(heap_task)

        count = 0
        while heap_task:
            used_tasks, used_tasks_count = [], 0
            for i in range(0, n + 1):
                if not heap_task:
                    break
                used_tasks_count += 1
                task = heapq.heappop(heap_task)
                new_task = (task[0] + 1, task[1])
                used_tasks.append(new_task) if new_task[0] != 0 else None

            heap_task += used_tasks
            heapq.heapify(heap_task)

            count = count + used_tasks_count if not heap_task else count + n + 1
        return count
