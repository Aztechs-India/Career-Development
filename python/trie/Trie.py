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
            except:
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
        return (current != None and current.is_end_of_word)

if __name__ == '__main__':
    trie = Trie()
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their"]

    for ele in keys:
        trie.insert(ele)

    print(trie.search("the"))
    print(trie.search("these"))