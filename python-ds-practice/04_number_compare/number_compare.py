def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        res = 'Numbers are equal'
    elif a < b:
        res = 'Second is greater'
    elif a > b:
        res = 'First is greater'
    else:
        res = None

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
