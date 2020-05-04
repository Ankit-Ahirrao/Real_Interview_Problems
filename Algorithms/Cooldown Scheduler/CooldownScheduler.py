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
