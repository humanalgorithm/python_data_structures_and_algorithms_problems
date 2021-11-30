class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        min_diff = sys.maxint

        k_points, solution = [], []

        for point in points:
            x2_minus_x1 = (point[0] - 0) ** 2
            y2_minus_y1 = (point[1] - 0) ** 2
            sum_diff = x2_minus_x1 + y2_minus_y1
            sqrt_sum = sum_diff ** .5
            heapq.heappush(k_points, (sqrt_sum, point))

        for x in range(0, k):
            solution.append(heapq.heappop(k_points)[1])
        return solution
