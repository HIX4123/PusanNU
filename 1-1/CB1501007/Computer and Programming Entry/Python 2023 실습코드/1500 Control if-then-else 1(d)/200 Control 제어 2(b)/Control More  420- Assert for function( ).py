
def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
    assert len(rect) == 4, '사각형은 반드시 4개의 점으로 구성되어야 함.'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'X 좌표값의 오류'
    assert y0 < y1, 'Y 좌표값의 오류'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'upper_x 범위 오류'
    assert 0 < upper_y <= 1.0, 'upper_y 범위 오류'

    return (0, 0, upper_x, upper_y)


print(normalize_rectangle( (0.0, 1.0, 2.0) )) # missing the fourth coordinate