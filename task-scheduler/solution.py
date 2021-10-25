import heapq
import sys


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks = sorted(tasks)
        i = 0
        task_heap = []
        while i < len(tasks):
            count_tasks = tasks.count(tasks[i])
            task = (-1 * count_tasks, count_tasks, tasks[i])
            i += count_tasks
            task_heap.append(task)

        counter, idle, task_history = 0, 0, []
        while task_heap:
            self.update_task_heap(task_heap, counter, n, task_history)
            heapq.heapify(task_heap)
            task = heapq.heappop(task_heap)
            task_time, task_count, task_name = task[0], task[1], task[2]

            if task_name not in task_history:
                idle = 0
            else:
                idle = n - (counter - task_time)

            while idle > 0:
                idle -= 1
                counter += 1

            counter += 1
            task_history.append(task_name)
            if task_count - 1 > 0:
                updated_task = (counter, task_count - 1, task_name)
                heapq.heappush(task_heap, updated_task)
        return counter

    def update_task_heap(self, task_heap, counter, n, task_history):
        for task in list(task_heap):
            task_time, task_count, task_name = task[0], task[1], task[2]
            elapsed_time = (n - (counter - task_time))

            if task_name in task_history and elapsed_time <= 0:
                task_time = -1 * task_count
                updated_task = (task_time, task_count, task_name)
                task_heap.remove(task)
                task_heap.append(updated_task)
