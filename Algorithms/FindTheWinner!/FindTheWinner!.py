def winner(andrea, maria, s):
    a_score = 0
    m_score = 0
    start = 0 if s == 'Even' else 1
    for i in range(start, len(andrea), 2):
        a_score += andrea[i] - maria[i]
        m_score += maria[i] - andrea[i]
    if a_score == m_score: return "Tie"
    return "Maria" if m_score > a_score else "Andrea"