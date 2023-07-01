class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def suggest(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions = []
        self._collect_words(node, prefix, suggestions)
        return suggestions

    def _collect_words(self, node, prefix, suggestions):
        if node.end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, suggestions)


# trie = Trie()
# trie.insert("cat")
# trie.insert("cats")
# trie.insert("cattle")
# trie.insert("marc")
# print(trie.search("cats"))  # Output: True
# print(trie.search("dog"))  # Output: False
# print(trie.starts_with("ca"))  # Output: True
#
# print(trie.root.children)

trie = Trie()
words = ["cat", "cattle", "cats", "marc", "marcus", "cathedral"]
for word in words:
    trie.insert(word)

print(trie.suggest("m"))  # Output: ['he', 'help', 'hello']
# print(trie.suggest("h"))  # Output: ['he', 'help', 'hello', 'hey', 'hi']
# print(trie.suggest("w"))  # Output: ['world']
# print(trie.suggest("z"))  # Output: []
