from collections import deque

def readingVertically(arr):
    clean = [word.strip() for word in arr]
    strings = deque([word for word in clean if len(word)])
    buffer = []
    while strings:
        cur = strings.popleft()
        first_char, remaining = cur[0], cur[1:]
        buffer.append(first_char)
        if len(remaining):
            strings.append(remaining)
    return ''.join(buffer)