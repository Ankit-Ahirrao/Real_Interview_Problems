# Given two words where backspaces is represented as 'B',
# determine if two words are the equal.
# ​
# ex:
# "foobarBB" and "foo23BBb" -> true

from collections import defaultdict

def compare (a_str,b_str):
    a = back_space(a_str)
    b = back_space(b_str)
    return a == b

def back_space (word):
    stack = []
    for char in word:
        if char == "B":
            if len(stack) > 0: stack.pop()
        else: 
            stack.append(char)
    return "".join(stack)

test_cases = [
    ('abc123BB', 'abcdeBB1'),
    ('BBBBBB', 'BBBBBBBBBBB'),
    ('', ''),
    ('', 'BBBBBBBBBB'),
    ('BBBBBBBBB', ''),
    ('', 'AB'),
    ('', 'ABC'),
    ('CBA', 'A'),
    ('ABBBBBBBB', 'AABBBBBBB'),
]

expected = [
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
]

num_passed = 0
print(f'XXXX TESTING {compare.__name__}')
for case, sol in zip(test_cases, expected):
    res = compare(*case)
    if res != sol:
        print(f'[TEST] CASE "{case}" failed')
        print(f'       GOT: {res}, EXPECTED: {sol}')
    else:
        num_passed += 1

print(f'{num_passed}/{len(test_cases)} cases passed!')

