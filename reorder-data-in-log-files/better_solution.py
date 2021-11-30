class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        log_strings_alpha = defaultdict(list)
        dig_logs, output = [], []

        for log in logs:
            log_text = " ".join(log.split()[1:])
            if self.checkDigit(log_text):
                dig_logs.append(log)
            else:
                log_strings_alpha[log_text].append(log)

        sorted_alpha = sorted(log_strings_alpha.keys())

        for text in sorted_alpha:
            logs = sorted(log_strings_alpha[text])
            output += logs
        return output + dig_logs

    def checkDigit(self, log):
        return True if log[0].isdigit() else False
