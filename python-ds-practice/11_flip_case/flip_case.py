def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap_phrase = ''.join([x.swapcase() if x.lower() == to_swap.lower() else x for x in phrase])
    return swap_phrase


if __name__ == '__main__':
    import doctest
    doctest.testmod()
