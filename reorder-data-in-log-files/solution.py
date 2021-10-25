class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        alpha_logs, num_logs = [], []
        for index, entry in enumerate(logs):
            entry = entry.split()
            is_number = not entry[1].isalpha()
            data_entry = {"index": index, "identifier": entry[0], "data": str(" ".join(entry[1:]))}
            if is_number:
                num_logs.append(data_entry)
            else:
                alpha_logs.append(data_entry)

        output_sorted = sorted(alpha_logs, key=lambda x: (x["data"], x["identifier"]))
        output_sorted += sorted(num_logs, key=lambda x: x["index"])

        return [entry["identifier"] + " " + entry["data"] for entry in output_sorted]
