from collections import defaultdict


class TrieNode(object):
    def __init__(self, _char, _is_sen, _children, _prefix, _count):
        self.char = _char
        self.is_sen = _is_sen
        self.children = _children
        self.prefix = _prefix
        self.count = _count


class AutocompleteSystem(object):

    def __init__(self, _sentences, _times):
        self.trie_root = TrieNode("", False, {}, "", 0)
        self.sentences = _sentences
        self.times = _times
        self.last_input = ""
        self.insert_sentences()

    def insert_sentences(self):
        for index, sen in enumerate(self.sentences):
            self.insert_sentence(sen, self.times[index])

    def insert_sentence(self, sentence, initial_count=None):
        curr, curr_prefix = self.trie_root, ""

        for x in range(0, len(sentence)):
            curr_prefix += sentence[x]
            char = sentence[x]
            if curr.children.get(char):
                curr = curr.children.get(char)
            else:
                new_node = TrieNode(char, False, {}, curr_prefix, 0)
                curr.children[char] = new_node
                curr = new_node
        curr.is_sen = True
        if initial_count:
            curr.count = initial_count
        else:
            curr.count += 1

    def get_sens_from_prefix_node(self, prefix_node):
        results, stack = [], []
        stack.append(prefix_node)
        if not prefix_node:
            return []
        while stack:
            node = stack.pop()
            if node.is_sen:
                results.append((node.prefix, node.count))
            for key in node.children.keys():
                stack.append(node.children[key])
        return results

    def get_node_for_prefix(self, prefix):
        curr = self.trie_root
        for char in prefix:
            curr = curr.children.get(char)
            if not curr:
                return None
        return curr

    def get_sens(self, prefix):
        prefix_node = self.get_node_for_prefix(prefix)
        sens = self.get_sens_from_prefix_node(prefix_node)
        return sens

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != "#":
            self.last_input += c
            sentences = self.get_sens(self.last_input)
            return self.filter_results(sentences)
        else:
            self.insert_sentence(self.last_input)
            self.last_input = ""
            return []

    def filter_results(self, results):
        result_dict = defaultdict(list)
        for entry in results:
            result_dict[entry[1]].append(entry[0])
        filtered_results = []
        for key in sorted(result_dict.keys(), reverse=True):
            filtered_results += sorted(result_dict[key])
        return filtered_results[0:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
