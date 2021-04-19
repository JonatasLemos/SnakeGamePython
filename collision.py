def collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + 40:
        if y1 >= y2 and y1 < y2 + 40:
            return True
    return False