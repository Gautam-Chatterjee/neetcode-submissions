class TrieNode:
    def __init__(self):
        self.words = {}
        self.end_of_word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root 
        for c in word:
            if c not in curr.words:
                curr.words[c] = TrieNode()
            curr = curr.words[c]
        curr.end_of_word = True



    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.words:
                return False
            curr = curr.words[c]
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.words:
                return False
            curr = curr.words[c]
        return True

        
        