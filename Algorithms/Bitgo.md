def  isPrime(n):
    root = int(n**(1/2))
    for factor in range(2, root+1):
        if n%factor == 0: return factor
    return 1

def maxTrailing(levels):
    maximum = 0
    always_decrease = False
    for i in range(1, len(levels)):
        cur = levels[i]
        levels[i] = min(levels[i], levels[i-1])
        cur_high = cur-levels[i]
        if cur_high > 0: always_decrease = True
        maximum = max(maximum, cur_high)
    return maximum if always_decrease else -1

def add_buffer(task, most_recent, str_buffer, cooldown):
    if task not in most_recent: return
    distance = len(str_buffer) - most_recent[task]
    for _ in range(cooldown-distance):
        str_buffer.append('.')

def schedule(tasks, cooldown):
    str_buffer = []
    most_recent = {}
    for task in tasks:
        add_buffer(task, most_recent, str_buffer, cooldown)
        str_buffer.append(task)
        most_recent[task] = len(str_buffer)
    return ''.join(str_buffer)
