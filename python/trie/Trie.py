from TrieNode import TrieNode
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        length = len(key)
        current = self.root
        for ind in range(length):
            try:
                current = current.children[key[ind]]
            except(Exception ex):
                new_trie_node = TrieNode()
                current.children[key[ind]] = new_trie_node
                current = new_trie_node
        current.is_end_of_word = True

    def search(self, key):
        length = len(key)
        current = self.root
        for ind in range(length):
            if(key[ind] not in current.children):
                return False
            current = current.children[key[ind]]
        return (not(current is None) and current.is_end_of_word)

    def remove(self, key):
        return self.removeUtil(self.root, key, 0)

    def removeUtil(self, root, key, deapth):
        if(not root):
            return None

        if(deapth == len(key)):
            if(root.is_end_of_word):
                root.is_end_of_word = False
            if(len(root.children) == 0):
                root = None
            return root

        root.children[key[deapth]] = self.removeUtil(root.children[key[deapth]], key, deapth+1)

        if(len(root.children) == 0 and not root.is_end_of_word):
            root = None
        return root

if __name__ == '__main__':
    trie = Trie()
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their"]

    for ele in keys:
        trie.insert(ele)

    #print(trie.search("the"))
    #print(trie.search("these"))
    trie.remove("there")
    print(trie.search("there"))
