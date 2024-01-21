
# Q1: Implement a function to search for a word in a trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


# Q2: Write a function to find all words in a trie that start with a given prefix.



def find_words_with_prefix(self,trie, prefix):
    node = trie.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    words = []
    self._dfs(node, prefix, words)
    return words


def _dfs(node, current_word, words, self=None):
    if node.is_end_of_word:
        words.append(current_word)

    for char, child_node in node.children.items():
        self._dfs(child_node, current_word + char, words)



# Q3: Solve a real-world problem using a tree data structure.

# File System Organization.

class FileSystemNode:
    def __init__(self, name, is_directory=True):
        self.name = name
        self.is_directory = is_directory
        self.children = {}


class FileSystemTree:
    def __init__(self):
        self.root = FileSystemNode("/")

    def add_path(self, path):
        current_node = self.root
        components = path.split('/')
        for component in components[1:]:
            if component not in current_node.children:
                current_node.children[component] = FileSystemNode(component)
            current_node = current_node.children[component]

    def list_files(self, path):
        current_node = self.root
        components = path.split('/')
        for component in components[1:]:
            if component not in current_node.children:
                return []
            current_node = current_node.children[component]

        return self._list_files_helper(current_node)

    def _list_files_helper(self, node):
        files = []
        if not node.is_directory:
            return [node.name]

        for child_node in node.children.values():
            files.extend(self._list_files_helper(child_node))

        return files