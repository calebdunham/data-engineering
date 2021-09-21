def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    return [x for (i, x) in enumerate(lst) if i % 2 == 0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
