# Window Starting Point

Given a list of keywords and a list of search words,
return a list of indices that indicate the beginning
of a sequence of adjacent keywords.

**Examples:**

    search_list = ['hello', 'hi', 'hi', 'greetings', 'hi', 'greetings', 'hey', 'hi']
    keywords = ['hi', 'hey', 'greetings']
    Output: [4, 5]
    Explanation: The 3 element at/after index 4 are the 3 elements we're looking for in keywords ('hi', 'greetings', 'hey'). Same thing for index 5 ('greetings', 'hey', 'hi')

**Examples 2:**

    search_list = [
        'peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers', 'a',
        'peck', 'of', 'pickled', 'peppers', 'peter', 'piper', 'picked', 'if',
        'peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers',
        'wheres', 'the', 'peck', 'of', 'pickled', 'peppers', 'peter', 'piper', 'picked']
        keywords = ['a', 'peter', 'picked', 'piper']
    Output: [0, 17]

**Examples 3:**

    search_list = ['i', 'saw', 'susie', 'sitting', 'in', 'a', 'shoe', 'shine', 'shop', 'where', 'she', 'sits', 'she', 'shines', 'and', 'where', 'she', 'shines', 'she', 'sits']
    keywords = ['she', 'sits', 'shines']
    Output: [11, 17]