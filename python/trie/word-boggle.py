from Trie import Trie

def match_words_in_dictionary(boggle, result):
    global trie
    children = trie.root.children
    srcs = trie.root.children.keys()

    for i in range(len(boggle)):
        for j in range(len(boggle[i])):
            if(boggle[i][j] in srcs and not children[boggle[i][j]].visited):
                match_words_util(i, j, children[boggle[i][j]], boggle, boggle[i][j], result)
    # for src in srcs:
    #     match_words_util(trie.root.children[src], src, result)

def is_safe(i, j):
    global boggle
    row = len(boggle)
    col = len(boggle[0])
    return i>=0 and i<row and j>=0 and j<col

def match_words_util(row, col, src, boggle, part_string, result):
    src.visited = True
    if(src.is_end_of_word):
        result.append(part_string)
    adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i,j in adjacents:
        i = row+i
        j = col+j
        if(is_safe(i, j) and boggle[i][j] in src.children and not src.children[boggle[i][j]].visited):
            match_words_util(i, j, src.children[boggle[i][j]], boggle, part_string+boggle[i][j], result)
        

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
match_words_in_dictionary(boggle, words_in_boggle)
print(words_in_boggle)