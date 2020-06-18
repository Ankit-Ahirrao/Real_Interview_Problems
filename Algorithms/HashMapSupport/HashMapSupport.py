def insert(memo, q):
    k, v = q
    memo[k] = v

def addToValue(memo, q):
    v_delta = q[0]
    for k in memo:
        memo[k] += v_delta
        
def addToKey(memo, q):
    k_delta = q[0]
    ret = {k+k_delta: v for k, v in memo.items()}
    return ret

def get(memo, q):
    k = q[0]
    return memo[k] if k in memo else 0

def hashMap(queryType, query):
    queries = zip(queryType, query)
    memo, result = {}, 0
    for q_type, q in queries:
        if q_type == 'insert':
            insert(memo, q)
        if q_type == 'addToKey':
            memo = addToKey(memo, q)
        if q_type == 'addToValue':
            addToValue(memo, q)
        if q_type == 'get':
            result += get(memo, q)
    return result