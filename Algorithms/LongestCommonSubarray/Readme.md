# Longest Common Subarray

We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

**Sample input:**

    user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
    user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
    user2 = ["a", "/one", "/two"]
    user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
    user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
    user5 = ["a"]

**Sample output:**

    findContiguousHistory(user0, user1) => /pink / => ister /orange
    findContiguousHistory(user1, user2) => (empty)
    findContiguousHistory(user2, user0) => /a
    findContiguousHistory(user3, user4) => /plum /blue /tan /red
    findContiguousHistory(user4, user3) => /plum /blue /tan /red

>n: length of the first user's browsing history
>m: length of the second user's browsing history