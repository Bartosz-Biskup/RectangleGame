def ranges_collision(a1, a2, b1, b2):
    if a2 > b1 or b2 > a1:
        return True

    return False