def pattern_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n-m+1):
        ind = 0
        while(ind < m):
            if(pattern[ind] != text[ind+i]):
                break
            ind += 1
        if(ind == m):
            print("Found at index", i)

pattern_match("This is a test text", "test")