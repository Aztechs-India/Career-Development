from Trie import Trie
from TrieNode import TrieNode

class UniqueRow(Trie):

    def insert(self, key):
        current = self.root
        new_entry = False
        for i in key:
            if(i not in current.children):
                new_entry = True
                current.children[i] = TrieNode()
            current = current.children[i]        
        if(not(not new_entry and current.is_end_of_word)):
            print(" ".join(key))
        current.is_end_of_word = True

    def insert_boolean_rows(self, row):
        self.insert("".join(map(str, row)))

    def insert_matrix(self, matrix):
        for row in matrix:
            self.insert_boolean_rows(row)

if __name__ == "__main__":
    matrix = [
            [0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0]
        ]
    unique_row = UniqueRow()
    unique_row.insert_matrix(matrix)
