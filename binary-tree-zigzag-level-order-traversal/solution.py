# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Queue import Queue
from collections import defaultdict


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level, prev_level, node_print_dict = 0, 0, defaultdict(list)
        reverse_bfs, queue = True, Queue()

        queue.put((root, 0))
        while not queue.empty():
            node_data = queue.get()
            node, level = node_data
            if level > prev_level:
                queue = self.reverse_queue(queue, node_data)
                node, level = queue.get()
                reverse_bfs = not reverse_bfs
            prev_level = level
            node_print_dict[level].append(node.val)
            if reverse_bfs:
                self.add_right_to_left(node, queue, level + 1)
            else:
                self.add_left_to_right(node, queue, level + 1)
        return self.parse_node_print_dict(node_print_dict)

    def add_right_to_left(self, node, queue, level):
        if node.left and node.left.val != None:
            queue.put((node.left, level))

        if node.right and node.right.val != None:
            queue.put((node.right, level))

    def add_left_to_right(self, node, queue, level):
        if node.right and node.right.val != None:
            queue.put((node.right, level))
        if node.left and node.left.val != None:
            queue.put((node.left, level))

    def reverse_queue(self, queue, node_data):
        queue_list = [node_data] + list(queue.queue)
        queue = Queue()
        [queue.put(item) for item in queue_list[::-1]]
        return queue

    def parse_node_print_dict(self, node_print_dict):
        output_list = []
        for key in sorted(node_print_dict.keys()):
            output_list.append(node_print_dict[key])
        return output_list
