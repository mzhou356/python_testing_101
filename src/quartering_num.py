def quartering_num(num):
    """quarter a number, num
    >>> quarter_num(5)
    1.25
    >>> quarter_num(0)
    0
    >>> quarter_num(-3)
    -0.75
    """
    if isinstance(num, bool) or (not (isinstance(num, int ) or isinstance(num, float))):
        raise TypeError
    return num*0.25