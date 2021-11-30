class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        count_dict = defaultdict(int)

        for entry in cpdomains:
            data = entry.split(" ")
            count = int(data[0])
            domains = data[1].split(".")

            for x in range(len(domains) - 1, -1, -1):
                domain = ".".join(domains[x:])
                count_dict[domain] += count

        return ["{} {}".format(value, key) for key, value in count_dict.items()]