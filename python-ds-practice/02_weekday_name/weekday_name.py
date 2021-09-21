def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if day_of_week == 1:
        dow = 'Sunday'
    elif day_of_week == 2:
        dow = 'Monday'
    elif day_of_week == 3:
        dow = 'Tuesday'
    elif day_of_week == 4:
        dow = 'Wednesday'
    elif day_of_week == 5:
        dow = 'Thursday'
    elif day_of_week == 6:
        dow = 'Friday'
    elif day_of_week == 7:
        dow = 'Saturday'
    else:
        dow = None

    return dow


if __name__ == '__main__':
    import doctest
    doctest.testmod()
