class TrieNode:
    def __init__(self):
        self.words = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.words:
                curr.words[c] = TrieNode()
            curr = curr.words[c]
        curr.end_of_word = True
            
    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(j, root):
        
            curr = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for nxt in curr.words.values():
                       if  dfs(i+1, nxt):
                        return True
                    return False

                else:
                    if word[i] not in curr.words.keys():
                        return False
                    curr = curr.words[word[i]]
            return curr.end_of_word

        return dfs(0, curr)
                    




        
