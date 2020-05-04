def iterate(upRight):
    for coordinates in upRight:
        for i,v in enumerate(coordinates):
            if v == ' ':
                yield int(coordinates[0:i]), int(coordinates[i+1:])
                break

def countMax(upRight):
    end_row, end_col = math.inf, math.inf
    for row, col in iterate(upRight):
        end_row = min(end_row, row)
        end_col = min(end_col, col)
    return end_col*end_row