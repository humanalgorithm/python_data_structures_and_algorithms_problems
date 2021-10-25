class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        self.path_dict, self.PATHS, self.FILE_NAME = {}, "paths", "file_name"

        for file_info in paths:
            path_and_files = file_info.split(" ")
            path = path_and_files[0]
            files = path_and_files[1::]
            file_meta_list = self.get_file_meta(files)
            self.update_path_dict(file_meta_list, path)

        return [[path for path in value[self.PATHS]]
                for key, value in self.path_dict.iteritems() if len(value[self.PATHS]) > 1]

    def get_file_meta(self, files):
        file_meta_list = []
        for file_meta in files:
            paren_index = file_meta.find("(")
            file_hash = hash(file_meta[paren_index:])
            file_name = file_meta[0:paren_index]
            file_meta_list.append([file_hash, file_name])
        return file_meta_list

    def update_path_dict(self, file_meta_list, file_path):
        for file_meta in file_meta_list:
            file_hash, file_name = file_meta[0], file_meta[1]
            if not self.path_dict.get(file_hash):
                self.path_dict[file_hash] = {self.PATHS: [], self.FILE_NAME: ""}
            self.path_dict[file_hash][self.PATHS].append(file_path + "/" + file_name)
