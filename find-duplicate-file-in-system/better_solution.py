class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        file_dict = defaultdict(list)

        for path_info in paths:
            data = path_info.split(" ")
            dirpath = data[0]
            for entry in data[1:]:
                contents = entry.split(".")
                filedata = contents[-1]
                filename = contents[0]

                file_dict[filedata].append((dirpath, filename))

        output = []
        for key, datalist in file_dict.items():
            if len(datalist) > 1:
                result = []
                for entry in datalist:
                    ext = key.split("(")[0]
                    dirpath = entry[0]
                    filename = entry[1]
                    result.append(dirpath + "/" + filename + "." + ext)
                output.append(result)

        return output
