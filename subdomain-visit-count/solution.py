class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        self.domain_tracking = {}

        for domain_entry in cpdomains:
            domain_entry = domain_entry.split(" ")
            count = domain_entry[0]
            domain = domain_entry[1]

            domains = self.get_domains(domain)
            self.track_domains(domains, int(count))

        return ["{} {}".format(value, key) for key, value in self.domain_tracking.iteritems()]

    def get_domains(self, domain):
        domains = []
        for x in range(len(domain) - 1, -1, -1):
            if domain[x] == ".":
                domains.append(domain[x + 1::])
        domains.append(domain)
        return domains

    def track_domains(self, domains, count):
        for domain in domains:
            if not self.domain_tracking.get(domain):
                self.domain_tracking[domain] = 0
            self.domain_tracking[domain] += count
