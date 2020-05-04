# Anagram Difference

An anagram is a word whose characters can be rearranged to create another word. 
Given two strings, determine the minimum number of characters in either string that must be modified to make the two strings anagrams . If it is not possible to make the two strings anagrams, return -1.

**Example:**

    a = ['tea', 'tea', 'act']
    b = ['ate', 'toe', 'acts']
    a[0] = tea and b[0] = ate are anagrams, so 0 characters need to be modified.
    a[1] = tea and b[1] = toe are not anagrams. Modify 1 character in either string (o → a or a → o) to make them anagrams.
    a[2] = act and b[2] = acts are not anagrams and cannot be converted to anagrams because they contain different numbers of characters.The return array is [0, 1, -1]

**Function Description**

    Complete the function getMinimumDifference in the editor below.
    getMinimumDifference has the following parameter(s):
    string a[n]: an array of strings
    string b[n]: an array of strings
    Return int[n]: an array of integers which denote the minimum number of characters in either string that need to be modified to make the two strings anagrams. If it is not possible, return -1.

**Constraints**

Each string consists of lowercase characters [a-z].
1 ≤ n ≤ 1000 ≤ |a[i]|,
|b[i]| ≤ 1041 ≤ |a[i]| + |b[i]| ≤ 104