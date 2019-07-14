"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
"""

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        trie = self.dict
        for ch in word[:-1]:
            if ch in trie:
                trie = trie[ch][1]
            else:
                trie[ch] = [False, dict()]
                trie = trie[ch][1]

        if word[-1] in trie:
            trie[word[-1]][0] = True
        else:
            trie[word[-1]] = [True, dict()]



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie = self.dict

        for ch in word:
            if ch not in trie:
                return False
            else:
                result = trie[ch][0]
                trie = trie[ch][1]

        return result


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        trie = self.dict
        for ch in prefix:
            if ch not in trie:
                return False
            trie = trie[ch][1]

        return True
