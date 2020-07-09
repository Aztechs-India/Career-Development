from Trie import Trie

def match_words_in_dictionary(boggle, result, trie):
    children = trie.root.children
    srcs = trie.root.children.keys()

    for i, v1 in enumerate(boggle):
        for j, v2 in enumerate(boggle[i]):
            if(boggle[i][j] in srcs and not children[boggle[i][j]].visited):
                match_words_util(i, j, children[boggle[i][j]], boggle, boggle[i][j], result)

def is_safe(i, j, src, boggle):
    row = len(boggle)
    col = len(boggle[0])
    if(i>=0 and i<row and j>=0 and j<col):
        curr = boggle[i][j]
        return curr in src.children and not src.children[curr].visited
    return False

def match_words_util(row, col, src, boggle, part_string, result):
    src.visited = True
    if(src.is_end_of_word):
        result.append(part_string)
    adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i,j in adjacents:
        i = row+i
        j = col+j
        if(is_safe(i, j, src, boggle)):
            curr = boggle[i][j]
            match_words_util(i, j, src.children[curr], boggle, part_string+curr, result)

words = ['GEEKS', 'FOR', 'QUIZ', 'GO']

boggle = [
    ['G', 'I', 'Z'],
    ['U', 'E', 'K'],
    ['Q', 'S', 'E']
]

#Insert words to trie
trie = Trie()
for word in words:
    trie.insert(word)

words_in_boggle = []
match_words_in_dictionary(boggle, words_in_boggle, trie)
print(words_in_boggle)