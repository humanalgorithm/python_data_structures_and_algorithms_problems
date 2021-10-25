from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.flight_dict = defaultdict(list)
        [self.flight_dict[ticket[0]].append(ticket[1]) for ticket in tickets]
        [self.flight_dict[k].sort() for k in self.flight_dict.keys()]

        flight_path = []
        self.get_flight_path("JFK", flight_path, [], len(tickets))
        return flight_path

    def get_flight_path(self, node, flight_path, visited, ticket_count):
        flight_path.append(node)
        if len(flight_path) == ticket_count + 1:
            return True

        for next_node in self.flight_dict.get(node, []):
            if visited.count((node, next_node)) != self.flight_dict[node].count(next_node):
                visited.append((node, next_node))
                if self.get_flight_path(next_node, flight_path, visited, ticket_count):
                    return True
                visited.remove((node, next_node))
        flight_path.pop()
