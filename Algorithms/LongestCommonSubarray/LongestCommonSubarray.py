def LongestCommonSubarray(user1, user2):
    m, n = len(user1)+1, len(user2)+1
    dp = [[0]*n for _ in range(m)]
    longest = 0
    end_ind = -1
    for i in range(m):
        for j in range(n):
            if not i or not j: continue
            if user1[i-1] == user2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > longest:
                    longest = max(longest, dp[i][j])
                    end_ind = i
    return [] if end_ind == -1 else user1[end_ind-longest:end_ind]

# Given 2 square find overlap
# Given paragraph, print parameter string counter clocker