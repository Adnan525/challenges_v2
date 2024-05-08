# vectors will be collinear if x1 * y2 == y1 * x2

def collinearity(x1, y1, x2, y2):
    temp = [x1, y1, x2, y2]
    if temp.count(0) == 4 or temp.count(0) == 3:
        return True
    if temp.count(0) == 2:
        if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
            return True
        if x1 == 0 and x2 == 0:
            return True
        if y1 == 0 and y2 == 0:
            return True
        if x1 == 0 and y2 == 0:
            return False
    if x2!=0 and y2!=0:
        return True if x1/x2 == y1/y2 else False
    else:
        return False

collinear_optim = lambda a, b, c, d : a*d == b*c

print(collinear_optim(0, 1, 6, 0))