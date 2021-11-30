class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()

        for email in emails:
            local_x_domain = email.split("@")

            domain = local_x_domain[1]
            local = local_x_domain[0]

            local_no_dots = local.replace(".", "")
            strip_plus_local = local_no_dots.split("+")

            email_set.add(strip_plus_local[0] + "@" + domain)
        return len(email_set)
