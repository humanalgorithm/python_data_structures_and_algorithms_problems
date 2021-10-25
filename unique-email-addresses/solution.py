class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local = ""
            domain = ""
            ignore_after_plus = False
            seen_at = False
            for index, char in enumerate(email):
                if seen_at:
                    domain += char
                elif char == "@":
                    seen_at = True
                    continue

                if ignore_after_plus and not seen_at:
                    continue
                elif char == "+":
                    ignore_after_plus = True
                    continue

                if not seen_at and char != ".":
                    local += char
            email_set.add(local + "@" + domain)
        return len(email_set)
