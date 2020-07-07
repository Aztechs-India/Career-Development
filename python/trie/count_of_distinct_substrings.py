from Trie import Trie
from RefInteger import RefInteger

def get_number_of_nodes(root, ref_int):
    if(root is None):
        return
    root.visited = True
    ref_int.increment()
    for children, trie_node in root.children.items():
        if(not trie_node.visited):
            get_number_of_nodes(trie_node, ref_int)

trie = Trie()

input_string = "ababa"

for i in range(len(input_string)):
    suffix = input_string[i:]
    trie.insert(suffix)

ref_int = RefInteger()
get_number_of_nodes(trie.root, ref_int)
print(ref_int.value)