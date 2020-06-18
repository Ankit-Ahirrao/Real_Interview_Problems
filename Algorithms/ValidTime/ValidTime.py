def validTime(time):
    hr, mn = time.split(':')
    is_valid_hr = 0 <= int(hr) <= 23
    is_valid_mn = 0 <= int(mn) <= 59
    return is_valid_hr and is_valid_mn