class Trie:
    
    def __init__(self):
        """
    Initialize your data structure here.
        """
        self.a=[]

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.a.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.a.count(word)>0

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        
        """
        for x in self.a:
            try:
                if x.index(prefix)==0 :
                    return 1

            except:
                continue
        return 0
                    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
