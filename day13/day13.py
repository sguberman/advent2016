def is_wall(x, y, secret=10):
    """
    Determine whether a given `x,y` coordinate will be a wall or an open space.
    """
    num = x*x + 3*x + 2*x*y + y + y*y + secret
    return bool(sum(1 for x in bin(num)[2:] if x == '1') % 2)
