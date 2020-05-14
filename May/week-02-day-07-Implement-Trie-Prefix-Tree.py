'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Node:
  def __init__(self, terminating=False):
    self.terminating = terminating
    self.word_map = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
          if c in node.word_map:
            node = node.word_map[c]
          else:
            node.word_map[c] = Node()
            node = node.word_map[c]
        node.terminating = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        
        node = self.root
        for c in word:
          if c in node.word_map:
            node = node.word_map[c]
          else:
            return False
        return node.terminating

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix == '':
          return False
        node = self.root
        for c in prefix:
          if c in node.word_map:
            node = node.word_map[c]
          else:
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
